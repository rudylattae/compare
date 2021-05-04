# Overview
___

This project primarily updates compare to be used on accessible on Python3

Compare is a compact utility that provides an alternative, expressive 
syntax for comparing data values. You may use it as a drop-in 
replacement for the "assert..." style of assertions in python.

The compare API exposes the **expect** constructs which allows 
you to compare values with readable and extensible syntax. It was designed 
to be a stand-alone alternative assertion syntax. As such you may use it 
as-is with your favorite testing/specification framework.

Requirements
___

The core implementation of compare is a single file module with no 
additional requirements beyond the `Python Standard Library`_.


Installation
___

The simplest and recommended way to install compare is with Pip. You may install 
the latest stable release from PyPI with pip::

    > pip install compare3

If you do not have pip, you may use easy_install::

    > easy_install compare3

Alternatively, you may download the source package from the `compare3 page on PyPI`_, 
extract it and install it using::

    > python setup.py install


# What's in it?
___

You get the **"expect"** starter, a simple 
class that allows you to compare two values and fail if the outcome does 
not meet your expectation. This class enables you to describe the expected outcome in a pythonic BDD manner. 

Compare shines brightest when you are crafting executable specifications 
for your software. It helps you maintain your flow of thought without succumbing to 
test-focused non-pythonic distrations like "self.assertEqual(s)...", 
"self.assertTrue", etc.


#Examples
___
## Basic Usage
```python
from compare3 import expect

test_value="grapes"
expect(test_value).equal_to("grapes")
expect(test_value).is_not_.equal_to("apples")
```
## Chaining
expect expressions can be chained ot validate more than one assertion with a single line

```python
from compare3 import expect
test_value=30
expect(test_value).is_.numeric().and_.greater_than(15)
```

## On Failure of Assertion
When an expectation fails, An UnexpectedExpectation error is raised. 
This Error inherits from AssertionError maintaining compatibility with standard
python assertions.
```python
from compare3 import UnmetExpectation,expect
test_value=20
try:
    expect(test_value).equal_to("apples")
except UnmetExpectation as e:
    expect(str(e)).equal_to("'20' is not equal to 'apples'")

try:
    expect(test_value).equal_to("apples")
except AssertionError as e:
    expect(str(e)).equal_to("'20' is not equal to 'apples'")
```

## Callables
compare3 also comes with **expect_call** which allows for additional validation on callable objects.

validation can occur on the return value or when raising an error.

.returns will validate the return of the callable with it's associated arguments with the expected value argument.

.raises will call the callable and check if the expected Exception was raised. If either a
different exception was raised or no exception was raised it will cause an UnmetExpectation.

You can optionally also define an error message. This uses re.fullMatch to match the error message.

```python
from compare3 import expect_call
def summer(*args):
    return sum([int(i) for i in args])

expect_call(summer,12,50,45).returns(107)
expect_call(summer,"25","apples","75").raises(ValueError,
                                  "invalid literal for .* 'apples'")
```


___

**Forked From Source: https://github.com/rudylattae/compare**

Thank you rudylattae for an interesting idea on making assertions.