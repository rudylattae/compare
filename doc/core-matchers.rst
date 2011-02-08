.. currentmodule:: compare

=============
Core Matchers
=============

When a :mod:`compare` matcher is registered, it is simply attached to 
the :class:`Expr` class. The matcher may then be accessed through the 
:func:`expect` function/starter.


The `Expr` class
================

.. autoclass:: Expr
    

Basic matchers
==============

Compare ships with some generic/base matchers that focus on handling 
simple comparisons. If you need use-case specific matchers, it is very 
easy to create and attach your own matcher to the :class:`Expr` class. 
In fact you are encouraged to create custom matchers since they make your 
assertions more readable and concise.

Here are the matchers that are available by default:

.. automethod:: Expr.to_be
.. automethod:: Expr.to_return
.. automethod:: Expr.to_equal
