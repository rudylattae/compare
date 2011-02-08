==============
Usage examples
==============

To make use of compare, simply import the :func:`expect` function into 
your module. You may then use the function to handle any comparisons 
and assertions you wish to make about values in your code.


Verifying expectations with the basic matchers
----------------------------------------------

Below is a simple example showing how you use the builtin matchers
to craft readable specifications for your code::

    >>> from compare import expect
    
    >>> fruit = 'Orange'
    
    >>> expect(fruit).to_equal('Orange')
    >>> expect(fruit).to_equal('Apple')
    Traceback (most recent call last):
        ...
    UnmetExpectation: Expected 'Orange' to equal 'Apple'
    

Creating and using custom matchers
----------------------------------

A compare matcher is a regular python function that can be 
wired into the :class:`Expr` class. You may extend compare with 
custom matchers that make make your examples succinct and 
easy to follow::

    >>> from compare import expect, matcher, ensure
    
    >>> @matcher
    ... def to_be_citrus(self):
    ...     ensure(self.actual in ['Orange'], True, 
    ...         "Expected %r to be a citrus fruit" % self.actual)
    
    >>> fruit = 'Orange'
    >>> expect(fruit).to_be_citrus()
