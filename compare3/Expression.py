from compare3.errors import UnmetExpectation
from logging import Logger
from numbers import Number
import re

class Expression(object):
    logger = Logger("expressions")
    comparison_log_level = 10

    """
    Wraps a python expression

    Serves as the basic construct for describing an expectation.
    Generally you would not use this class directly, instead it is
    available through the "expect" alias.
    
    This class can be extended via inheritance to set up your own custom expressions.
    
    Examples of using Expressions (expect) can be found in README.md

    It initializes with primitives, native types and expressions:

        >>> e = Expression("Foo")
        >>> e.value == "Foo"
        True

        >>> e = Expression(['a', 'b'])
        >>> e.value == ['a', 'b']
        True

        >>> Expression(4 + 7).value == 11
        True

        >>> Expression(4 == 7).value == False
        True
    """

    def __init__(self, value):
        self._determinant: bool = True
        self.value = value

    def _ensure(self, expression, value_to_match, message):
        if self._determinant:
            if expression != value_to_match:
                raise UnmetExpectation(message)
        else:
            if expression == value_to_match:
                raise UnmetExpectation(message)

        return self

    def _message(self, expected, actual=None, msg_type="equal to"):
        msg = "'{}' is {}{} '{}'".format(expected, "not " if self._determinant else "", msg_type, actual)
        return msg

    def log(self, msg):
        return self.__class__.logger.log(self.__class__.comparison_log_level, msg)

    @property
    def is_(self) -> 'Expression':
        self._determinant = True
        return self

    @property
    def is_not_(self) -> 'Expression':
        self._determinant = False
        return self

    @property
    def and_(self) -> 'Expression':
        self._determinant = True
        return self

    def equal_to(self, value):
        self.log("checking if '{}'{} equal_to '{}'".format(self.value," not" if self._determinant else "",value))
        return self._ensure(self.value == value, True, self._message(self.value, value))

    def equal_to_as_strings(self, value):
        self.log("checking if '{}'{} equal_to_as_strings '{}'".format(self.value, " not" if self._determinant else "", value))
        return self._ensure(str(self.value) == str(value), True, self._message(self.value, value))

    def equal_to_as_integer(self, value):
        self.log("checking if '{}'{} equal_to_as_integer '{}'".format(self.value, " not" if self._determinant else "", value))
        return self._ensure(int(self.value) == int(value), True, self._message(int(self.value), int(value)))

    def equal_to_as_floating_point(self, value):
        self.log("checking if '{}'{} equal_to_as_floating_point '{}'".format(self.value, " not" if self._determinant else "", value))
        return self._ensure(float(self.value) == float(value), True, self._message(float(self.value), float(value)))

    def greater_than(self, value):
        self.log("checking if '{}'{} greater_than '{}'".format(self.value, " not" if self._determinant else "", value))
        return self._ensure(self.value > value, True, self._message(self.value, value, "greater than"))

    def greater_than_or_equal_to(self, value):
        self.log("checking if '{}'{} greater_than_or_equal_to '{}'".format(self.value, " not" if self._determinant else "", value))
        return self._ensure(self.value >= value, True, self._message(self.value, value, "greater than or equal to"))

    def less_than(self, value):
        self.log("checking if '{}'{} less_than '{}'".format(self.value, " not" if self._determinant else "", value))
        return self._ensure(self.value < value, True, self._message(self.value, value, "less than"))

    def less_than_or_equal_to(self, value):
        self.log("checking if '{}'{} less_than_or_equal_to '{}'".format(self.value, " not" if self._determinant else "", value))
        return self._ensure(self.value <= value, True, self._message(self.value, value, "less than or equal to"))

    def none(self):
        self.log("checking if '{}' is{} None".format(self.value, " not" if self._determinant else ""))
        return self._ensure(self.value is None, True,
                            "{} is{} None".format(self.value, " not" if self._determinant else ""))

    def truthy(self):
        self.log("checking if '{}' is{} truthy".format(self.value, " not" if self._determinant else ""))
        return self._ensure(bool(self.value), True,
                            "{} {} truthy".format(self.value, "doesn't seem" if self._determinant else "seems"))

    def falsy(self):
        self.log("checking if '{}' is{} falsy".format(self.value, " not" if self._determinant else ""))
        return self._ensure(bool(self.value), False,
                            "{} {} falsy".format(self.value, "doesn't seem" if self._determinant else "seems"))

    def contains(self, value):
        self.log("checking if '{}' is{} in '{}'".format(value, " not" if self._determinant else "", self.value))
        return self._ensure(value in self.value, True,
                            "{} was{} in {}".format(self.value, " not" if self._determinant else "", value))

    def numeric(self):
        self.log("checking if '{}' is{} numeric".format(self.value, " not" if self._determinant else ""))
        return self._ensure(isinstance(self.value, Number), True,
                            "{} {} numeric".format(self.value, "doesn't seem" if self._determinant else "seems"))

    def alphabetical(self):
        self.log("checking if '{}' is{} alphabetical".format(self.value, " not" if self._determinant else ""))
        return self._ensure(re.fullmatch("[a-zA-Z]*", self.value) is not None, True,
                            "{} {} alphabetical".format(self.value, "doesn't seem" if self._determinant else "seems"))

    def alphanumeric(self):
        self.log("checking if '{}' is{} alphanumeric".format(self.value, " not" if self._determinant else ""))
        return self._ensure(re.fullmatch("[a-zA-Z0-9]*", self.value) is not None, True,
                            "{} {} alphabetical".format(self.value, "doesn't seem" if self._determinant else "seems"))

    def __eq__(self, other):
        self.equal_to(other)

    def __lt__(self, other):
        self.less_than(other)

    def __le__(self, other):
        self.less_than_or_equal_to(other)

    def __gt__(self, other):
        self.greater_than(other)

    def __ge__(self, other):
        self.greater_than_or_equal_to(other)


