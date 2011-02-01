"""The compare module contains the components you need to
compare values and ensure that your expectations are met.

To make use of this module, you simply import the "expect"
starter into your spec/test file, and specify the expectation
you have about two values.

The expect starter is simply an alias to the Expr class so
you may use it like so:

    >>> expect(5 + 10).value == 15
    True
"""

class Expr(object):
    """Encapsulates a python expression, primitive value or callable
    that is to be evaluated and compared to another value.

    Serves as the basic construct for describing an expectation.
    Generally you would not use this class directly, instead it is
    available through the "expect" alias which allows for a more 
    pythonic syntax.
    
    It initializes with primitives, native types and expressions:
    
    >>> e = Expr("Foo")
    >>> e.value == "Foo"
    True
    
    >>> e = Expr(['a', 'b'])
    >>> e.value == ['a', 'b']
    True
    
    >>> Expr(4 + 7).value == 11
    True
    
    >>> Expr(4 == 7).value == False
    True
    """
    def __init__(self, value):
        self.value = value
        

# provide a usable alias for the Expr class
expect = Expr
"""Alias for the Expect class that starts an expectation contruct."""


def matcher(func):
    """Decorator to register a function as a matcher. It attaches the
    decorated function to the Expr class so that it is available through
    the "expect" starter.
    
    The matcher being registered is expected to accept at least a single parameter
    "self", which is the Expr object it is attached to.
    
    Here is a trivial example showing how to create and register a matcher:
    
    >>> def to_equal_foo(self):
    ...     assert self.value == "foo"
    >>> matcher(to_equal_foo)
    
    Now you may use the matcher with the expect syntax:
    
    >>> expect("foo").to_equal_foo()
    """
    setattr(expect, func.__name__, func)
