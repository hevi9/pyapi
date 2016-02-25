""" pyapi command line interface. """

import sys
import argparse
import logging
from .htmls import make_page
from pyapi.extracts import get_pobj_module
import os

log = logging.getLogger(__name__)
D = log.debug
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
    else:
        logging.getLogger().setLevel(logging.INFO)

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


# Copyright (C) 2014 Petri Heinilä, LGPL 2.1
