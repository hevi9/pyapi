#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2015 Petri Heinilä, LGPL 2.1
import logging
from jinja2 import Environment, PackageLoader
from html import escape as e

__all__ = (
    "make_page"
)


log = logging.getLogger(__name__)
D = log.debug
I = log.info
E = log.error
jenv = Environment(loader=PackageLoader(__package__, "."))


class WriteBuf:

    def __init__(self):
        self._buf = list()

    def write(self, text):
        self._buf.append(text)
        return len(text)

    def value(self):
        return "".join(self._buf)

    def value_nl(self):
        return "\n".join(self._buf)


def make_node(node, write_func):

    for snode in node.subs:
        D(type(snode.object))


def make_module_section(module_node, write_func):
    w = write_func

    w("<h1>%s</h1>" % module_node.name)
    w("<ol>")
    nodes = list(module_node.subs)
    nodes.sort(key=lambda node: node.name)
    for node in nodes:
        w("<li>")
        w("%s %s" % (e(node.name), e(str(type(node.object)))))
        w("</li>")
    w("</ol>")


def make_page(root, write_func):

    module_nodes = list()
    wbuf = WriteBuf()

    # find modules from node trees
#     def find_module(tnode):
#         if tnode.is_module:
#             module_nodes.append(tnode)
#             for snode in tnode.subs:
#                 find_module(snode)
#     for node in nodes:
#         find_module(node)
#     module_nodes.sort(key=lambda node: node.name)
#     for module_node in module_nodes:
#         make_module_section(module_node, wbuf.write)
    # make context
    ctx = {
        "title": "pyapi",
        "root": root
    }

    tmpl = jenv.get_template("tmpl/page.html", globals=ctx)

    # write
    write_func(tmpl.render())
