#############################################################################################
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

import sys
import random

import shutil
import numpy
from numpy import sign, where, array, ones
import parse
import utils
from poim import compute_poims

import shogun
from shogun.Kernel import GaussianKernel, WeightedDegreePositionStringKernel
from shogun.Kernel import WeightedDegreeStringKernel
from shogun.Kernel import LinearKernel, PolyKernel, LocalAlignmentStringKernel
from shogun.Kernel import LocalityImprovedStringKernel
from shogun.Kernel import CommWordStringKernel, WeightedCommWordStringKernel
from shogun.Kernel import CombinedKernel
from shogun.Kernel import FULL_NORMALIZATION, SLOWBUTMEMEFFICIENT
from shogun.Features import RealFeatures, Labels, StringCharFeatures, DNA, StringWordFeatures
from shogun.Features import CombinedFeatures
from shogun.Classifier import LibSVM,GPBTSVM

DefaultSVM = LibSVM
try:
    from shogun.Classifier import SVMLight
    LinAddSVM = SVMLight
    LinearSVM = SVMLight
except:
    LinAddSVM = GPBTSVM
    LinearSVM = LibSVM
    
from shogun.PreProc import SortWordString

from utils import calcprc, calcroc, accuracy
from utils import getPartitionedSet, getCurrentSplit
import plots

from poim import reshape_normalize_contribs, compute_weight_mass

################################################################################
# helper functions

