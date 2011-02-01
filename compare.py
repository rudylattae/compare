"""The compare module contains the components you need to 
compare values and ensure that your expectations are met.

To make use of this module, you simply import the "expect" 
starter into your spec/test file, and specify the expectation 
you have about two values.
"""

class Expr(object):
    """Encapsulates a python expression, primitive value or callable
    that is to be evaluated and compared to another value.

    Serves as the basic construct for describing an expectation.
    Generally you would not use this class directly, instead it is 
    available through the "expect" alias which allows for a more 
    pythonic syntax.
    
    It initializes with primitives, native types and expressions
    
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
        
