# /usr/bin/env python
import re

from setuptools import setup


def get_name():
    name = ""
    with open("pyproject.toml") as f:
        name = re.search(r'^name = ["\']([^"\']*)["\']', f.read(), re.M)
    if not name:
        raise RuntimeError("name is not set")
    return name.group(1)


def get_version():
    version = ""
    with open("pyproject.toml") as f:
        version = re.search(r'^version = ["\']([^"\']*)["\']', f.read(), re.M)
    if not version:
        raise RuntimeError("version is not set")
    return version.group(1)


def get_dependencies():
    with open("pyproject.toml") as f:
        dependency_match = re.search(r"^dependencies = \[([\s\S]*?)\]", f.read(), re.M)
    if not dependency_match or not dependency_match.group(1):
        return []
    return [
        dependency.strip().strip(",").strip('"')
        for dependency in dependency_match.group(1).split("\n")
        if dependency
    ]


try:
    # check if pyproject.toml can be used to install dependencies and set the version
    setup(
        packages=[get_name()],
        package_data={get_name(): ["py.typed"]},
    )
except Exception:
    # fallback for old versions of pip/setuptools
    setup(
        name=get_name(),
        packages=[get_name()],
        package_data={get_name(): ["py.typed"]},
        version=get_version(),
        install_requires=get_dependencies(),
    )
