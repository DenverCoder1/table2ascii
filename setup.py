# /usr/bin/env python
import os
from setuptools import setup
from setuptools.command.test import test as TestCommand, Command


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["tests", "-s"]
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        raise SystemExit(errno)


class LintCommand(Command):
    """
    A copy of flake8's Flake8Command
    """

    description = "Run flake8 on modules registered in setuptools"
    user_options = []

    def initialize_options(self):
        # must override
        pass

    def finalize_options(self):
        # must override
        pass

    def distribution_files(self):
        if self.distribution.packages:
            for package in self.distribution.packages:
                yield package.replace(".", os.path.sep)

        if self.distribution.py_modules:
            for filename in self.distribution.py_modules:
                yield "%s.py" % filename

    def run(self):
        from flake8.api.legacy import get_style_guide

        flake8_style = get_style_guide(config_file="setup.cfg")
        paths = self.distribution_files()
        report = flake8_style.check_files(paths)
        raise SystemExit(report.total_errors > 0)


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.read().split("\n")

setup(
    name="table2ascii",
    version="0.1.1",
    author="Jonah Lawrence",
    author_email="jonah@freshidea.com",
    description="Convert 2D Python lists into Unicode/Ascii tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DenverCoder1/table2ascii",
    project_urls={
        "Bug Tracker": "https://github.com/DenverCoder1/table2ascii/issues",
    },
    packages=["table2ascii"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=[requirements],
    setup_requires=[
        "flake8>=3.8,<4",
    ],
    tests_require=[
        "pytest>=6.2,<7",
    ],
    cmdclass={
        "test": PyTest,
        "lint": LintCommand,
    },
)
