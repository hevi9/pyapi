#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inspect import getmembers, ismodule
import logging
log = logging.getLogger(__name__)
D = log.debug


class Node:

    def __init__(self, obj, *, up=None, name=None):
        """ Node handling python object. """
        self._obj = obj
        self._up = up
        if name:
            self._name = name
        else:
            if hasattr(obj, "__name__"):
                self._name = obj.__name__
            else:
                self._name = None
                if not isinstance(self, Root):
                    log.warn("%r has no name", self)
        self._attrs = set()
        if up and self not in up.attrs:
            up.attrs.add(self)
        D("new %r", self)

    @property
    def name(self):
        """ Object name as str. """
        return self._name

    @property
    def path(self):
        """ Object name as str. """
        return ((self._up.path + "." if self._up and self._up._name else "") + self._name) if \
            self._name else None

    @property
    def attrs(self):
        """ Node object attribute nodes as set. """
        return self._attrs

    def __repr__(self):
        return "%s(%r as %r)" % (self.__class__.__name__, self.name, type(self))


class Module(Node):

    def __init__(self, obj, *, up=None, name=None):
        super().__init__(obj, up=up, name=name)
        for attr_name, attr in getmembers(obj):
            if ismodule(attr):  # do not traverse on used modules, recursion
                continue
            node = extracts.build_node(attr, up=self, name=attr_name)
            if node:
                self.attrs.add(node)


class Class(Node):

    def __init__(self, obj, *, up=None, name=None):
        super().__init__(obj, up=up, name=name)
        for attr_name, attr in getmembers(obj):
            node = extracts.build_node(attr, up=self, name=attr_name)
            if node:
                self.attrs.add(node)


class Function(Node):

    def __init__(self, obj, *, up=None, name=None):
        super().__init__(obj, up=up, name=name)


class Data(Node):

    def __init__(self, obj, *, up=None, name=None):
        super().__init__(obj, up=up, name=name)


class Root(Node):
    """ Root placeholder node to contain specified packages and modules. """

    def __init__(self, obj=None, *, up=None, name=None):
        super().__init__(obj, up=up, name=name)


# have to be last due mutual dependencies
from . import extracts  # noqa


# Copyright (C) 2015 Petri Heinilä, LGPL 2.1
