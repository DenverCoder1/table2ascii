# /usr/bin/env python
import os
import re

from setuptools import setup
from setuptools.command.test import test as Command


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
        "sphinx",
        "enum-tools",
        "sphinx-toolbox",
        "sphinxcontrib_trio",
        "sphinx-rtd-theme",
        "sphinxext-opengraph",
        "sphinx-autobuild",
    ],
    "dev": [
        "pre-commit==2.18.1",
        "taskipy==1.10.1",
        "slotscheck==0.14.0",
        "pyright==1.1.244",
        "tox==3.24.5",
        "pytest==7.1.2",
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
    project_urls={
        "Documentation": "https://table2ascii.rtfd.io",
        "Issue tracker": "https://github.com/DenverCoder1/table2ascii/issues",
    },
    license="MIT",
    packages=["table2ascii"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    keywords="table ascii unicode formatter",
    python_requires=">=3.6",
    install_requires=[requirements()],
    extras_require=extras_require,
    setup_requires=[
        "flake8>=3.8,<4",
    ],
    tests_require=[
        "pytest>=6.2,<7",
    ],
)
