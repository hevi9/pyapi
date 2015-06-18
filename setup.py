#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Petri Heinilä, LGPL 2.1

from setuptools import setup, find_packages

info = dict()
with open("INFO") as f:
    exec(f.read(), info)


setup(
    name=info["name"],
    version=info["version"],
    description=info["title"],
    author=info["author"],
    url=info["url"],
    license=info["license"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyapi=pyapi.main:main"
        ]
    },
    install_requires=[
    ],
    dependency_links=[
    ]

)
#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1

from setuptools import setup, find_packages
from hevi_util.setups import package_data, console_scripts
from pyapi.INFO import *

setup(
  install_requires=['setuptools >= 0.9'],
  name=name,
  version=version,
  description='Name based python document generator',
  author=author,
  url=url,
  packages = find_packages(),
  package_data = {name: package_data(name) },
  entry_points={
    'console_scripts': console_scripts(name)
  },
  license = license
)