class Callable(Expression):
    """
    Wraps a python callable

    Serves as the basic construct for describing an expectation when it comes to callables.
    Generally you would not use this class directly, instead it is
    available through the "expect_call" alias.

    This class can be extended via inheritance to set up your own custom expressions.

    Examples of using Expressions (expect_call) can be found in README.md

    It initializes with functions, and any other callable, and it's associated arguments:


        >>>def callable_funciton(*args,**kwargs):
        >>>    print('args: {}, kwargs: {}'.format(args,kwargs))
        >>>
        >>> e = Callable(callable_function,"arg1","arg2",3,4,kw_arg1="apples",kw_arg2="oranges")
        >>> e.value.__name__ == "callable_function"
        >>> e.args == ["arg1", "arg2", 3, 4]
        >>> e.kwargs == {"kw_arg1":"apples", "kw_arg2":"oranges"}
        True
        True
        True

    """

    def __init__(self, expect, *args, **kwargs):
        super().__init__(expect)
        self.args = args
        self.kwargs = kwargs

    def returns(self, expected):
        self.log("Calling {} with:\nargs: {}\nkwargs:{}".format(self.value.__name__, self.args,self.kwargs))
        return_val = self.value(*self.args, **self.kwargs)

        self.log("checking if return: {} is{} equal to {}".format(return_val, " not" if self._determinant else "", expected))
        self._ensure(return_val == expected, True,
                     "{} {}return {}, it returned {} instead".format(self.value,
                                                                     "did not " if self._determinant else "",
                                                                     expected, return_val))

    def raises(self, exception_type, exception_message=None):
        try:
            self.log("Calling {} with:\nargs: {}\nkwargs:{}\nexpecting exception class {}".format(
                self.value.__name__,
                self.args, self.kwargs,
                exception_type
            ))
            self.value(*self.args, **self.kwargs)
        except Exception as e:
            self._ensure(isinstance(e, exception_type),
                         True,
                         "{} {}raise {}, it returned {} instead".format(self.value.__name__,
                                                                        "did not " if self._determinant else "",
                                                                        exception_type.__class__.__name__,
                                                                        e.__class__.__name__))
            if exception_message is not None:
                self.log("checking {} with:\nargs: {}\nkwargs:{}\nexpecting exception class {}".format(
                    self.value.__name__,
                    self.args, self.kwargs,
                    exception_type
                ))
                expected = re.fullmatch(exception_message, str(e))
                self._ensure(expected is not None, True,
                             self._message(exception_message, str(e), msg_type="match pattern"))
        else:
            raise UnmetExpectation("call '{}' did not raise '{}' error".format(self.value.__name__, exception_type.__class__.__name__))



