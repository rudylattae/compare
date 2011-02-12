import os
from setuptools import setup

version = '0.2b'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.txt').read(),
])

setup(
    name = "compare",
    version = version,
    description = "Alternative syntax for comparing/asserting expressions in Python. Supports pluggable matchers for custom comparisons.",
    long_description = long_description,
    author = "Rudy Lattae",
    author_email = "rudylattae@gmail.com",
    url = 'https://github.com/rudylattae/compare',
    license = "Simplified BSD",
    keywords = ['python', 'compare', 'matcher', 'to be', 'to equal', 'assert', 'test equality', 'specification', 'BDD', 'TDD'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules = ['compare'],
    zip_safe = False
)