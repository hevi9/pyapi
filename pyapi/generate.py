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

##############################################################################
class Resource:
  pass

##############################################################################
class Page(Resource):
  pass

##############################################################################


def generate(forest,control):
  modules = list()
  for entry in forest.index.values():
    modules.append(entry)
  D(modules)
  
