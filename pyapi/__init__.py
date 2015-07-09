#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
""" """

import logging
from hevi_lib.tagtree import Forest, dump
import pyapi.extractor as ext
import sys
import os
import argparse
import pprint
import inspect
import pyapi.generate as gen
log = logging.getLogger(__name__)
D = log.debug


j = os.path.join


class control:
    out = "./build/api"
    sources = None
    debug = False


def cdump(obj):
    print("class control:")
    for name, sobj in inspect.getmembers(obj):
        if name.startswith("_"):
            continue
        print("  ", name, " = ", sobj)

##############################################################################
description = """
Generate python API presentation to static html pages.
""".strip()


def _add_arguments(parser):
    parser.add_argument(
        'sources', metavar="source", type=str, nargs='+',
        help="python source, module or package, file or modulename")
    parser.add_argument(
        "-d", '--debug', action='store_true',
        help="set debugging on")
    parser.add_argument(
        "-o", '--out', type=str, metavar="dir", default=control.out,
        help="html output directory (%(default)s)")


def _apply_arguments(args, control):
    for name, value in inspect.getmembers(args):
        if name.startswith("_"):
            continue
        if hasattr(control, name):
            setattr(control, name, value)


def error(msg):
    log.error(msg)
    sys.exit(1)


def produce(control):
    # extract to forest
    forest = Forest()
    for source in control.sources:
        if not os.path.exists(source):
            error("{} does not exists".format(source))
        D(source)
        for r, p in ext.filter_files(ext.find_files(source)):
            log.info("extracting {}".format(j(r, p)))
            ext.extract_module_file(r, p, forest)
    # generate
    gen.generate(forest, control)


def main_pyapi(args=sys.argv[1:]):
    """
    args is list of program arguments, *not* including program name, argv[0].
    """
    parser = argparse.ArgumentParser(description=description)
    _add_arguments(parser)
    args = parser.parse_args(args)
    _apply_arguments(args, control)
    logging.basicConfig(level=logging.INFO)
    if control.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    cdump(control)
    produce(control)

if __name__ == "__main__":
    main_pyapi()
