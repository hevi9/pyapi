#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" Extract names from python module. """

import logging
log = logging.getLogger(__name__)
D = log.debug
import os
j = os.path.join
from hevi_util.module import module_name, import_file
import importlib as imp

def find_files(path, root = None):
  """ """
  ## determine root
  if root is None:
    if os.path.isabs(path):
      root = os.path.dirname(path)
      path = os.path.basename(path)
    else:
      root = os.getcwd()
  ##
  f = j(root,path)
  yield root,path
  if os.path.isdir(f):
    for name in os.listdir(f):
      for i in find_files(j(path,name),root):
        yield i

def filter_files(iter):
  suffixes = imp.machinery.SOURCE_SUFFIXES + imp.machinery.EXTENSION_SUFFIXES
  for root, path in iter:
    if os.path.isdir(j(root,path)):
      yield root,path
    if os.path.basename(path) == "__init__.py": continue
    if not os.path.splitext(path)[1] in suffixes: continue
    yield root,path
    
def extract_module_file(root,path,forest):
  

  
##############################################################################
__doc__ += """
"""