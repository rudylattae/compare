===========
Get started
===========

To get started with compare, simply import the :func:`expect` function into 
your module. You may then use the function to handle any comparisons 
and assertions you wish to make about values in your code.


Verifying expectations with the base matchers
=================================================

Below is a simple example showing how you use the builtin matchers
to craft readable specifications for your code::

    >>> from compare import expect
    
    >>> fruit = 'Orange'
    
    >>> expect(fruit).to_equal('Orange')
    >>> expect(fruit).to_equal('Apple')
    Traceback (most recent call last):
        ...
    UnmetExpectation: Expected 'Orange' to equal 'Apple'


Verifying expectations with the "rich comparison" matchers
==================================================================

If you find some of the base matchers too verbose for your 
examples, you may take advantage of the alternative syntax 
through the rich comparison matchers. Here is what the previous 
example would look like with rich comparisons::

    >>> from compare import expect
    
    >>> fruit = 'Orange'
    
    >>> expect(fruit) == 'Orange'
    >>> expect(fruit) == 'Apple'
    Traceback (most recent call last):
        ...
    UnmetExpectation: Expected 'Orange' to equal 'Apple'

To illustrate the major benefit of rich comparason matchers, 
note that the following expectations achieve the same goal.::

    >>> from compare import expect
    
    >>> expect(960).to_be_greater_than_or_equal_to(950)
    >>> expect(960) >= 950


Using custom matchers to enhance clarity
============================================

A compare matcher is a regular python function that can be 
wired into the :class:`Expr` class. You may extend compare with 
custom matchers that make make your examples succinct and 
easy to follow::

    >>> from compare import expect, matcher, ensure
    
    >>> @matcher
    ... def to_be_citrus(self):
    ...     ensure(self.value in ['Orange'], True, 
    ...         "Expected %r to be a citrus fruit" % self.value)
    
    >>> fruit = 'Orange'
    >>> expect(fruit).to_be_citrus()
