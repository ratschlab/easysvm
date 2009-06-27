# -*-Python-*-
################################################################################
#
# File:         docstring.py
# RCS:          $Header: $
# Description:  Documentation string for the arff package
# Author:       Staal Vinterbo
# Created:      Wed Jan  9 13:39:00 2008
# Modified:     Mon Feb 11 13:21:32 2008 (Staal Vinterbo) staal@ding
# Language:     Python
# Package:      arff
# Status:       Experimental
#
# docstring.py is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# docstring.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with docstring.py; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# (c) Copyright 2008, Staal Vinterbo, all rights reserved.
#
################################################################################
"""generate a document string"""

__all__ = ['dstring']

base = """a package for reading and writing ARFF format files.

Synopsis
========

::

  from arff import arffread, arffwrite
  import sys
  f = open(sys.argv[1])
  (name, sparse, alist, m) = arffread(f)
  arffwrite(sys.stdout, alist, m)

Description
===========

The package arff implements an ARFF format antlr v3 parser/lexer 
specification derived from
http://weka.sourceforge.net/wekadoc/index.php/en:ARFF_%283.5.1%29

There are two parts to *arff*. The first is the Python 
software which implements functions for reading and writing ARFF
format files. The other part is a formal ANTLR (http://www.antlr.org/) 
parser/lexer specification of the ARFF syntax. This specification can be 
used to automatically generate parsers and lexical analyzers for a range 
of language targets. These language targets currently include java, C, C#, 
C++, Objective C, Python, Ruby, Perl, Ada, ActionScript. Indeed
the specification was used to generate the Python code 
for the parser and lexical analyzer.

The *arff* Python package
-------------------------

The *arff* package has two main entry points. They are::

  arffread(fstream)
  arffwrite(f, alist, m, name='Unknown', sparse=False, comment=None)

The parameters of these functions are::

  f, fstream - output, input stream
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
                      a list of strings from which the nominal values
                      are taken.
                  for typecode 1 this is the empty list []
                  for typecode 2 this is the emptily list [] indicating 
                      use of the default date format or
                      a list containing the date format string.
                  for typecode 3 this is a list of the attribute type
                      information tuples of the sub-attributes.
  comment: a string that is printed on the output stream before
           anything else.
  m      : Each element in the list m is an instance. When writing relational
           attributes, that attribute must be a list of the relational attribute
           values. 

``arffwrite`` will try to be conservative with quoting strings.

Note that the reader and writer functions do not do any semantic checking
of the data and its values. 

Error Handling
~~~~~~~~~~~~~~

``arffread`` returns ``None`` in case there was an error. An error
message is printed to the standard error stream.

Example
~~~~~~~

Let the file ``test.arff`` contain the following::

    @relation sparse
    @attribute a1 string
    @attribute a2 string
    @attribute a3 {val1,val2,val3}
    @attribute a4 string
    @attribute a5 relational
     @attribute a51 numeric
     @attribute a52 string
     @attribute a53 date yyyy-MM-ddTHH:mm:ss
     @attribute a54 {'val 0','val 1'}
    @end a5
    @attribute a6 numeric
    @data
    {1 X,3 Y,4 'class A'}
    {2 W,4 'class B'}

The result of

::

    from arff import arffread
    from pprint import pprint

    f = open('test.arff')
    (name, sparse, alist, m) = arffread(f)
    pprint((name,sparse,alist,m))

is (comments are inserted to help understanding)::

    ('sparse',  # name of the relation
     True,      # this is a sparse data set
     # the alist:
     [('a1', 0, []),
      ('a2', 0, []),
      ('a3', 0, ['val1', 'val2', 'val3']),
      ('a4', 0, []),
      ('a5',
       3,       # the typecode for attribute a5
       [('a51', 1, []), # the alist for attribute a5
        ('a52', 0, []),
        ('a53', 2, ['yyyy-MM-ddTHH:mm:ss']),
        ('a54', 0, ['val 0', 'val 1'])]),
      ('a6', 1, [])],
     # the data list of lists m
     [[(1, 'X'), (3, 'Y'), (4, 'class A')], [(2, 'W'), (4, 'class B')]])



The ANTLR specification
-----------------------

The full grammar with semantic actions for Python is contained in the 
file ``arff.g`` distributed with the *arff* package.

The parser grammar essentially is::

  file     : header data;
  header   : '@relation' string adecls;
  adecls   : adecl (adecl)*;
  adecl    : '@attribute' string datatype;
  datatype : 'numeric'|'integer'|'real'|'string'|
             'relational' adecls '@end' string | date | '{' values '}';
  date     : 'date' (string)?;
  data     : '@data' ( (pairs)+ | (values)+ );
  pairs    : '{' pair (',' pair)* '}';
  pair     : INT value;
  values   : value (',' value)*;
  value    : '?' | FLOAT | INT | string;
  keyword  : 'numeric' | 'integer' | 'real' | 'string' | 'relational' | 'date';
  string   : QSTRING | STRING | keyword;



Dependencies
============

* python package antlr3 (http://www.antlr.org/download/Python/)

Availability
============

:License:
    *arff* in general is distributed as free (not as in beer)
    software under the 
    GNU General Public License (http://www.gnu.org/licenses/gpl.txt).
    The ANTLR grammar file ``arff.g``
    is distributed under the Apache licence version 2.0
    (http://www.apache.org/licenses/LICENSE-2.0).

:Download:
    http://www.mit.edu/~sav/arff/dist

:Homepage:
    http://www.mit.edu/~sav/arff

Version
=======

This documentation was generated for *arff* version $version.

Bugs and "Features"
===================

* keywords are not fully case sensitive (keyword, Keyword, and KEYWORD 
  are supported)
* date formats are not checked
* no checking of semantics (e.g., consistency between declared
  data types and actual data types)
* Error reporting is done via return value
* take care when dealing with relational format data. Per specification
  input is a quoted string and is returned as such, while when using 
  ``arffwrite`` the value must be a list of the sub-attribute values. 
  This means that when there are relational attributes, ``arffread`` and
  ``arffwrite`` are not symmetrical.

Must be plenty of others. Please report them to the author/maintainer:
    Staal A. Vinterbo.

"""

from .version import Version
from string import Template
dstring = Template(base).substitute({'version' : Version })


if __name__ == "__main__":
    print dstring

    

