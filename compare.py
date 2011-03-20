"""The compare module contains the components you need to
compare values and ensure that your expectations are met.

To make use of this module, you simply import the :func:`expect`
starter into your spec/test file, and specify the expectation
you have about two values.
"""


# Core API
# ========

class Expr(object):
    """Wraps a python expression, primitive value or callable
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
    def __init__(self, expr, *args, **kwargs):
        self._determinant = True
        self.value = expr
        self.args = args
        self.kwargs = kwargs

    @property
    def NOT(self):
        """Negates the determinant for and returns a reference to 
        the current expectation instance to enable chaining.
        
        Behind the scenes, the NOT operator sets an internal flag, 
        the determinant. This is the flag that all matchers must 
        validate against. If the determinant is True (default), 
        then the wrapped expression is expected to evaluate to True, 
        and vice-versa.
        
        The following is a simple example to illustrate how this 
        operator affects the internals of the current expectation::
            
            >>> sound = 'Woosh'
            >>> x = Expr(sound)
            
            Default value of the determinant
            >>> x._determinant
            True
            
            NOT returns a reference to the current Expr instance
            >>> x.NOT.value == 'Woosh'
            True
            
            and it negates the determinant
            >>> x._determinant
            False
        
        For more information on the `NOT` operator, please refer to
        the documenation of the base matchers.
        """
        self._determinant = False
        return self
        
class UnmetExpectation(AssertionError):
    """Error that is raised if an expectation is not met.
    
    This error class inherits :py:exc:`AssertionError` so it is compatible with
    unittest assertion errors and plain old python "assert" errors.
    """
    pass

    
# provide a usable alias for the Expr class
expect = Expr
"""This is an alias for the :class:`Expr` class that starts an expectation contruct.
It makes it easier to construct a readable assertion/expectation for some 
value, callable or expression that you are interested in.

When you apply expect to a value or expression, that value is stored as an 
attribute on the `Expr` instance that is returned. For instance the example 
below shows how the "value" attribute is the evaluated expression::

    >>> expect(5 + 10).value == 15
    True
    
If expect is applied to a callable, it does not evaluate immediately. Whether or 
not the callable is evaluated depends on the matcher that is applied. So as you 
can see from the example below, the callable is stored as-is::

    >>> def call_me():
    ...     return "I was called..."
    >>> expect(call_me).value      # doctest: +ELLIPSIS
    <function call_me at 0x...>

However, if the function is called and passed into expect, the wrapped value stored 
is of course the return value of the callable::

    >>> expect(call_me()).value == "I was called..."
    True
