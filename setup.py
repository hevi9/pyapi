#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1

from setuptools import setup, find_packages
from hevi_util.setups import package_data, console_scripts
from INFO import *

setup(
  install_requires=['distribute'],
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