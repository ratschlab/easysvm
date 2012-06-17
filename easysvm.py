#############################################################################################
#                                                                                           #
#    This class is part of the MLB-Galaxy package, adding some sequence analysis            #
#    functionality to PSU's Galaxy framework.                                               #
#    Copyright (C) 2008 Cheng Soon Ong <chengsoon.ong@tuebingen.mpg.de>                     #
#    Copyright (C) 2008 Gunnar Raetsch <Gunnar.Raetsch@tuebingen.mpg.de>                    #
#    Copyright (C) 2007 Sebastian J. Schultheiss <sebi@umich.edu>                           #
#                                                                                           #
#    This program is free software; you can redistribute it and/or modify                   #
#    it under the terms of the GNU General Public License as published by                   #
#    the Free Software Foundation; either version 3 of the License, or                      #
#    (at your option) any later version.                                                    #
#                                                                                           #
#    This program is distributed in the hope that it will be useful,                        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                           # 
#    GNU General Public License for more details.                                           #
#                                                                                           #
#    You should have received a copy of the GNU General Public License                      # 
#    along with this program; if not, see http://www.gnu.org/licenses                       #
#    or write to the Free Software Foundation, Inc., 51 Franklin Street,                    #
#    Fifth Floor, Boston, MA 02110-1301  USA                                                #
#                                                                                           #
#############################################################################################
#                                                                                           #
#  Original Author: Sebastian J. Schultheiss, version 0.77                                  #
#  Please add a notice of any modifications here:                                           #
#     Gunnar Raetsch: rewrote code for training on sequences to be read from files          #
#     Cheng Soon Ong: Added code for educational toolbox                                    #
#                                                                                           #
#############################################################################################

import sys
import random

sys.path.append('/fml/ag-raetsch/share/software/galaxy/shogun/lib/python2.5/site-packages')
#sys.path.append('/fml/ag-raetsch/share/software/python_tools/lib/python2.5/site-packages')
#sys.path.append('/Users/raetsch/projects/shogun/lib/python2.5/site-packages/')
import shutil
import numpy
from numpy import sign, where, array, ones
import parse
import utils

import shogun
from shogun.Kernel import GaussianKernel, WeightedDegreePositionStringKernel
from shogun.Kernel import LinearKernel, PolyKernel, LocalAlignmentStringKernel, LocalityImprovedStringKernel,CommWordStringKernel
from shogun.Features import RealFeatures, Labels, StringCharFeatures, DNA, StringWordFeatures
from shogun.Classifier import LibSVM
from shogun.PreProc import SortWordString

from utils import calcprc, calcroc, accuracy
from utils import getPartitionedSet, getCurrentSplit
import plots

from poim import reshape_normalize_contribs, compute_weight_mass

################################################################################
# helper functions

def create_features(kname, examples, kparam, train_mode):
    """Converts numpy arrays or sequences into shogun features"""

    if kname == 'gauss' or kname == 'linear' or kname == 'poly':
        examples = numpy.array(examples)
        feats = RealFeatures(examples)
        
    elif kname == 'wd' or kname == 'localalign' or kname == 'localimprove':
        feats = StringCharFeatures(DNA)
        feats.set_string_features(examples)

    elif kname == 'spec':
        feats = StringCharFeatures(DNA)
        feats.set_string_features(examples)

        wf = StringWordFeatures( feats.get_alphabet() )
        wf.obtain_from_char(feats, kparam['degree']-1, kparam['degree'], 0, False)
        del feats

        if True:#train_mode:
            pre = SortWordString()
            pre.init(wf)
            wf.add_preproc(pre)
        ret = wf.apply_preproc()
        #assert(ret)

        feats = wf 

    else:
        print 'Unknown kernel %s' % kname
    
    return feats

def create_kernel(kname,kparam,feats_train):
    """Call the corresponding constructor for the kernel"""

    if kname == 'gauss':
        kernel = GaussianKernel(feats_train, feats_train, kparam['width'])
    elif kname == 'linear':
        kernel = LinearKernel(feats_train, feats_train, kparam['scale'])
    elif kname == 'poly':
        kernel = PolyKernel(feats_train, feats_train, kparam['degree'], kparam['inhomogene'], kparam['normal'])
    elif kname == 'wd':
        kernel=WeightedDegreePositionStringKernel(feats_train, feats_train, kparam['degree'])
        kernel.set_shifts(kparam['shift']*numpy.ones(kparam['seqlength'],dtype=numpy.int32))
    elif kname == 'spec':
        kernel = CommWordStringKernel(feats_train, feats_train)
    elif kname == 'localalign':
        kernel = LocalAlignmentStringKernel(feats_train, feats_train)
    elif kname == 'localimprove':
        kernel = LocalityImprovedStringKernel(feats_train, feats_train, kparam['length'],\
                                              kparam['indeg'], kparam['outdeg'])
    else:
        print 'Unknown kernel %s' % kname

    return kernel