"""

def matcher(obj):
    """Registers a callable object (function or callable class) as a matcher. 
    It attaches the specified callable to the Expr class so that it is available through
    the "expect" starter.
    
    *obj* is the matcher being registered. It is expected to accept at least one parameter
    `context`, which is an instance of the the Expr class it is attached to.
    
    Here is a trivial example showing how to create and register a matcher::
    
        >>> def to_equal_foo(context):
        ...     assert context.value == "foo"
        >>> matcher(to_equal_foo)
    
    Now you may use the matcher with the expect syntax::
    
        >>> expect("foo").to_equal_foo()
    
    Typically, a matcher would also accept a second parameter `other`, 
    which is the python expression, primitive or callable that the wrapped 
    value would be compared to.
    
    Another trivial matcher example. This time it takes a value to compare with
    and it spits out a helpful message if the comparison fails::
    
        >>> def to_equal(context, other):
        ...     assert context.value == other, "Expected '%s' to equal '%s'" % (context.value, other)
        >>> matcher(to_equal)
        
    You may now use the matcher in an expectation::
        
        >>> expect("foo").to_equal("foo")
        
    When the matcher fails, it tells you what went wrong::
        
        >>> expect("foo").to_equal("BAR")
        Traceback (most recent call last):
            ...
        AssertionError: Expected 'foo' to equal 'BAR'
    """
    setattr(expect, obj.__name__, obj)

def ensure(expr, outcome, message=""):
    """Compares the result of the given boolean expression to the anticipated
    boolean outcome.
    
    All the the default matchers delegate to the trusty `ensure` helper to handle 
    the actual determination of pass/fail for a given comparison. If there is a match, 
    all is well. If the comparison fails, it raises an UnmetExpectation error with 
    the given message.
    
    Stays quite if the comparison lines up::
    
        >>> ensure(5 == 5, True)
    
    Raises an error if the comparison fails::
    
        >>> ensure('Foo' == 'foo', True)
        Traceback (most recent call last):
            ...
        UnmetExpectation
    
    Raises an error with the given message if the comparison fails::
    
        >>> A = 'Foo'
        >>> B = 'foo'
        >>> message = "'%s' does not equal '%s'" % (A, B)
        >>> ensure(A == B, True, message)
        Traceback (most recent call last):
            ...
        UnmetExpectation: 'Foo' does not equal 'foo'
    """
    if expr != outcome:
        raise UnmetExpectation(message)


# Base Matchers
# =============

@matcher
def to_equal(context, other, hint=None, fail_message=None):
    """Checks if `value == other` -- simple equality.
    
    - *hint* may be optionally supplied to be used as an identifier in the failure message.
    - *message* may be provided to replace the stock failure message with your very own choice words.
    
    Passes if the values are equal::
    
        >>> expect(555).to_equal(555)
    
    Fails if the values are not equal::
    
        >>> expect('waiting...').to_equal('done!')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 'waiting...' to equal 'done!'
        
    The clarity of the failure message may be improved with a *hint*::
    
        >>> status = 'waiting...'
        >>> expect(status).to_equal('done!', 'status')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected status to equal 'done!' but got 'waiting...'
    
    Sometimes you may find it necessary to completely override the failure message::
    
        >>> status = 'waiting...'
        >>> expect(status).to_equal('done!', fail_message='OMGWTFBBQ!?! Should be done by now.')
        Traceback (most recent call last):
            ...
        UnmetExpectation: OMGWTFBBQ!?! Should be done by now.
        
    Supports negation via the `NOT` operator::
        
        >>> expect('waiting...').NOT.to_equal('done!')
        >>> expect('waiting...').NOT.to_equal('waiting...')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 'waiting...' not to equal 'waiting...'
        
        >>> expect('waiting...').NOT.to_equal('waiting...', hint='status')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected status not to equal 'waiting...' but got 'waiting...'
        
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s %(negate)sto equal %(expected)r but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r %(negate)sto equal %(expected)r"
    negate = "" if context._determinant else "not "
    message = fail_message % {'actual':context.value, 'expected':other, 'hint': hint, 'negate': negate}
    ensure(context.value == other, context._determinant, message)

@matcher
def to_be(context, other, hint=None, fail_message=None):
    """Checks if `value is other` -- identity, id().
    
    Passes if the values are identical::
    
        >>> a1 = a2 = ['foo', 'bar']
        >>> expect(a1).to_be(a2)
    
    Fails if the values are not identical::
    
        >>> b1 = ['foo', 'bar']
        >>> expect(a1).to_be(b1)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected ['foo', 'bar'] to be ['foo', 'bar']
        
    Supports negation via the `NOT` operator::
        
        >>> expect(a1).NOT.to_be(b1)
        >>> expect(a1).NOT.to_be(a2)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected ['foo', 'bar'] not to be ['foo', 'bar']
        
        >>> expect(a1).NOT.to_be(a2, hint='a1')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected a1 not to be ['foo', 'bar'] but got ['foo', 'bar']
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s %(negate)sto be %(expected)r but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r %(negate)sto be %(expected)r"
    negate = "" if context._determinant else "not "
    message = fail_message % {'actual':context.value, 'expected':other, 'hint': hint, 'negate': negate}
    ensure(context.value is other, context._determinant, message)

@matcher
def to_be_less_than(context, other, hint=None, fail_message=None):
    """Checks if `value < other`.
    
    Passes if the wrapped `value` is less than `other`::
    
        >>> expect(9).to_be_less_than(10)
    
    Fails if wrapped `value` is greater than or equal to `other`::
    
        >>> expect(9).to_be_less_than(5)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 9 to be less than 5
        
        >>> expect(9).to_be_less_than(9)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 9 to be less than 9
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to be less than %(expected)r but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to be less than %(expected)r"
    message = fail_message % {'actual':context.value, 'expected':other, 'hint': hint}
    ensure(context.value < other, True, message)
    
