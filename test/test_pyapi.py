#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" pynamedoc.extractor tests """

import logging
import pyapi
import os
import unittest
import sys

log = logging.getLogger(__name__)
D = log.debug
j = os.path.join


root = j(os.getcwd(), "testforest")
if not os.path.isdir(root):
    root = os.path.normpath(j(os.getcwd(), "..", "testforest"))
    if not os.path.isdir(root):
        sys.exit(1)


class control:
    out = "/home/hevi/public_html/pyapi_test"
    sources = [j(root, "package")]
    debug = True


class test_pyapi(unittest.TestCase):

    def test_01(self):
        """ extract modules into forest """
        pyapi.produce(control)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
