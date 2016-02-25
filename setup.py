#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Petri Heinilä, LGPL 2.1

from setuptools import setup

setup(
    name="pyapi",
    packages=["pyapi"],
    version="0.0.3",
    entry_points={
        "console_scripts": [
            "pyapi=pyapi.main:main"
        ]
    },
    install_requires=[
        "jinja2",
        "hevi-lib>=dev",  # have to have version for dependency_links
        "mkwww>=dev"  # have to have version for dependency_links
    ],
    dependency_links=[
        'https://github.com/hevi9/hevi-lib/tarball/master#egg=hevi-lib-dev',
        'https://github.com/hevi9/mkwww/tarball/master#egg=mkwww-dev'
    ],

)
