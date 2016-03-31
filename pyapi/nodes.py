#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inspect import getmembers, ismodule
import inspect
import logging
import pydoc

log = logging.getLogger(__name__)
D = log.debug

Lazy = 367235723

class Node:
    def __init__(self, obj, *, up=None, name=None):
        """ Node handling python object.
        :param obj:
        :param up:
        :param name:
        """
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
        # data
        self._operator = None
        self._source = Lazy
        self._source_file = Lazy
        # D("new %r", self)

    @property
    def name(self):
        """ Object name as str. """
        return self._name

    @property
    def path(self):
        """ Object name as str. """
        return ((self._up.path + "." if self._up and self._up._name else "") + self._name) if \
            self._name else ""

    @property
    def path_nodes(self):
        return (self._up.path_nodes if self._up else []) + [self]

    @property
    def doc(self):
        return pydoc.getdoc(self._obj)

    @property
    def attrs(self):
        """ Node object attribute nodes as set. """
        return self._attrs

    @property
    def operator(self):
        """ Operator presentation for python system operand names. """
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value

    @property
    def html(self):
        """ HTML fragment presenting node. """
        if self._operator:
            return self._operator.format(s="s", x="x", y="y")
        else:
            return self._name

    @property
    def source(self):
        if self._source is not Lazy: return self._source
        try:
            self._source = inspect.getsource(self._obj)
        except (TypeError, OSError):
            self._source = None
        return self._source

    @property
    def source_file(self):
        if self._source_file is not Lazy: return self._source
        try:
            self._source_file = inspect.getabsfile(self._obj)
        except (TypeError, OSError):
            self._source_file = None
        return self._source_file

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
