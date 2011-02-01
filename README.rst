Overview
========

Compare is a compact utility that provides a concise, expressive 
syntax for comparing data values. Have you been looking for a 
escape from stale XUnit style asserts that plague the omni-present 
`unittest <http://docs.python.org/library/unittest.html>`_? 
Grab a lung-full of fresh pythonic air because compare is designed 
to be a drop-in replacement for "self.assert..." cruft.

The compare public API exposes the **expect** construct which allows 
you to compare values with readable and extensible syntax.


Features
--------

- provides a base set of matchers for comparing values
- easy to extend with custom matchers
- packaged as a single drop-in module


Requirements
------------

The core implementation of compare is a single file module with no 
additional requirements beyond the 
`Python Standard Library <http://docs.python.org/library/>`_.


Installation
------------

You may install the latest stable release from PyPI with 
``pip install compare`` or with ``easy_install specit``. Alternatively, 
you may `download <http://pypi.python.org/pypi/compare>`_ the 
source package from PyPI, extract it and install it using 
``python setup.py install``.

If you wish, you may download 
`compare.py <https://github.com/rudylattae/compare/raw/master/compare.py>`_ 
(development/unstable) and put it into your project directory.


What you get
------------

When you install the package, you get the **"expect"** starter, a simple 
function that allows you to compare two values and fail if the outcome does 
not meet your expectation. This starter has extensible matchers that 
enable you to describe the expected outcome using a pythonic BDD manner. 

Compare shines brightest when you are crafting executable specifications 
for your software. It helps you maintain your flow of thought without succumbing to 
test-focused non-pythonic distrations like "self.assertEqual(s)...", 
"self.assertTrue", etc.

Here is a trivial example of the clarity you gain when you 
employ the "expect" construct in your specs::

    > cat hello.py
    greeting = 'Hello you'
    
    > cat hello_specs.py
    from compare import expect
    import hello
        
    expect(hello.greeting).to_equal('Hello you')
    
If you define an expectation that is not met, you will get an error like so::

    >>> from compare import expect
    >>> opts = ['foo', 'bar', 'baz']
    >>> expect(opts).to_contain('BAT')
    Traceback (most recent call last):
        ...
    UnmetExpectation: Expected ['foo', 'bar', 'baz'] to contain 'BAT'


Feedback
--------

I welcome any questions or feedback about bugs and suggestions on how to 
improve compare. Let me know what you think about compare. I am on twitter 
`@RudyLattae <http://twitter.com/RudyLattae>`_ . I appreciate constructive 
criticsms or high fives :)

Do you have suggestions for improvement? Then please create an 
`issue <https://github.com/rudylattae/compare/issues>`_ with details 
of what you would like to see. I'll take a look at it and work with you to either kill 
the idea or implement it.