@matcher
def to_be_less_than_or_equal_to(context, other, hint=None, fail_message=None):
    """Checks if `value <= other`.
    
    Passes if the wrapped `value` is less than or equal to `other`::
    
        >>> expect(9).to_be_less_than_or_equal_to(10)
        >>> expect(9).to_be_less_than_or_equal_to(9)
    
    Fails if wrapped `value` is greater than `other`::
    
        >>> expect(9).to_be_less_than_or_equal_to(5)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 9 to be less than or equal to 5
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to be less than or equal to %(expected)r but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to be less than or equal to %(expected)r"
    message = fail_message % {'actual':context.value, 'expected':other, 'hint': hint}
    ensure(context.value <= other, True, message)
    
@matcher
def to_be_greater_than(context, other, hint=None, fail_message=None):
    """Checks if `value > other`.
    
    Passes if the wrapped `value` is greater than `other`::
    
        >>> expect(20).to_be_greater_than(10)
    
    Fails if wrapped `value` is less than or equal to `other`::
    
        >>> expect(20).to_be_greater_than(30)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 20 to be greater than 30
        
        >>> expect(20).to_be_greater_than(20)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 20 to be greater than 20
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to be greater than %(expected)r but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to be greater than %(expected)r"
    message = fail_message % {'actual':context.value, 'expected':other, 'hint': hint}
    ensure(context.value > other, True, message)
    
@matcher
def to_be_greater_than_or_equal_to(context, other, hint=None, fail_message=None):
    """Checks if `value >= other`.
    
    Passes if the wrapped `value` is greater than or equal to `other`::
    
        >>> expect(20).to_be_greater_than_or_equal_to(10)
        >>> expect(20).to_be_greater_than_or_equal_to(20)
    
    Fails if wrapped `value` is less than `other`::
    
        >>> expect(20).to_be_greater_than_or_equal_to(30)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 20 to be greater than or equal to 30
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to be greater than or equal to %(expected)r but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to be greater than or equal to %(expected)r"
    message = fail_message % {'actual':context.value, 'expected':other, 'hint': hint}
    ensure(context.value >= other, True, message)

@matcher
def to_be_none(context, hint=None, fail_message=None):
    """Checks that the wrapped `value` is None.
    
    Passes if the given value is None::
    
        >>> foo = None
        >>> expect(foo).to_be_none()
    
    Fails if the given value is not None::
    
        >>> bar = 'This is not None'
        >>> expect(bar).to_be_none()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 'This is not None' to be None
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to be None but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to be None"
    message = fail_message % {'actual':context.value, 'hint': hint}
    ensure(context.value is None, True, message)

@matcher
def to_be_truthy(context, hint=None, fail_message=None):
    """Evaluates the Python "truthiness" -- `bool()` of a given expression.
    See :meth:`to_be_falsy` for inverse matcher.
    
    Here are some examples of a truth value test::
    
        >>> bool(1)
        True
        >>> bool(0)
        False
        >>> bool('')
        False
        >>> bool('Foo')
        True
    
    For more information about truth value testing in Python please see 
    http://docs.python.org/library/stdtypes.html#truth-value-testing
    
    Passes if the given value is truthy::
    
        >>> foo = 'This is truthy'
        >>> expect(foo).to_be_truthy()
    
    Fails of the given value does not evaluate as truthy::
    
        >>> bar = ''
        >>> expect(bar).to_be_truthy()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected '' to be truthy
        
    As you would expect, the number `1` is truthy but `0` is not::
    
        >>> expect(1).to_be_truthy()
        >>> expect(0).to_be_truthy()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 0 to be truthy
    
    A value of `True` is truthy but `False` and `None` are not::
    
        >>> expect(True).to_be_truthy()
        >>> expect(False).to_be_truthy()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected False to be truthy
        >>> expect(None).to_be_truthy()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected None to be truthy
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to be truthy but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to be truthy"
    message = fail_message % {'actual':context.value, 'hint': hint}
    ensure(bool(context.value), True, message)

@matcher
def to_be_falsy(context, hint=None, fail_message=None):
    """Evaluates the Python "falsyness" -- `not bool()` of a given expression.
    See :meth:`to_be_truthy` for inverse matcher and details on Python truth tests.
    
    Passes if the given value is falsy::
    
        >>> foo = ''
        >>> expect(foo).to_be_falsy()
    
    Fails of the given value does not evaluate as falsy::
    
        >>> bar = 'This is not falsy'
        >>> expect(bar).to_be_falsy()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 'This is not falsy' to be falsy
    
    The number `0` is falsy but `1` is not::
    
        >>> expect(0).to_be_falsy()
        >>> expect(1).to_be_falsy()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 1 to be falsy
    
    The values `False` and `None` are falsy but `True` is not::
    
        >>> expect(False).to_be_falsy()
        >>> expect(None).to_be_falsy()
        >>> expect(True).to_be_falsy()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected True to be falsy
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to be falsy but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to be falsy"
    message = fail_message % {'actual':context.value, 'hint': hint}
    ensure(not bool(context.value), True, message)

