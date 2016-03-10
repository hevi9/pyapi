""" pyapi command line interface. """

import sys
import argparse
import logging
from .htmls import make_page
from . import extracts
from .nodes import Root
from . import NAME
import os
from tempfile import gettempdir
from hashlib import sha1
import webbrowser

log = logging.getLogger(__name__)
D = log.debug
j = os.path.join


ARGS = argparse.ArgumentParser()
ARGS.add_argument("modules", nargs="+", metavar="module",
                  help="Modules to create API description")
ARGS.add_argument("--debug", "-d", action="store_true",
                  help="set debugging on")
ARGS.add_argument("--page", "-p", default=None, metavar="FILE",
                  help="output to single page html file")
ARGS.add_argument("--browser", "-b", action="store_true",
                  help="open in browser with temporary file")


def make_tmp_path(modules):
    hsh = sha1()
    for i in sorted(modules):
        hsh.update(i.encode())
    return j(gettempdir(), NAME + "-" + hsh.hexdigest() + ".html")


def setup_logging(args):
    logging.basicConfig()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)


def main(*args):
    # init
    args = ARGS.parse_args(args if args else None)
    if not args.page and not args.browser:
        ARGS.error("--page FILE or --browser required")
    setup_logging(args)

    # build nodes from given modules
    root = Root()
    for module_path in args.modules:
        root.attrs.add(extracts.load_module(module_path, root))

    # set target path
    path = args.page
    path = make_tmp_path(args.modules) if not path else path
    assert path, "should not happen"

    # generate
    with open(path, "w") as fo:
        make_page(root, fo)

    # open browser if requested
    if args.browser:
        path = os.path.abspath(path)
        webbrowser.open("file://%s" % path)


# Copyright (C) 2014 Petri Heinilä, LGPL 2.1