def model2str(kparam,C,kp,shownames=True):
    """Generates a string describing the model parameters"""

    if kparam["modelsel_name"]==None or len(kparam["modelsel_params"])==1:
        if shownames:
            str="\tC=%1.1f" % C
        else:
            str="\t%1.2f" % C
    else:
        if type(kp)==type(int(0)):
            if shownames:
                str="\tC=%1.1f\t%s=%i" %(C, kparam["modelsel_name"], kp)
            else:
                str="\t%1.1f\t%i" %(C, kp)
        else:
            if shownames:
                str="\tC=%1.1f\t%s=%1.2f" %(C, kparam["modelsel_name"], kp)
            else:
                str="\t%1.1f\t%1.2f" %(C, kp)
    return str



def train(trainex,trainlab,C,kname,kparam):
    """Trains a SVM with the given kernel"""

    kernel_cache_size = 500
    num_threads = 2

    feats_train = create_features(kname,trainex, kparam, True)
    if kname == 'wd':
        kparam['seqlength'] = len(trainex[0])
    kernel = create_kernel(kname,kparam,feats_train)
    
    kernel.io.disable_progress()
    kernel.set_cache_size(int(kernel_cache_size))

    labels = Labels(numpy.array(trainlab,numpy.double))

    svm = LibSVM(C, kernel, labels)
    svm.parallel.set_num_threads(num_threads)
    svm.io.disable_progress()
    svm.train()

    return (svm, kernel, feats_train)

def train_and_test(trainex,trainlab,testex,C,kname,kparam):
    """Trains a SVM with the given kernel, and predict on the test examples"""

    (svm, kernel, feats_train) = train(trainex,trainlab,C,kname,kparam)
    feats_test = create_features(kname, testex, kparam, False)
    kernel.init(feats_train, feats_test)
    output = svm.classify().get_labels()
    
    return output

def compute_poims(svm, kernel, poimdegree, max_len):
    """For a trained SVM, compute Position Oligomer Importance Matrices"""

    distr = ones((max_len,4))/4 ;
    kernel.prepare_POIM2(distr)

    kernel.compute_POIM2(poimdegree, svm) ;
    poim = kernel.get_POIM2()
    kernel.cleanup_POIM2() 

    (poim, max_poim, diff_poim) = reshape_normalize_contribs(poim, poimdegree, max_len)
    (poim_weightmass, poim_totalmass) = compute_weight_mass(poim, poimdegree, max_len)

    poim_totalmass=poim_totalmass/numpy.sum(poim_totalmass)

    return (poim, max_poim, diff_poim, poim_totalmass)

def crossvalidation(cv, kname, kparam, C, all_examples, all_labels):
    """Perform cross validation using an SVM

    cv -- the number of folds
    kernel -- the kernel used
    data -- the dataset, assumed to be compatible to kernel, label is in the first column

    """
    print 'Using %i-fold crossvalidation' % cv
    
    partitions = getPartitionedSet(len(all_labels), cv)
    error = []
    sum_accuracy = 0.0
    sum_roc = 0.0
    all_outputs=[0.0] * len(all_labels)
    all_split=[-1] * len(all_labels)

    for repetition in xrange(cv):
        XT, LT, XTE, LTE = getCurrentSplit(repetition, partitions, all_labels, all_examples)
        numpos = len(where(array(LTE)>0)[0])
        svmout = train_and_test(XT, LT, XTE, C, kname, kparam)
        
        for i in xrange(len(svmout)):
            all_outputs[partitions[repetition][i]] = svmout[i]
            all_split[partitions[repetition][i]] = repetition ;
        

    return (all_outputs, all_split)

