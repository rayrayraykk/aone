# -*- coding: utf-8 -*-
""" Setup for installation."""
from __future__ import absolute_import, division, print_function

import setuptools

NAME = "aone"
VERSION = "0.0.1"
URL = "xxx"

minimal_requires = ["pre-commit"]

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    author="xxx",
    author_email="xxx@xxx.com",
    description="xxx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    download_url=f"{URL}/archive/{VERSION}.tar.gz",
    keywords=["xxx"],
    packages=[
        package
        for package in setuptools.find_packages()
        if package.startswith(NAME)
    ],
    install_requires=minimal_requires,
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
