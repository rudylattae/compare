from setuptools import setup
from pathlib import Path

parent = Path(__file__).parent
readme = parent / "README.md"
with open(str(readme)) as f:
    long_description = f.read()

setup(
    name = "compare3",
    version = "1.0.1",
    description = "Alternative syntax for comparing/asserting expressions in Python 3.",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = "Austin Stromness",
    author_email = "stromnessdevelopment@gmail.com",
    url = 'https://github.com/astromness/compare',
    download_url='https://github.com/astromness/compare/archive/refs/tags/1.0.1.tar.gz',
    license = "Simplified BSD",
    keywords = ['python', 'compare', 'matcher', 'to be', 'to equal', 'assert', 'test equality', 'specification', 'BDD', 'TDD'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)