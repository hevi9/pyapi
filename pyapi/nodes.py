#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2015 Petri Heinilä, LGPL 2.1


class Node:

    def __init__(self):
        self.name = None
        self.object = None
        self.subs = set()
        self.is_module = False

    def __repr__(self):
        return "<%s %s>" % (self.name, type(self.object))
