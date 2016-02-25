from setuptools import setup

setup(
    name="pyapi",
    packages=["pyapi"],
    version="0.0.4",
    entry_points={
        "console_scripts": [
            "pyapi=pyapi.main:main"
        ]
    },
    install_requires=[
        "jinja2"
    ],
)

# Copyright (C) 2014 Petri Heinilä, LGPL 2.1
