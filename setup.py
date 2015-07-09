#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Petri Heinilä, LGPL 2.1

from setuptools import setup

info = dict()
with open("INFO") as f:
    exec(f.read(), info)

setup(
    name="pyapi",
    packages=("pyapi"),
    entry_points={
        "console_scripts": [
            "pyapi=pyapi.main:main"
        ]
    },
    install_requires=[
        "hevi-lib"
    ],
    dependency_links=[
    ]
)
