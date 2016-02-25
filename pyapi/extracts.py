#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
from pyapi.nodes import Node
import logging
from pyapi.rules import rule_name
import os
import sys
import importlib as il
import importlib.machinery as ilm
# from types import *
from types import ModuleType
from .nodes import Module, Class, Function, Node

log = logging.getLogger(__name__)
D = log.debug
j = os.path.join


def is_composite(obj):
    return inspect.ismodule(obj) or inspect.isclass(obj)


def is_name_ignore(name):
    if is_system_name(name):
        return True
    return False


def is_system_name(name):
    return (name in control.sys_module_names or
            name in control.sys_class_names)


def extract_thing(entry):
    D("extract_thing({})".format(entry.path))
#     assert entry.obj is not None
#     if is_composite(entry.obj):
#         for name, obj in inspect.getmembers(entry.obj):
#             if is_name_ignore(name):
#                 continue
#             if inspect.isclass(obj):
#                 subentry = Class(entry, name, obj)
#             elif inspect.isroutine(obj):
#                 subentry = Function(entry, name, obj)
#             else:
#                 subentry = Entry(entry, name, obj)
#             extract_thing(subentry)


skips = [
    "__call__",
    "__class__",
    "__delattr__",
    "__dir__",
    "__add__",
    "__contains__"
]


def build_node(obj, name=None, parent=None):
    """ Build node and it's member node tree if any. """
    D("build_node(%r,%r,%r)", obj, name, parent)

    for attr_name, attr in inspect.getmembers(obj):
        D("  %r @%r", attr_name, attr)
#         if attr_name in skips:
#             continue
#         build_node(attr, attr_name, obj)

#     tnode = Node(module_obj)
#     tnode.name = module_obj.__name__
#     tnode.object = module_obj
#     tnode.is_module = True
#
#     for rname, obj in inspect.getmembers(module_obj):
#
#         if inspect.ismodule(obj):
#             continue
#
#         name = rule_name(rname)
#         if not name:
#             continue
#
#         node = Node(obj)
#         node.name = name
#         tnode.subs.add(node)
#         node.parent = tnode
#
#     return tnode


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

#     # process module object
#     node = process_module_obj(module_obj)
#     if tnode:
#         tnode.subs.add(node)
#         node.parent = tnode
#
#     return node


class control:
    sys_module_names = (
        "__builtins__",
        "__cached__",
        "__doc__",
        "__file__",
        "__initializing__",
        "__loader__",
        "__name__",
        "__package__",
        "__path__"
    )
    sys_class_names = (
        "__class__",
        "__dict__",
        "__dir__",
        "__doc__",
        "__reduce__",
        "__le__",
        "__gt__",
        "__ne__",
        "__new__",
        "__subclasshook__",
        "__getattribute__",
        "__module__",
        "__repr__",
        "__ge__",
        "__lt__",
        "__eq__",
        "__format__",
        "__weakref__",
        "__setattr__",
        "__str__",
        "__delattr__",
        "__sizeof__",
        "__hash__",
        "__reduce_ex__"

    )


# Copyright (C) 2015 Petri Heinilä, LGPL 2.1
