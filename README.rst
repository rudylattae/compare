.. _compare page on PyPI: http://pypi.python.org/pypi/compare
.. _compare.py: https://github.com/rudylattae/compare/raw/master/compare.py
.. _create an issue: https://github.com/rudylattae/compare/issues
.. _unittest: http://docs.python.org/library/unittest.html
.. _Python Standard Library: http://docs.python.org/library/

Overview
========

Compare is a compact utility that provides an alternative, expressive 
syntax for comparing data values. Have you been looking for an escape 
from the stale XUnit style asserts that plague the omni-present unittest_? 
You may have found just what you need. I invite you to take a look at this 
little utility. If it fits your style, you may use it as a drop-in 
replacement for the "self.assert..." style of doing assertions in python.

The compare API exposes the **expect** construct which allows 
you to compare values with readable and extensible syntax. It was designed 
to be a stand-alone alternative assertion syntax. As such you may use it 
as-is with your favorite testing/specification framework.

**Documentation**: http://packages.python.org/compare

**Project source**: https://github.com/rudylattae/compare

**PyPI page**: http://pypi.python.org/pypi/compare


Features
--------

- provides a base set of matchers for comparing values
- easy to extend with custom matchers
- packaged as a single drop-in module


Requirements
------------

The core implementation of compare is a single file module with no 
additional requirements beyond the `Python Standard Library`_.


Installation
------------

The simplest and recommended way to install compare is with Pip. You may install 
the latest stable release from PyPI with pip::

    > pip install compare

If you do not have pip, you may use easy_install::

    > easy_install compare

Alternatively, you may download the source package from the `compare page on PyPI`_, 
extract it and install it using::

    > python setup.py install

If you wish, you may grab the in development (cutting-edge but unstable) 
version `compare.py`_ from the project repository and put it into your project directory.


What you get
------------

When you install the package, you get the **"expect"** starter, a simple 
function that allows you to compare two values and fail if the outcome does 
not meet your expectation. This starter has extensible matchers that 
enable you to describe the expected outcome in a pythonic BDD manner. 

Compare shines brightest when you are crafting executable specifications 
for your software. It helps you maintain your flow of thought without succumbing to 
test-focused non-pythonic distrations like "self.assertEqual(s)...", 
"self.assertTrue", etc.

Here is a trivial example of the readability you gain when you 
employ the "expect" construct in your specs.

`> cat hello.py`::

    greeting = 'Hello you'

`> cat hello_specs.py`::

    from compare import expect
    import hello
    
    expect(hello.greeting).to_equal('Hello you')

If you define an expectation that is not met, you will get an "Unmet Expectation" error 
which inherits from the python AssertionError so it is compatible with the usual unittest 
tools. Here is an example of such an error::

    >>> from compare import expect
    >>> opts = ['foo', 'bar', 'baz']
    >>> expect(opts).to_contain('BAT')
    Traceback (most recent call last):
        ...
    UnmetExpectation: Expected ['foo', 'bar', 'baz'] to contain 'BAT'


What's missing
--------------

The `expect` syntax does not yet have a clean way to negate a matcher. This feature is 
planned for the next release. An example of the anticipated usage::

    expect(['a', 'c', 'd']).NOT.to_contain('b')

The `to_return` matcher does not accept any parameters to pass to the callable.

Matchers do not accept custom fail messages.


Feedback
--------

I welcome any questions or feedback about bugs and suggestions on how to 
improve compare. Let me know what you think about compare. I am on twitter 
`@RudyLattae <http://twitter.com/RudyLattae>`_ . I appreciate constructive 
criticsms or high fives :)

Do you have suggestions for improvement? Then please `create an issue`_ with details 
of what you would like to see. I'll take a look at it and work with you to either kill 
the idea or implement it.
