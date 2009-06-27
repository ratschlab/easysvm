# -*-Python-*-
################################################################################
#
# File:         __init__.py
# RCS:          $Header: $
# Description:  __init__.py file for arff package
# Author:       Staal Vinterbo
# Created:      Thu Jan 10 12:24:23 2008
# Modified:     Thu Jan 10 12:24:53 2008 (Staal Vinterbo) staal@peep
# Language:     Python
# Package:      arff
# Status:       Experimental
#
# __init__.py is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# __init__.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with __init__.py; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# (c) Copyright 2008, Staal Vinterbo, all rights reserved.
#
################################################################################
"""arff: a package for reading and writing ARFF format files."""

from arff import *
__all__ = arff.__all__

from .docstring import dstring
__doc__ = dstring