@matcher
def to_contain(context, other, hint=None, fail_message=None):
    """Checks if the wrapped `value` contains the other value.
    
    It applies to lists, strings, dict keys
    
    Passes if the other value is in the wrapped value::
    
        >>> fruits = ['apple', 'orange', 'pear']
        >>> expect(fruits).to_contain('apple')
    
    Fails if the other value cannot be found in the wrapped value::
    
        >>> mammals = ['dog', 'whale', 'cat']
        >>> expect(mammals).to_contain('fly')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected ['dog', 'whale', 'cat'] to contain 'fly'
    
    Works for stings::
    
        >>> foo = "There is a BAR in here"
        >>> expect(foo).to_contain('BAR')
    
    And dict keys::
    
        >>> pos = {'x': 40, 'y': 500}
        >>> expect(pos).to_contain('x')
    """
    if not fail_message:
        if hint:
            fail_message = "Expected %(hint)s to contain %(expected)r but got %(actual)r"
        else:
            fail_message = "Expected %(actual)r to contain %(expected)r"
    message = fail_message % {'actual':context.value, 'expected':other, 'hint': hint}
    ensure(other in context.value, True, message)
    
@matcher
def to_return(context, expected):
    """Compares the return value of the wrapped callable to the expected value
    
    Passes if the callable returns the expected value::
    
        >>> def foo():
        ...     return "Foo"
        >>> expect(foo).to_return('Foo')
    
    Fails if the callable does not return the expected value::
    
        >>> def bar():
        ...     return "Barf"
        >>> expect(bar).to_return('Bar')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected callable to return 'Bar' but got 'Barf'
    
    If you provide parameters while wrapping the callable, they will be used::
    
        >>> def hello(who):
        ...     return "Hello " + who
        >>> expect(hello, "Fuzz ball").to_return('Hello Fuzzy')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected callable to return 'Hello Fuzzy' but got 'Hello Fuzz ball'
        
    And of course keyword args (kwargs) are also supported::
    
        >>> def baz(a, b="change", c="me"):
        ...     return "Baz %s %s %s" % (a, b, c)
        >>> expect(baz, "please").to_return('Baz please change me')
        >>> expect(baz, "params", b="got", c="changed!").to_return('Baz params got changed!')

    """
    actual = context.value(*context.args, **context.kwargs)
    message = "Expected callable to return %r but got %r" % (expected, actual)
    ensure(actual == expected, True, message)

