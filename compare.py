"""The compare module contains the components you need to
compare values and ensure that your expectations are met.

To make use of this module, you simply import the "expect"
starter into your spec/test file, and specify the expectation
you have about two values.

The expect starter is simply an alias to the Expr class so
you may use it like so::

    >>> expect(5 + 10).value == 15
    True
"""


# core
# ====

class Expr(object):
    """Encapsulates a python expression, primitive value or callable
    that is to be evaluated and compared to another value.

    Serves as the basic construct for describing an expectation.
    Generally you would not use this class directly, instead it is
    available through the "expect" alias which allows for a more 
    pythonic syntax.
    
    It initializes with primitives, native types and expressions::
    
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

class UnmetExpectation(AssertionError):
    """Error that is raised if an expectation is not met.
    
    This error class inherits AssertionError so it is compatible with
    unittest assertion errors and plain old python "assert" errors.
    """

# provide a usable alias for the Expr class
expect = Expr
"""Alias for the Expect class that starts an expectation contruct."""

def matcher(func):
    """Decorator to register a function as a matcher. It attaches the
    decorated function to the Expr class so that it is available through
    the "expect" starter.
    
    The matcher being registered is expected to accept at least a single parameter
    "self", which is the Expr object it is attached to.
    
    Here is a trivial example showing how to create and register a matcher::
    
        >>> def to_equal_foo(self):
        ...     assert self.value == "foo"
        >>> matcher(to_equal_foo)
    
    Now you may use the matcher with the expect syntax::
    
        >>> expect("foo").to_equal_foo()
    
    Typically, a matcher would also accept a second parameter "expected", 
    which is the python expression, primitive or callable that the initial 
    value would be compared to.
    
    Another trivial matcher example, this time it takes a value to compare with
    and it spits out a helpful message if the comparison fails::
    
        >>> def to_equal(self, expected):
        ...     assert self.value == expected, "Expected '%s' to equal '%s'" % (self.value, expected)
        >>> matcher(to_equal)
        
    You may now use the matcher in an expectation::
        
        >>> expect("foo").to_equal("foo")
        
    When the matcher fails, it tells you what went wrong::
        
        >>> expect("foo").to_equal("BAR")
        Traceback (most recent call last):
            ...
        AssertionError: Expected 'foo' to equal 'BAR'
    """
    setattr(expect, func.__name__, func)

def verify(expr, outcome, message=""):
    """Compares the result of the given boolean expression to the anticipated
    boolean outcome. If there is a match, all is well. If the comparison fails,
    it raises an UnmetExpectation error with the given message
    
    Stays quite if the comparison lines up::
    
        >>> verify(5 == 5, True)
    
    Raises an error if the comparison fails::
    
        >>> verify('Foo' == 'foo', True)
        Traceback (most recent call last):
            ...
        UnmetExpectation
    
    Raises an error with the given message if the comparison fails::
    
        >>> actual = 'Foo'
        >>> expected = 'foo'
        >>> message = "'%s' does not equal '%s'" % (actual, expected)
        >>> verify(actual == expected, True, message)
        Traceback (most recent call last):
            ...
        UnmetExpectation: 'Foo' does not equal 'foo'
    """
    if expr != outcome:
        raise UnmetExpectation(message)


# Matchers
# ========

@matcher
def to_equal(self, expected):
    """Compares values based on simple equality "=="
    
    Passes if the values are equal::
    
        >>> expect(555).to_equal(555)
    
    Fails if the values are not equal::
    
        >>> expect('waiting...').to_equal('done!')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 'waiting...' to equal 'done!'
    """
    message = "Expected %r to equal %r" % (self.value, expected)
    verify(self.value == expected, True, message)


@matcher
def to_be(self, expected):
    """Compares values based on identity ("is")
    
    Passes if the values are identical
    
    >>> a1 = a2 = ['foo', 'bar']
    >>> expect(a1).to_be(a2)
    
    Fails if the values are not identical
    
    >>> b1 = ['foo', 'bar']
    >>> expect(a1).to_be(b1)
    Traceback (most recent call last):
        ...
    UnmetExpectation: Expected ['foo', 'bar'] to be ['foo', 'bar']
    """
    message = "Expected %r to be %r" % (self.value, expected)
    verify(self.value is expected, True, message)
