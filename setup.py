# /usr/bin/env python
import re

from setuptools import setup


def version():
    version = ""
    with open("table2ascii/__init__.py") as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if not version:
        raise RuntimeError("version is not set")
    return version.group(1)


setup(name="table2ascii", version=version())
