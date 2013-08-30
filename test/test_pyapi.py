#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" pynamedoc.extractor tests """

import logging
log = logging.getLogger(__name__)
D = log.debug
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

class test_pyapi(unittest.TestCase):

  def test_01(self):
    """ extract modules into forest """
    forest = Forest()
    for r,p in sut.filter_files(sut.find_files(j(root,"package"))):
      #D("{} {}".format(r,p))
      sut.extract_module_file(r, p, forest)
    #dump(forest)
      
if __name__ == "__main__": 
  logging.basicConfig(level=logging.DEBUG)
  unittest.main()
  
  