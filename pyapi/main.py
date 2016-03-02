""" pyapi command line interface. """

import sys
import argparse
import logging
from .htmls import make_page
from . import extracts
from .nodes import Root
import os

log = logging.getLogger(__name__)
D = log.debug
j = os.path.join


ARGS = argparse.ArgumentParser()
ARGS.add_argument("modules", nargs="+", metavar="module",
                  help="Modules to create API description")
ARGS.add_argument("--debug", "-d", action="store_true",
                  help="set debugging on")
ARGS.add_argument("--html", default=None, metavar="FILE",
                  help="output html file")


def setup_logging(args):
    logging.basicConfig()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)


def main():
    args = ARGS.parse_args()
    setup_logging(args)

    root = Root()

    for module_path in args.modules:
        root.attrs.add(extracts.load_module(module_path, root))

    if args.html:
        fo = open(args.html, "w")
        write_func = fo.write
    else:
        write_func = sys.stdout.write

    make_page(root, write_func)
    # D(root.attrs)

    if args.html:
        fo.close()


# Copyright (C) 2014 Petri Heinilä, LGPL 2.1
