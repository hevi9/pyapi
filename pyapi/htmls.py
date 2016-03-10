from jinja2 import Environment, PackageLoader
from . import log

__all__ = (
    "make_page"
)

jenv = Environment(loader=PackageLoader(__package__, "."))


def make_page(root, fo):
    """ """
    log.info("making page to %r", fo.name)
    ctx = {
        "title": "pyapi",
        "root": root
    }
    tmpl = jenv.get_template("tmpl/page.html", globals=ctx)
    fo.write(tmpl.render())

# Copyright (C) 2015 Petri Heinilä, LGPL 2.1
