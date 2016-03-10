import os
import pydoc
import logging
from .rules import get_rules

log = logging.getLogger(__name__)
D = log.debug
j = os.path.join


def build_node(obj, *, up=None, name=None):
    """ Build node and it's member node tree if any. """
    for applies, factory, _ in get_rules():
        if applies(obj, name):
            node = factory(obj, up=up, name=name)
            # if node:
            #    D("%r as %r -> %r", node.name, obj, node)
            return node
    # None applied, ignore ? or generic
    log.warn("no rule for %r as %r in %r", name, obj, up.name)
    return None


def load_module(module_path, up=None):
    """ Get python object from name. """
    obj = pydoc.safeimport(module_path)
    if obj is None:
        raise ImportError("%r not found" % module_path)
    node = build_node(obj, up=up)
    D("%r -> %r", module_path, node)
    return node


# Copyright (C) 2015 Petri Heinilä, LGPL 2.1
