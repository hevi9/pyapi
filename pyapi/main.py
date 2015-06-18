#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Petri Heinilä, LGPL 2.1

import sys       # http://docs.python.org/py3k/library/sys.html
import argparse  # http://docs.python.org/py3k/library/argparse.html
import logging   # http://docs.python.org/py3k/library/logging.html
from pyapi.htmls import make_page
from pyapi.extract import get_pobj_module
log = logging.getLogger(__name__)
D = log.debug
I = log.info
E = log.error
import os
j = os.path.join


ARGS = argparse.ArgumentParser()
ARGS.add_argument("module", nargs="+",
                  help="Modules to create API description")
ARGS.add_argument("--debug", "-d", action="store_true",
                  help="set debugging on")
ARGS.add_argument("--output", "-o", default=None, metavar="FILE",
                  help="output html file")


def main():
    args = ARGS.parse_args()
    logging.basicConfig()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    nodes = set()

    for module in args.module:
        nodes.add(get_pobj_module(module))

    if args.output:
        fo = open(args.output, "w")
        write_func = fo.write
    else:
        write_func = sys.stdout.write

    make_page(nodes, write_func)

    if args.output:
        fo.close()

if __name__ == "__main__":
    main()