@matcher
def to_raise(context, exception_class=None, exception_message=None):
    """Invokes the provided callable and ensures that it raises an Exception.
    
    Passes if the callable raises an exeption (any exception)::
    
        >>> def bad():
        ...     raise Exception()
        >>> expect(bad).to_raise()
        
    Fails if the callable does not raise any exception::
    
        >>> def good():
        ...     return "No exceptions here"
        >>> expect(good).to_raise()
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected callable to raise an exception
        
    You may specify the type of exception you expect to be raised. The expectation 
    will fail if the callable raises an exception which is not an instance of the 
    expected exception class::
    
        >>> class MildError(Exception):
        ...     pass
        >>> class CatastrophicError(Exception):
        ...     pass
        
        >>> def raise_custom_exception():
        ...     raise MildError
        >>> expect(raise_custom_exception).to_raise(CatastrophicError)
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected callable to raise CatastrophicError() but got MildError()
        
    Further, you may specify the message you expect the exception to be raised with.
    The expectation will fail if the callable raises the right exception but with 
    a non matching message::
    
        >>> def raise_exception_with_message():
        ...     raise CatastrophicError('BOOM!')

        >>> expect(raise_exception_with_message).to_raise(CatastrophicError, 'Ohly Crap...')
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected callable to raise CatastrophicError('Ohly Crap...',) 
          but got CatastrophicError('BOOM!',)
    """
    raised = False
    actual_exception = None
    
    try:
        context.value(*context.args, **context.kwargs)
    except Exception as e:
        actual_exception = e
        raised = True
    
    if exception_class and exception_message:
        message = "Expected callable to raise %r \n  but got %r" % (exception_class(exception_message), actual_exception)
        ensure(raised and isinstance(actual_exception, exception_class) and actual_exception.message == exception_message, True, message)
    elif exception_class:
        message = "Expected callable to raise %r but got %r" % (exception_class(), actual_exception)
        ensure(raised and isinstance(actual_exception, exception_class), True, message)
    else:
        message = "Expected callable to raise an exception"
        ensure(raised, True, message)


# Rich Comparison Matchers
# ========================
# These are convenient matchers that harness the Python "rich comparison" 
# methods to provide alternatives to some of the more verbose the base matchers.

@matcher
def __eq__(context, other):
    """Checks if `value == other`. It is an alternative to the to_equal base matcher.
    For instance, this example::
    
        >>> expect(555).to_equal(555)
    
    May be expressed as::
    
        >>> expect(555) == 555
    
    Fails if the values are not equal::
    
        >>> expect('waiting...') == 'done!'
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 'waiting...' to equal 'done!'
    """
    context.to_equal(other)

@matcher
def __lt__(context, other):
    """Checks if `value < other`. It is an alternative to the to_be_less_than base matcher.
    For instance, this example::
    
        >>> expect(45).to_be_less_than(50)
    
    May be expressed as::
    
        >>> expect(45) < 50
    
    Fails if the wrapped `value` is not less than `other`::
    
        >>> expect(350) < 200
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 350 to be less than 200
    """
    context.to_be_less_than(other)

@matcher
def __le__(context, other):
    """Checks if `value <= other`. It is an alternative to the 
    to_be_less_than_or_equal_to base matcher. For instance, this example::
    
        >>> expect(50).to_be_less_than_or_equal_to(50)
    
    May be expressed as::
    
        >>> expect(50) <= 50
    
    Fails if the wrapped `value` is greater than `other`::
    
        >>> expect(201) <= 200
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 201 to be less than or equal to 200
    """
    context.to_be_less_than_or_equal_to(other)

@matcher
def __gt__(context, other):
    """Checks if `value > other`. It is an alternative to the to_be_greater_than base matcher.
    For instance, this example::
    
        >>> expect(45).to_be_greater_than(40)
    
    May be expressed as::
    
        >>> expect(45) > 40
    
    Fails if the wrapped `value` is not greater than `other`::
    
        >>> expect(150) > 200
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 150 to be greater than 200
    """
    context.to_be_greater_than(other)

@matcher
def __ge__(context, other):
    """Checks if `value >= other`. It is an alternative to the 
    to_be_greater_than_or_equal_to base matcher. For instance, this example::
    
        >>> expect(50).to_be_greater_than_or_equal_to(50)
    
    May be expressed as::
    
        >>> expect(50) >= 50
    
    Fails if the wrapped `value` is less than `other`::
    
        >>> expect(199) >= 200
        Traceback (most recent call last):
            ...
        UnmetExpectation: Expected 199 to be greater than or equal to 200
    """
    context.to_be_greater_than_or_equal_to(other)
