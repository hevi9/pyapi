#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" Document object model. """

import logging
log = logging.getLogger(__name__)
D = log.debug
from pynamedoc.dom import Name

class FactoryMix:
  
  def new_module(self,name,obj):
    name = self.setdefault(name,Name(name,self))
    name.tags.add(self.tag("module"))
    return name