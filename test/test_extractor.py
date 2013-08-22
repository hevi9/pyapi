#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" pynamedoc.extractor tests """

import logging
log = logging.getLogger(__name__)
D = log.debug
logging.basicConfig(level=logging.DEBUG)
import pynamedoc.extractor as sut
from hevi_util.processes import cd
import os
j = os.path.join

root = j(os.getcwd(),"testforest")

def test_01():
  """ file found """
  with cd("testforest"):
    assert (root,"justamodule.py") in [i for i in sut.find_files("justamodule.py")]

def test_02():
  """ package tree found """
  files = [i for i in sut.find_files(j(root,"package"))]
  assert (root,"package") in files
  assert (root,"package/module.py") in files
  assert (root,"package/subpackage") in files
  assert (root,"package/subpackage/module.py") in files

def test_03():
  """ package tree found no __init__ """
  files = [i for i in sut.find_files(j(root,"packagenoinit"))]
  assert (root,"packagenoinit") in files
  assert (root,"packagenoinit/module.py") in files
  assert (root,"packagenoinit/subpackage") in files
  assert (root,"packagenoinit/subpackage/module.py") in files

def test_04():
  """ filter non-python files """
  #files = [i for i in sut.find_files(j(root,"package"))]
  files = [i for i in sut.filter_files(sut.find_files(j(root,"package")))]
  #D(files)

def test_05():
  """  """
  for r,path in sut.filter_files(sut.find_files(j(root,"package"))):
    D(j(r,path))
  
  
  
if __name__ == "__main__": test_02()
  
  