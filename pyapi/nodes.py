#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, obj, name=None):
        """ Node handling python object. """

        #
        self.obj = obj
        self._name = name if name else obj.__name__
        self._attrs = set()
        self.type = type(obj)

        #
        self.is_module = False

    def name(self):
        """ Object name as str. """
        return self._name

    def attrs(self):
        """ Node object attribute nodes as set. """
        return self._attrs

    def __repr__(self):
        return "%s(%r as %r)" % (self.__class__.__name__, self.name, self.type)


class Module(Node):

    def __init__(self, obj, name=None):
        super().__init__(obj, name)


class Class(Node):

    def __init__(self, obj, name=None):
        super().__init__(obj, name)


class Function(Node):

    def __init__(self, obj, name=None):
        super().__init__(obj, name)

# Copyright (C) 2015 Petri Heinilä, LGPL 2.1