def evaluate(predictions, splitassignments, labels, roc_fname=None, prc_fname=None):
    """Evaluate prediction results
    """

    res_str = ""

    cv = 1
    if splitassignments!=None:
        for split in splitassignments:
            if split+1>cv:
                cv=int(split+1)
    if cv>1:
        res_str = "Evaluating on %i examples in %i splits\n" % (len(labels),cv)
    else:
        res_str = "Evaluating on %i examples\n" % len(labels)

    output_splits = cv* [[]]
    label_splits = cv* [[]]
    for i in xrange(cv):
        label_splits[i]=[] 
        output_splits[i]=[] 

    for i in xrange(0,len(labels)):
        if cv>1:
            split=int(splitassignments[i])
        else:
            split=0
        output_splits[split].append(predictions[i])
        label_splits[split].append(labels[i])

    error = []
    sum_accuracy = 0.0
    sum_roc = 0.0
    sum_prc = 0.0

    for split in xrange(cv):
        res_str += 'Split %d\n' % (split+1)

        LTE = label_splits[split] ;
        svmout = output_splits[split]

        numpos=0 
        for l in LTE:
            if l==1:
                numpos+=1 
        istwoclass = numpos>0 and numpos<len(LTE)
        res_str += '   number of positive examples = %i\n' % numpos
        res_str += '   number of negative examples = %i\n' % (len(LTE)-numpos)
        if istwoclass:
            auROC = calcroc(svmout,LTE)
            res_str += '   Area under ROC curve        = %2.1f %%\n' % (100.0*auROC)
            sum_roc += auROC
            if roc_fname!=None:
                if split!=cv-1:
                    plots.plotroc(svmout, LTE, split==cv-1, None, "ROC curve of SVM, split %i" % (split+1))
                else:
                    plots.plotroc(svmout, LTE, split==cv-1, roc_fname, "ROC curve of SVM, split %i" % (split+1))
            auPRC = calcprc(svmout,LTE)
            res_str += '   Area under PRC curve        = %2.1f %%\n' % (100.0*auPRC)
            sum_prc += auPRC
            if prc_fname!=None:
                if split!=cv-1:
                    plots.plotprc(svmout, LTE, None, "PRC curve of SVM, split %i" % (split+1))
                else:
                    plots.plotprc(svmout, LTE, prc_fname, "PRC curve of SVM, split %i" % (split+1))

        acc = accuracy(svmout, LTE)
        res_str += '   accuracy (at threshold 0)   = %2.1f %% \n' % (100.0*acc)
        sum_accuracy += acc

    numpos=0 
    for l in labels:
        if l==1:
            numpos+=1 

    mean_roc = sum_roc/cv
    mean_prc = sum_prc/cv
    mean_acc = sum_accuracy/cv

    res_str += 'Averages\n'
    res_str += '   number of positive examples = %i\n' % round(numpos/cv)
    res_str += '   number of negative examples = %i\n' % round((len(labels)-numpos)/cv)
    res_str += '   Area under ROC curve        = %2.1f %%\n' % (100.0*mean_roc) 
    res_str += '   Area under PRC curve        = %2.1f %%\n' % (100.0*mean_prc) 
    res_str += '   accuracy (at threshold 0)   = %2.1f %% \n' % (100.0*mean_acc) 

    return (res_str,mean_roc,mean_prc,mean_acc)

################################################################################
# main functions

def svm_cv(argv):
    """A top level script to parse input parameters and run cross validation"""

    assert(argv[1]=='cv')
    if len(argv)<5:
        sys.stderr.write("usage: %s cv repeat C kernelname [kernelparameters] [arff|fasta] inputfiles  outputfile\n" % argv[0])
        sys.exit(-1)

    # parse input parameters
    cv = int(argv[2])
    C = float(argv[3])
    (kernelname,kparam,argv_rest) = parse.parse_kernel_param(argv[4:],False)
    (examples,labels,argv_rest) = parse.parse_input_file_train(kernelname, argv_rest)
    if len(argv_rest)<1:
        sys.stderr.write("Output file missing\n")
        sys.exit(-1)
    if len(argv_rest)>1:
        sys.stderr.write("Too many arguments\n")
        sys.exit(-1)
    outfilename = argv_rest[0]

    utils.check_params(kparam, C, len(examples[0]))

    # run cross-validation
    (all_outputs, all_split) = crossvalidation(cv, kernelname, kparam, C, examples, labels)

    f = open(outfilename, 'w+')
    res_str = '#example\toutput\tsplit\n'
    f.write(res_str)
    for ix in xrange(len(all_outputs)):
	res_str = '%d\t%2.7f\t%d\n' % (ix,all_outputs[ix],all_split[ix])
        f.write(res_str)
    f.close()


