#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2015 Petri Heinilä, LGPL 2.1

import inspect
from pyapi.nodes import Node
import logging
from pyapi.rules import rule_name
import os
log = logging.getLogger(__name__)
D = log.debug
j = os.path.join


def process_module_obj(module_obj):
    tnode = Node()
    tnode.name = module_obj.__name__
    tnode.object = module_obj
    tnode.is_module = True

    for rname, object in inspect.getmembers(module_obj):
        # D(name)

        if inspect.ismodule(object):
            continue

        name = rule_name(rname)
        if not name:
            continue

        node = Node()
        node.name = name
        node.object = object
        tnode.subs.add(node)
        node.parent = tnode

    return tnode


def get_pobj_module(module, tnode=None):
    """ Get python object from name. """

    # import and locate real module
    D("loading %s", module)
    module_obj = __import__(module)
    parts = module.split(".")
    parts.reverse()
    parts.pop()
    while parts:
        module_obj = getattr(module_obj, parts.pop())
    # D("=> %s", module_obj)

    # process module object
    node = process_module_obj(module_obj)
    if tnode:
        tnode.subs.add(node)
        node.parent = tnode

    # recurse to sub modules and packages
    if hasattr(module_obj, "__path__"):
        paths = getattr(module_obj, "__path__")
        for filename in os.listdir(paths[0]):
            name, ext = os.path.splitext(filename)
            if name == "__init__":
                continue
            if ext == ".py":
                get_pobj_module(".".join((module, name)), node)
            apath = j(paths[0], filename)
            if os.path.exists(j(apath, "__init__.py")):
                get_pobj_module(".".join((module, name)), node)

    return node
