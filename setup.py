# /usr/bin/env python
import re

from setuptools import setup


def version():
    version = ""
    with open("pyproject.toml") as f:
        version = re.search(r'^version = ["\']([^"\']*)["\']', f.read(), re.M)
    if not version:
        raise RuntimeError("version is not set")
    return version.group(1)


setup(
    name="table2ascii",
    version=version(),
    packages=["table2ascii"],
    package_data={"table2ascii": ["py.typed"]},
)
