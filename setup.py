# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='CS 430 Summer 2020 Project',
    version='0.1.0',
    description='A project from the IIT Intro to Algorithms class',
    long_description=readme,
    author='Emma Foley-Beaver',
    author_email='efoley@hawk.iit.edu.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

