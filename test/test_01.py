#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Petri Heinilä, LGPL 2.1

import logging  # http://docs.python.org/py3k/library/logging.html
log = logging.getLogger(__name__)
D = log.debug
logging.basicConfig(level=logging.DEBUG)
import pytest

import sys
sys.path.append("..")

from pyapi.main import get_pobj_module


def test_01():
    """ Testing 01 """
    get_pobj_module("pyapi.main")
    assert 0

if __name__ == "__main__":
    pytest.main("-s")
