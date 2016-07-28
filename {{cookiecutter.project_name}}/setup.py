#!/usr/bin/env python
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []
with open('requirements.txt') as requirements_file:
    requirements = [l.strip('\n') for l in requirements_file]


test_requirements = []
with open('requirements-dev.txt') as test_requirements_file:
    test_requirements = [l for l in test_requirements_file]


setup(
    name='{{cookiecutter.project_name}}',
    version='0.1.0',
    long_description=readme,
    packages=[
        '{{cookiecutter.project_name}}',
    ],
    package_dir={
        '{{cookiecutter.project_name}}': '{{cookiecutter.project_name}}'
    },
    scripts=[
        'bin/{{cookiecutter.project_name}}',
    ],
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
)
