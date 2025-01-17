#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit fish_project/__version__.py
version = {}
with open(os.path.join(here, 'fish_project', '__version__.py')) as f:
    exec(f.read(), version)

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='fish_project',
    version=version['__version__'],
    description="Secret fish project about fishing",
    long_description=readme + '\n\n',
    author="Faruk D.",
    author_email='faruk@universe.nl',
    url='https://github.com//fish_project',
    packages=[
        'fish_project',
    ],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='fish_project',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    install_requires=[],  # FIXME: add your package's dependencies to this list
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
    extras_require={
        'dev':  ['prospector[with_pyroma]', 'yapf', 'isort'],
    }
)
