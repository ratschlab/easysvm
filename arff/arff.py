# -*-Python-*-
################################################################################
#
# File:         arff.py
# RCS:          $Header: $
# Description:  
# Author:       Staal Vinterbo
# Created:      Mon Jan  7 12:04:28 2008
# Modified:     Wed Jan 16 17:08:38 2008 (Staal Vinterbo) staal@ding
# Language:     Python
# Package:      N/A
# Status:       Experimental
#
# arff.py is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# arff.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with arff.py; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# (c) Copyright 2008, Staal Vinterbo, all rights reserved.
#
################################################################################

__all__ = ['arffread',
           'arffwrite', 'arffalist', 'arffheader', 'vformat', 'grow']

from antlr3 import CommonTokenStream as CTS, ANTLRInputStream as AIS
from arffLexer import arffLexer
from arffParser import arffParser
import re

def arffread(fstream):
    '''read an ARFF format data set.

    Input: 
      fstream - an input stream object from which the data is read.
    Returns:
      None if an error was encountered. 
      Otherwise:
      (name, sparse, alist, m) - a tuple where
        name  : a string containing the relation name.
        sparse: a Boolean indicating whether the data is sparse.
        alist : a list of attribute type information tuples 
                (name, typecode, rest) where
                name: is a string containing the attribute name.
                typecode: an integer indicating the type of the attribute:
                    1 - number, 
                    0 - string and nominal type
                    2 - date,
                    3 - relational.
                rest: for typecode 0 this is either the empty list [] 
                          indicating 'string' type or
                          a list of nominal values. 
                      for typecode 1 this is the emptly list []
                      for typecode 2 this is the emptly list [] indicating 
                          use of the default date format or
                          a list containing the date format string.
                      for typecode 3 this is a list of the attribute type
                          information tuples of the sub-attributes.
        m     : a list of lists in which list corresponds to one instance.
                In the case of a sparse data set, each instance 
                list is a list of tuples (0-based attribute index, value).
                For non-sparse data, each instance list is a list of values.
    '''
    parser = arffParser(CTS(arffLexer(AIS(fstream))))
    parser.file()
    if parser.anyErrors:
        return None
    return (parser.rname, parser.sparse, parser.alist, parser.m)

def arffwrite(f, alist, m, name='Unknown', sparse=False, comment=None):
    '''write data in ARFF format.

    Each element in the list m is an instance. When writing relational
    attributes, that attribute must be a list of the relational attribute
    values. arffwrite() will try to be conservative with quoting strings.

    Input:
       f    : output stream
       alist: a list of attribute type information tuples 
                (name, typecode, rest) where
                name: is a string containing the attribute name.
                typecode: an integer indicating the type of the attribute:
                    1 - number, 
                    0 - string and nominal type
                    2 - date,
                    3 - relational.
                rest: for typecode 0 this is either the empty list [] 
                          indicating 'string' type or
                          a list of nominal values.
                      for typecode 1 this is the emptly list []
                      for typecode 2 this is the emptly list [] indicating 
                          use of the default date format or
                          a list containing the date format string.
                      for typecode 3 this is a list of the attribute type
                          information tuples of the sub-attributes.
        m   : a list of lists in which list corresponds to one instance.
                In the case of a sparse data set, each instance 
                list is a list of tuples (0-based attribute index, value).
                For non-sparse data, each instance list is a list of values.
        name: a string containing the name of the relation.
        sparse: a Boolean indicating if sparse data should be written.
        comment: a string that is written to the stream before anything else.
    '''
    arffheader(f, alist, name, comment)
    f.write('@data\n')
    for row in m:
        f.write(grow(row,alist,sparse) + '\n')

def grow(row,alist,sparse):
    if sparse:
        return "{" + ','.join(sformat(row, alist, sparse)) + "}"
    return ','.join(sformat(row, alist, sparse))

def arffalist(names, isnumeric):
    '''create an alist from a list of names and a list of type indicators.

    arffalist will create an alist to be used in arffwrite. 

    Input:
       names: a list of attribute names.
       isnumeric: a list of elements v for which int(v) should yield
                  1 if the corresponding attribute is numeric, and 
                  0 if not.
    Returns: the alist.
    '''
    return [(n, int(t), []) for n,t in zip(names, isnumeric)]

def arffheader(f, alist,name='Unknown', comment=None):
    if comment:
        if comment[0] != '%':
            comment = '% ' + comment
        f.write(comment + '\n')
    f.write('@relation ' + name + '\n')
    for a in alist:
        f.write(aformat(a) + '\n')

def sformat(valist, alist, sparse=False, sep=','):
    vlist = unsparse(valist, alist)
    s = []
    for i,(v,a) in enumerate(zip(vlist, alist)):
        if sparse and (v == 0 or v == ''):
            continue
        (name, typc, rest) = a
        item = None
        if typc == 1: # number
            item = str(v)
        elif typc == 0 or typc == 2: # categorical/string or date
            item = tos(v)
        else: # relational, assumes v is a list of values
            item = ('"' + sep.join(sformat(v, rest, sep=sep)) + '"')
        if sparse:
            s.append(str(i) + " " + item)
        else:
            s.append(item)
    return s

import sys    
def unsparse(vlist, alist):
    try:
        if not isinstance(vlist[0], tuple):
            return vlist
    except: # is empty
        return vlist

    out = []
    for n,t,r in alist:
        if t == 1:
            out.append(0)
        else:
            out.append('')
    for i, v in vlist:
        out[i] = v
    return out
        

#typecode: 1 -- number, 0 - string, 2 - date
def tos(v, qc="'"):
    '''convert to string and quote string if needed'''
    # test is string compatible type
    try:
        v + 'ert'
    except:
        return str(v)
    if len(re.split('[ \t,{}\r\\/\=\>\<]', v)) > 1:
        return qc + v + qc
    #if re.match('[-+]?[0-9]?[.]?[0-9]+([eE][+=]?[0-9]+)?$', v):
    #    return qc + v + qc
    if v == '':
        return qc + v + qc
    return v
    
def aname(at):
    return '@attribute ' + tos(at[0]) + ' '

def astring(at):
    if at[2]:
        return aname(at) + '{' + ','.join(tos(n) for n in at[2]) + '}'
    return aname(at) + 'string'

def adate(at):
    if at[2]:
        return aname(at) + 'date ' + tos(at[2][0])
    return aname(at)

def arelation(at):
    return ((aname(at) + 'relational\n ') +
            '\n '.join(aformat(atr) for atr in at[2]) +
            '\n@end ' + tos(at[0]))

def anum(at):
    return (aname(at) + 'numeric')

afuns = {0:astring, 1:anum, 2:adate, 3:arelation}

def aformat(at):
    assert(at[1] in [0,1,2,3])
    return afuns[at[1]](at)

def vformat(row, sparse=False, sep=','):
    if sparse:
        if type(row[0]) == type(()):
            return ('{' + sep.join(str(i) + ' ' +
                                   tos(v) for i,v in row)+'}')
        else:
            return ('{' + sep.join(str(i) + ' ' + tos(v) for i,v in
                           enumerate(row) if v != 0)+'}')
    return (sep.join(tos(v) for v in row))

if __name__ == "__main__":
    from urllib import urlopen
    from pprint import pprint
    import sys
    f = urlopen(sys.argv[1])
    res = arffread(f)
    if res == None:
        print "Errors encountered, bye."
        sys.exit(1)
    (name, sparse, alist, m) = res
    arffwrite(sys.stdout, alist, m, name, sparse)
    #pprint((name,sparse,alist,m))
    
