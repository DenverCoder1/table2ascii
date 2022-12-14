# /usr/bin/env python
import os
import re

from setuptools import setup


def version():
    version = ""
    with open("table2ascii/__init__.py") as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if not version:
        raise RuntimeError("version is not set")
    return version.group(1)


def long_description():
    # check if README.md exists
    if not os.path.exists("README.md"):
        return ""
    with open("README.md", "r") as fh:
        return fh.read()


def requirements():
    # check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        return []
    with open("requirements.txt") as f:
        return f.read().splitlines()


extras_require = {
    "docs": [
        "enum-tools",
        "sphinx",
        "sphinx-autobuild",
        "sphinx-toolbox",
        "sphinxcontrib_trio",
        "sphinxext-opengraph",
        "sphinx-book-theme==0.3.3",
    ],
    "dev": [
        "mypy>=0.982,<1",
        "pre-commit>=2.0.0,<3",
        "pyright>=1.0.0,<2",
        "pytest>=6.0.0,<8",
        "slotscheck>=0.1.0,<1",
        "taskipy>=1.0.0,<2",
        "tox>=3.0.0,<5",
    ],
}

setup(
    name="table2ascii",
    version=version(),
    author="Jonah Lawrence",
    author_email="jonah@freshidea.com",
    description="Convert 2D Python lists into Unicode/Ascii tables",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/DenverCoder1/table2ascii",
    packages=["table2ascii"],
    install_requires=requirements(),
    extras_require=extras_require,
    setup_requires=[],
    tests_require=[
        "pytest>=6.2,<8",
    ],
)
