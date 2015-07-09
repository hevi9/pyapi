#!/usr/bin/env python3
# Copyright (C) 2014 Petri Heinilä, LGPL 2.1

from pyapi.main import get_pobj_module


def test_01():
    """ Testing 01 """
    get_pobj_module("pyapi.main")
    assert 0
