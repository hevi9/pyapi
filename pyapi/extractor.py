#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" Extract names from python module. """

import logging
from inspect import ismodule
log = logging.getLogger(__name__)
D = log.debug
import os
j = os.path.join
from hevi_util.module import module_name, import_file
from hevi_util.tagtree import Forest, Entry
import importlib as il
import importlib.machinery as ilm 
import sys
from types import *
import inspect

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
  suffixes = ilm.SOURCE_SUFFIXES + ilm.EXTENSION_SUFFIXES
  for root, path in iter:
    if os.path.isdir(j(root,path)):
      if os.path.basename(path) == "__pycache__": continue
      yield root,path
    if os.path.basename(path) == "__init__.py": continue
    if not os.path.splitext(path)[1] in suffixes: continue
    yield root,path
    
def extract_module_file(root,path,forest):
  D("extract_module_file({})".format(path))
  ## insert root to sys.path
  inserted = False
  if root not in sys.path:
    sys.path.insert(0, root)
    inserted = True
  ## import 
  mname = module_name(path)
  mpath = mname.split(".")
  centry = forest
  for i in range(0,len(mpath)):
    if mpath[i] not in centry:
      mname2 = ".".join(mpath[:i+1])
      mobj = il.import_module(mname2)
      centry = Entry(centry,mpath[i],mobj)
      extract_module_to_entry(centry)
    else:
      centry = centry[mpath[i]]
  ## clean up sys.path
  if inserted: sys.path.remove(root)
  
def extract_module_to_entry(entry):
  assert type(entry.obj) is ModuleType
  D("extract_module_to_entry({})".format(entry.path))
  # extract data
  # create members
  for name,obj in inspect.getmembers(entry.obj):
    if is_name_ignore(name): continue
    subentry = Entry(entry,name,obj)
    extract_thing(subentry)
  # tags
  entry.tags.add("module")
  
def extract_thing(entry):
  D("extract_thing({})".format(entry.path))
  assert entry.obj is not None
  if is_composite(entry.obj):
    for name,obj in inspect.getmembers(entry.obj):
      if is_name_ignore(name): continue
      subentry = Entry(entry,name,obj)
      extract_thing(subentry)

def is_composite(obj):
  return inspect.ismodule(obj) or inspect.isclass(obj)
    
def is_name_ignore(name):
  if is_system_name(name): return True
  return False

def is_system_name(name):
  return name in (
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__initializing__",
    "__loader__",
    "__name__",
    "__package__",
    "__path__"
  )
  
##############################################################################
__doc__ += """
"""