def svm_modelsel(argv):
    """A top level script to parse input parameters and run model selection"""

    assert(argv[1]=='modelsel')
    if len(argv)<5:
        sys.stderr.write("usage: %s modelsel repeat Cs kernelname [kernelparameters] [arff|fasta] inputfiles  outputfile\n" % argv[0])
        sys.exit(-1)

    # parse input parameters
    cv = int(argv[2])
    Cs = parse.parse_float_list(argv[3])
    (kernelname,kparam,argv_rest) = parse.parse_kernel_param(argv[4:], True)
    (examples,labels,argv_rest) = parse.parse_input_file_train(kernelname, argv_rest)
    if len(argv_rest)<1:
        sys.stderr.write("Output file missing\n")
        sys.exit(-1)
    if len(argv_rest)>1:
        sys.stderr.write("Too many arguments\n")
        sys.exit(-1)
    outfilename = argv_rest[0]

    # run cross-validation
    mean_rocs=[] ;
    mean_prcs=[] ;
    mean_accs=[] ;
    all_Cs = [] ;
    all_kparam=[] ;

    if kparam["modelsel_name"]==None:
        for C in Cs:
            utils.check_params(kparam, C, len(examples[0]))

            (all_outputs, all_split) = crossvalidation(cv, kernelname, kparam, C, examples, labels)
            (res_str, mean_roc, mean_prc, mean_acc) = evaluate(all_outputs, all_split, labels)
            mean_rocs.append(mean_roc) 
            mean_prcs.append(mean_prc) 
            mean_accs.append(mean_acc) 
            all_Cs.append(C) 
            all_kparam.append(None) 
    else: # also optimize one kernel parameter
        for C in Cs:
            for kp in kparam["modelsel_params"]:
                kparam[kparam["modelsel_name"]] = kp 
                utils.check_params(kparam, C, len(examples[0]))

                (all_outputs, all_split) = crossvalidation(cv, kernelname, kparam, C, examples, labels)
                (res_str, mean_roc, mean_prc, mean_acc) = evaluate(all_outputs, all_split, labels)
                mean_rocs.append(mean_roc) 
                mean_prcs.append(mean_prc) 
                mean_accs.append(mean_acc) 
                all_Cs.append(C) 
                all_kparam.append(kp)

    max_roc=numpy.max(numpy.array(mean_rocs)) 
    max_prc=numpy.max(numpy.array(mean_prcs)) 
    max_acc=numpy.max(numpy.array(mean_accs)) 

    f = open(outfilename, 'w+')
    if kparam["modelsel_name"]==None or len(kparam["modelsel_params"])==1:
        detail_str = "\tC\tROC\tPRC\tAccuracy (at threshold 0)\n"
    else:
        detail_str = "\tC\t%s\tROC\tPRC\tAccuracy (at threshold 0)\n" % kparam["modelsel_name"]

    best_roc_str=''
    best_prc_str=''
    best_acc_str=''
    for i in xrange(len(all_Cs)):
        # determine the best parameter combinations
        if mean_rocs[i]==max_roc:
            rocsym='+'
            best_roc_str+=model2str(kparam, all_Cs[i], all_kparam[i])+'\n'
        else:
            rocsym=' '
        if mean_prcs[i]==max_prc:
            prcsym='+'
            best_prc_str+=model2str(kparam, all_Cs[i], all_kparam[i])+'\n'
        else:
            prcsym=' '
        if mean_accs[i]==max_acc:
            accsym='+'
            best_acc_str+=model2str(kparam, all_Cs[i], all_kparam[i])+'\n'
        else:
            accsym=' '
        
        detail_str+=model2str(kparam, all_Cs[i], all_kparam[i], False)+'\t'
        if kparam["modelsel_name"]==None or len(kparam["modelsel_params"])==1:
            detail_str += '%c%2.1f%%\t%c%2.1f%%\t%c%2.1f%%\n' % (rocsym, 100*mean_rocs[i], prcsym, 100*mean_prcs[i], accsym, 100*mean_accs[i])
        else:
            detail_str += '%c%2.1f%%\t%c%2.1f%%\t%c%2.1f%%\n' % (rocsym, 100*mean_rocs[i], prcsym, 100*mean_prcs[i], accsym, 100*mean_accs[i])

    f.write('Best model(s) according to ROC measure:\n%s' % best_roc_str)
    f.write('\nBest model(s) according to PRC measure:\n%s' % best_prc_str)
    f.write('\nBest model(s) according to accuracy measure:\n%s' % best_acc_str)

    f.write('\nDetailed results:\n')
    f.write(detail_str)

    f.close()


