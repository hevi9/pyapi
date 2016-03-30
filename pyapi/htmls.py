from jinja2 import Environment, PackageLoader
from . import log
import pyapi

__all__ = (
    "make_page"
)

jenv = Environment(
    loader=PackageLoader(__package__, "."),
    trim_blocks=True,
    lstrip_blocks=True
)


def make_page(root, fo):
    """ """
    log.info("making page to %r", fo.name)
    ctx = {
        "title": "pyapi",
        "root": root,
        "pyapi": pyapi
    }
    tmpl = jenv.get_template("tmpl/page.html", globals=ctx)
    fo.write(tmpl.render())

# Copyright (C) 2015 Petri Heinilä, LGPL 2.1