def create_features(kname, examples, kparam, train_mode, preproc):
    """Converts numpy arrays or sequences into shogun features"""

    if kname == 'gauss' or kname == 'linear' or kname == 'poly':
        examples = numpy.array(examples)
        feats = RealFeatures(examples)
        
    elif kname == 'wd' or kname == 'localalign' or kname == 'localimprove':
        feats = StringCharFeatures(DNA)
        feats.set_string_features(examples)

    elif kname == 'spec' or kname == 'cumspec':
        feats = StringCharFeatures(DNA)
        feats.set_string_features(examples)

        wf = StringWordFeatures( feats.get_alphabet() )
        wf.obtain_from_char(feats, kparam['degree']-1, kparam['degree'], 0, kname=='cumspec')
        del feats

        if train_mode:
            preproc = SortWordString()
            preproc.init(wf)
        wf.add_preproc(preproc)
        ret = wf.apply_preproc()
        #assert(ret)

        feats = wf 
    elif kname == 'spec2' or kname == 'cumspec2':
        # spectrum kernel on two sequences
        feats = {}
        feats['combined'] = CombinedFeatures()

        reversed = kname=='cumspec2'

        (ex0,ex1) = zip(*examples)

        f0 = StringCharFeatures(DNA)
        f0.set_string_features(list(ex0))
        wf = StringWordFeatures(f0.get_alphabet())
        wf.obtain_from_char(f0, kparam['degree']-1, kparam['degree'], 0, reversed)
        del f0

        if train_mode:
            preproc = SortWordString()
            preproc.init(wf)
        wf.add_preproc(preproc)
        ret = wf.apply_preproc()
        assert(ret)
        feats['combined'].append_feature_obj(wf)
        feats['f0'] = wf

        f1 = StringCharFeatures(DNA)
        f1.set_string_features(list(ex1))
        wf = StringWordFeatures( f1.get_alphabet() )
        wf.obtain_from_char(f1, kparam['degree']-1, kparam['degree'], 0, reversed)
        del f1

        if train_mode:
            preproc = SortWordString()
            preproc.init(wf)
        wf.add_preproc(preproc)
        ret = wf.apply_preproc()
        assert(ret)
        feats['combined'].append_feature_obj(wf)
        feats['f1'] = wf

    else:
        print 'Unknown kernel %s' % kname
    
    return (feats,preproc)

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
        #kernel=WeightedDegreeStringKernel(feats_train, feats_train, kparam['degree'])
    elif kname == 'spec':
        kernel = CommWordStringKernel(feats_train, feats_train)
    elif kname == 'cumspec':
        kernel = WeightedCommWordStringKernel(feats_train, feats_train)
        kernel.set_weights(numpy.ones(kparam['degree']))
    elif kname == 'spec2':
        kernel = CombinedKernel()
        k0 = CommWordStringKernel(feats_train['f0'], feats_train['f0'])
        k0.io.disable_progress()
        kernel.append_kernel(k0)
        k1 = CommWordStringKernel(feats_train['f1'], feats_train['f1'])
        k1.io.disable_progress()
        kernel.append_kernel(k1)
    elif kname == 'cumspec2':
        kernel = CombinedKernel()
        k0 = WeightedCommWordStringKernel(feats_train['f0'], feats_train['f0'])
        k0.set_weights(numpy.ones(kparam['degree']))
        k0.io.disable_progress()
        kernel.append_kernel(k0)
        k1 = WeightedCommWordStringKernel(feats_train['f1'], feats_train['f1'])
        k1.set_weights(numpy.ones(kparam['degree']))
        k1.io.disable_progress()
        kernel.append_kernel(k1)
    elif kname == 'localalign':
        kernel = LocalAlignmentStringKernel(feats_train, feats_train)
    elif kname == 'localimprove':
        kernel = LocalityImprovedStringKernel(feats_train, feats_train, kparam['length'],\
                                              kparam['indeg'], kparam['outdeg'])
    else:
        print 'Unknown kernel %s' % kname

    kernel.set_cache_size(32) 
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

    (feats_train, preproc) = create_features(kname,trainex, kparam, True, None)
    
    if kname == 'wd':
        kparam['seqlength'] = len(trainex[0])
    kernel = create_kernel(kname,kparam,feats_train)

    if kname == 'spec2' or kname == 'cumspec2':
        kernel.init(feats_train['combined'], feats_train['combined'])
    else:    
        kernel.init(feats_train, feats_train)
    kernel.io.disable_progress()
    kernel.set_optimization_type(SLOWBUTMEMEFFICIENT)
    labels = Labels(numpy.array(trainlab,numpy.double))

    # libsvm is fine for most kernels
    if kname in ('wd', 'spec', 'cumspec', 'spec2', 'cumspec2'):
        # for the string kernels there exist specific optimizations that are only effective when using
        # a LinAdd SVM implementation (e.g. SVM-light or GPBT-SVM)
        SVMClass = LinAddSVM 
    elif kname == 'linear': 
        SVMClass = LinearSVM
    else:
        SVMClass=DefaultSVM 

    svm = SVMClass(C, kernel, labels)

    svm.io.disable_progress()
    svm.set_batch_computation_enabled(True)
    svm.set_linadd_enabled(True)
    svm.set_epsilon(1e-5)
    svm.parallel.set_num_threads(svm.parallel.get_num_cpus())
    
    svm.train()

    return (svm, kernel, feats_train, preproc)

def train_and_test(trainex,trainlab,testex,C,kname,kparam):
    """Trains a SVM with the given kernel, and predict on the test examples"""

    (svm, kernel, feats_train, preproc) = train(trainex,trainlab,C,kname,kparam)
    (feats_test, preproc) = create_features(kname, testex, kparam, False, preproc)
    if kname == 'spec2' or kname == 'cumspec2':
        for feats in feats_train.values():
            feats.io.disable_progress()
        for feats in feats_test.values():
            feats.io.disable_progress()
        kernel.init(feats_train['combined'], feats_test['combined'])
    else:    
        feats_train.io.disable_progress()
        feats_test.io.disable_progress()
        kernel.init(feats_train, feats_test)

    kernel.set_optimization_type(SLOWBUTMEMEFFICIENT)
    output = svm.classify().get_labels()
    
    return output

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
    (svm, kernel, feats_train, preproc) = train(examples,labels,C,kernelname,kparam)
    (poim, max_poim, diff_poim, poim_totalmass) = compute_poims(svm, kernel, poimdegree, len(examples[0]))

    # plot poims
    plots.plot_poims(poimfilename, poim, max_poim, diff_poim, poim_totalmass, poimdegree, len(examples[0]))

