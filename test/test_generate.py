#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" pynamedoc.extractor tests """

import logging
import pyapi.generate as sut
import unittest
from hevi_lib.tagtree import Forest, Entry
log = logging.getLogger(__name__)
D = log.debug


def make_forest():
    f = Forest()
    e = Entry(f, "module1", None)
    e.tags.add("module")
    e = Entry(f, "module2", None)
    e.tags.add("module")
    e = Entry(f, "module3", None)
    e.tags.add("module")
    return f


class control:
    out = "/home/hevi/public_html/pyapi-test"
    sources = None
    debug = False


class test_01(unittest.TestCase):

    def test_01(self):
        forest = make_forest()
        sut.generate(forest, control)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