def svm_pred(argv):
    """A top level script to parse input parameters and train and predict"""

    assert(argv[1]=='pred')
    if len(argv)<6:
        sys.stderr.write("usage: %s pred C kernelname kernelparameters [arff|fasta] inputfiles  outputfile" % argv[0])
        sys.exit(-1)

    # parse input parameters
    C = float(argv[2])
    (kernelname,kparam,argv_rest) = parse.parse_kernel_param(argv[3:],False)
    (trainex, trainlab, testex, argv_rest) = parse.parse_input_file_train_test(kernelname, argv_rest)
    if len(argv_rest)<1:
        sys.stderr.write("Output file missing\n")
        sys.exit(-1)
    if len(argv_rest)>1:
        sys.stderr.write("Too many arguments\n")
        sys.exit(-1)
    outfilename = argv_rest[0]

    utils.check_params(kparam, C, len(trainex[0]))

    # run training and testing
    svmout = train_and_test(trainex, trainlab, testex, C, kernelname, kparam)

    # write output file
    f = open(outfilename,'w')
    res_str = '#example\toutput\n'
    f.write(res_str)
    for ix in xrange(len(svmout)):
        res_str = str(ix)+'\t'+str(svmout[ix])+'\n'
        f.write(res_str)
    
    f.close()


def svm_eval(argv):
    """A top level script to parse input parameters and evaluate"""

    assert(argv[1]=='eval')
    if len(argv)<6:
        sys.stderr.write("usage: %s eval predictionfile [arff|fasta] inputfiles outputfile [roc|prc figure.png]" % argv[0])
        sys.exit(-1)

    # parse input parameters
    (predictions, splitassignments) = parse.parse_prediction_file(argv[2])
    (trainex, trainlab, argv_rest) = parse.parse_input_file_train(None, argv[3:])
    if len(argv_rest)<1:
        sys.stderr.write("Output file missing\n")
        sys.exit(-1)
    if len(argv_rest)>3:
        sys.stderr.write("Too many arguments\n")
        sys.exit(-1)
    outfilename = argv_rest[0]
    roc_fname = None
    prc_fname = None

    if len(argv_rest)>2:
        if argv_rest[1]=='roc':
	    roc_fname=argv_rest[2]
	elif argv_rest[1]=='prc':
            prc_fname=argv_rest[2]
	else:
	    sys.stderr.write('Usage: [roc|prc]')
	    sys.exit(-1)

    # run training and testing
    (res_str,mean_roc,mean_prc,mean_acc) = evaluate(predictions, splitassignments, trainlab, roc_fname, prc_fname)

    # write output file
    f = open(outfilename,'w')
    f.write(res_str)
    f.close()

    
def svm_poim(argv):
    """A top level script to parse input parameters and plot poims"""

    assert(argv[1]=='poim')
    if len(argv)<7:
        sys.stderr.write("usage: %s poim C poimdegree wd [kernelparameters] [arff|fasta] inputfiles  poim.png\n" % argv[0])
        sys.exit(-1)

    # parse input parameters
    C = float(argv[2])
    poimdegree = int(argv[3])
    (kernelname,kparam,argv_rest) = parse.parse_kernel_param(argv[4:], False)
    (examples,labels,argv_rest) = parse.parse_input_file_train(kernelname, argv_rest)
    if len(argv_rest)<1:
        sys.stderr.write("Output file missing\n")
        sys.exit(-1)
    if len(argv_rest)>1:
        sys.stderr.write("Too many arguments\n")
        sys.exit(-1)
    poimfilename = argv_rest[0]

    utils.check_params(kparam, C, len(examples[0]))

    # train svm and compute POIMs
    (svm, kernel, feats_train) = train(examples,labels,C,kernelname,kparam)
    (poim, max_poim, diff_poim, poim_totalmass) = compute_poims(svm, kernel, poimdegree, len(examples[0]))

    # plot poims
    plots.plot_poims(poimfilename, poim, max_poim, diff_poim, poim_totalmass, poimdegree, len(examples[0]))

################################################################################
# main

if __name__ == '__main__':

    if len(sys.argv)<2:
        sys.stderr.write("usage: %s [cv|pred|modelsel|eval|poim] parameters\n" % sys.argv[0])
        sys.exit(-1)

    random.seed()

    topmode = sys.argv[1]

    if topmode == 'cv':
        svm_cv(sys.argv)
    elif topmode == 'pred':
        svm_pred(sys.argv)
    elif topmode == 'poim':
        svm_poim(sys.argv)
    elif topmode == 'eval':
        svm_eval(sys.argv)
    elif topmode == 'modelsel':
        svm_modelsel(sys.argv)
    else:
        sys.stderr.write( "unknown mode %s (use: cv, pred, poim, eval)\n" % topmode)
        sys.exit(-1)

    sys.exit(0)

