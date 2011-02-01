import os
from setuptools import setup

version = '0.1a'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.txt').read(),
])

setup(
    name = "compare",
    version = version,
    description = "Concise, expressive syntax for comparing data values. A pluggable alternative to XUnit style asserts.",
    long_description = long_description,
    author = "Rudy Lattae",
    author_email = "rudylattae@gmail.com",
    url = 'https://github.com/rudylattae/compare',
    license = "Simplified BSD",
    keywords = ['compare', 'matcher', 'to be', 'to equal', 'assert', 'test equality', 'specification', 'BDD', 'TDD'],
    classifiers = [
        'Development Status :: 3 - Alpha',
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