#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" pynamedoc.extractor tests """

import logging
log = logging.getLogger(__name__)
D = log.debug
logging.basicConfig(level=logging.DEBUG)
import pyapi.extractor as sut
from hevi_util.processes import cd
import os
j = os.path.join
import unittest
import sys
from hevi_util.tagtree import Forest, Entry, dump

root = j(os.getcwd(),"testforest")
if not os.path.isdir(root):
  root = os.path.normpath(j(os.getcwd(),"..","testforest"))
  if not os.path.isdir(root):
    sys.exit(1)

class test_extractor(unittest.TestCase):

  def test_01(self):
    """ file found """
    with cd(root):
      assert (root,"justamodule.py") in [i for i in sut.find_files("justamodule.py")]
  
  def test_02(self):
    """ package tree found """
    files = [i for i in sut.find_files(j(root,"package"))]
    assert (root,"package") in files
    assert (root,"package/module.py") in files
    assert (root,"package/subpackage") in files
    assert (root,"package/subpackage/module.py") in files
  
  def test_03(self):
    """ package tree found no __init__ """
    files = [i for i in sut.find_files(j(root,"packagenoinit"))]
    assert (root,"packagenoinit") in files
    assert (root,"packagenoinit/module.py") in files
    assert (root,"packagenoinit/subpackage") in files
    assert (root,"packagenoinit/subpackage/module.py") in files
  
  def test_04(self):
    """ filter non-python files """
    files = [i for i in sut.filter_files(sut.find_files(j(root,"package")))]
    #D(files)
    assert (root,"package/nonpython.txt") not in files
    #assert (root,"package/module.py") not in files

  def test_05(self):
    """ extract modules into forest """
    forest = Forest()
    for r,p in sut.filter_files(sut.find_files(j(root,"package"))):
      #D("{} {}".format(r,p))
      sut.extract_module_file(r, p, forest)
    #dump(forest)
      
if __name__ == "__main__": 
  #test_02()
  unittest.main()
  
  