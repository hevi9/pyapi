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
from hevi_util.files import mkdir
from pkgutil import get_data
import jinja2
jenv = jinja2.Environment(loader = jinja2.PackageLoader("pyapi","tmpl"))
from hevi_util.tagtree import dump

##############################################################################
class Resource:

  def __init__(self, manual):
    self.manual = manual
    self.manual.resources.append(self)
  
  @property
  def url(self):
    pass
  
  @property
  def path(self):
    pass
  
  @property
  def apath(self):
    return os.path.abspath(j(self.manual.control.out,self.path))  
  
  def process(self):
    pass
  
  def make(self):
    pass

##############################################################################
class Page(Resource):

  def __init__(self, manual):
    super().__init__(manual)

  @property  
  def title(self):
    pass

##############################################################################
class Index(Page):
  
  tmpl = jenv.get_template("index.html") 

  def __init__(self, manual):
    super().__init__(manual)

  @property
  def path(self):
    return "index.html"
  
  @property
  def ctx(self):
    return {
      "forest": self.manual.forest
    }

  def make(self):
    log.info("making {}".format(self.apath))
    with open(self.apath,"w") as fo:
      fo.write(self.tmpl.render(self.ctx))
    

##############################################################################
class Module(Page):

  tmpl = jenv.get_template("module.html") 

  def __init__(self, manual,entry):
    super().__init__(manual)
    self.entry = entry

##############################################################################
class Manual(Resource):
  
  def __init__(self, forest, control):
    self.resources = list()
    self.modules = list()
    self.control = control
    self.forest = forest
    
  def process(self):
    for r in self.resources:
      r.process()
      
  def make(self):
    mkdir(self.control.out)
    for r in self.resources:
      r.make()    

##############################################################################
def generate(forest,control):
  log.info("Generating to {}".format(control.out))
  dump(forest)
  manual = Manual(forest, control)
  Index(manual)
  for entry in forest.index.values():
    if "module" in entry.tags:
      Module(manual,entry)
  manual.process()
  manual.make()
  log.info("done")



