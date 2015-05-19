#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Petri Heinilä, LGPL 2.1

import sys       # http://docs.python.org/py3k/library/sys.html
import argparse  # http://docs.python.org/py3k/library/argparse.html
import logging   # http://docs.python.org/py3k/library/logging.html
import inspect
log = logging.getLogger(__name__)
D = log.debug
I = log.info
E = log.error
import os
j = os.path.join


class Node:

    def __init__(self):
        self.name = None
        self.object = None
        self.subs = set()


def process_module_obj(module_obj):
    tnode = Node()
    tnode.name = module_obj.__name__
    tnode.object = module_obj

    for name, object in inspect.getmembers(module_obj):
        D(name)
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
    D("=> %s", module_obj)

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


ARGS = argparse.ArgumentParser()
ARGS.add_argument("module", nargs="+",
                  help="Modules to create API description")
ARGS.add_argument("-d", "--debug", action="store_true",
                  help="set debugging on")


def main():
    args = ARGS.parse_args()
    logging.basicConfig()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    for module in args.module:
        get_pobj_module(module)


if __name__ == "__main__":
    main()
