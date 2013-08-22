#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" Document object model. """

import logging
log = logging.getLogger(__name__)
D = log.debug
import collections

##############################################################################
class Tag:
  
  def __init__(self,tname):
    self.tname = tname
    self.names = set()
    
  def __str__(self):
    return self.tname  

"""
self.tag("module")
"""

##############################################################################
class Name(collections.UserDict):
  
  def __init__(self,name,parent):
    # id
    self.name = name   # as str
    # structure
    self.parent = parent # as Name
    self.data = dict() # as dict of (str: Name)
    self.tags = set()  # as set of Tag
    # information    
    self.doc = None    # as str
    
  @property 
  def forest(self):
    if self.parent is None:
      return self
    else:
      return self.forest()
    
  def tag(self,tname):
    return self.forest.tag(tname)

##############################################################################
class Forest(Name):
  
  def __init__(self):
    super().__init__(None,None)
    self.tags = dict() # all tags

  def tag(self,tname):
    return self.tags.setdefault(tname.Tag(tname))

  