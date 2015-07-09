#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" Python things. """


import logging
from hevi_lib.tagtree import Entry
log = logging.getLogger(__name__)
D = log.debug

__all__ = list()


class Mixin:

    @property
    def is_composite(self):
        return False


class Module(Entry, Mixin):

    def __init__(self, up, name, obj):
        super().__init__(up, name, obj)
        self.tags.add("module")

    @property
    def is_composite(self):
        return True
__all__.append("Module")


class Class(Entry, Mixin):

    def __init__(self, up, name, obj):
        super().__init__(up, name, obj)
        self.tags.add("class")

    @property
    def is_composite(self):
        return True
__all__.append("Class")


class Function(Entry, Mixin):

    def __init__(self, up, name, obj):
        super().__init__(up, name, obj)
        self.tags.add("function")

__all__.append("Function")
