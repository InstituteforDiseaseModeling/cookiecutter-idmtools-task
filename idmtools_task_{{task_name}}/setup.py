#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script for the idmtools_task_{{task_name}} platform"""
import sys

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().split("\n")

build_requirements = ['flake8', 'coverage', 'py-make', 'bump2version', 'twine']
setup_requirements = []
test_requirements = ['pytest', 'pytest-runner', 'pytest-timeout', 'pytest-cache'] + build_requirements

extras = dict(test=test_requirements, packaging=build_requirements)

# check for python 3.7
if sys.version_info[0] == 3 and sys.version_info[1] == 7 and sys.version_info[2] < 3:
    raise EnvironmentError("Python 3.7 requires 3.7.3 or higher")

authors = [
    ("{{full_name}}", "{{email}}"),
]

setup(
    author=[author[0] for author in authors],
    author_email=[author[1] for author in authors],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework:: IDM-Tools :: models'
    ],
    description="Core tools for modeling",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='modeling, IDM',
    name='idmtools_task_{{task_name}}',
    entry_points=dict(idmtools_task=  # noqa E521
                      ["idmtools_task_{{task_name}} = idmtools_task_{{task_name}}.{{task_name}}TaskSpecification"
                       ]
                      ),
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    extras_require=extras,
    version='1.0.0+nightly'
)
