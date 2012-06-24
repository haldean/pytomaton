from setuptools import setup, find_packages

import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# (from http://packages.python.org/an_example_pypi_project/setuptools.html)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'pytomaton',
    version = '0.1',
    author = 'Will Haldean Brown',
    author_email = 'will.h.brown@gmail.com',
    description = 'A more convenient and succinct way of expressing state machines in Python',
    license = 'MIT',
    keywords = 'automaton state machine library',
    long_description = read('README.md'),
    url = 'https://github.com/haldean/pytomaton',
    test_suite = 'pytomaton.tests',
    packages = find_packages(),
    classifiers = [
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Libraries',
      ],
    )
