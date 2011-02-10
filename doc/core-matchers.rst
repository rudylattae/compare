.. currentmodule:: compare

=============
Core Matchers
=============

When a :mod:`compare` matcher is registered, it is simply attached to 
the :class:`Expr` class. The matcher may then be accessed through the 
:func:`expect` function/starter.


Base Matchers
=============

Compare ships with some generic/base matchers that focus on handling 
simple comparisons. If you need use-case specific matchers, it is very 
easy to create and attach your own matcher to the :class:`Expr` class. 
In fact you are encouraged to create custom matchers since they make your 
assertions more readable and concise.

Here are the base matchers that are available by default:


`to_equal`
----------
.. automethod:: Expr.to_equal

`to_be`
-------
.. automethod:: Expr.to_be

`to_be_less_than`
-----------------
.. automethod:: Expr.to_be_less_than

`to_be_less_than_or_equal_to`
-----------------------------
.. automethod:: Expr.to_be_less_than_or_equal_to

`to_be_greater_than`
--------------------
.. automethod:: Expr.to_be_greater_than

`to_be_greater_than_or_equal_to`
--------------------------------
.. automethod:: Expr.to_be_greater_than_or_equal_to

`to_be_none`
------------
.. automethod:: Expr.to_be_none

`to_be_truthy`
--------------
.. automethod:: Expr.to_be_truthy

`to_be_falsy`
-------------

.. automethod:: Expr.to_be_falsy

`to_contain`
------------
.. automethod:: Expr.to_contain

`to_return`
------------
.. automethod:: Expr.to_return

`to_raise`
------------
.. automethod:: Expr.to_raise


"Rich Comparison" Matchers
==========================

These are convenient matchers that harness the concept of Python "rich comparison" 
methods to provide succinct alternatives to some of the more verbose `base matchers`_.
For more information on these special methods, please see: 
http://docs.python.org/reference/datamodel.html#special-method-names

`== , equal to`
---------------
.. automethod:: Expr.__eq__

`< , less than`
---------------
.. automethod:: Expr.__lt__

`<= , less than or equal to`
----------------------------
.. automethod:: Expr.__le__
