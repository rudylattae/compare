.. currentmodule:: compare

=============
Core Matchers
=============

When a :mod:`compare` matcher is registered, it is simply attached to 
the :class:`Expr` class. The matcher may then be accessed through the 
:func:`expect` function/starter.

Compare ships with some generic/base matchers that focus on handling 
simple comparisons. If you need use-case specific matchers, it is very 
easy to create and attach your own matcher to the :class:`Expr` class. 
In fact you are encouraged to create custom matchers since they make your 
assertions more readable and concise.

Here are the matchers that are available by default:


`to_equal`
==========
.. automethod:: Expr.to_equal

`to_be`
=======
.. automethod:: Expr.to_be

`to_return`
===========
.. automethod:: Expr.to_return

`to_raise`
==========
.. automethod:: Expr.to_raise

`to_be_none`
============
.. automethod:: Expr.to_be_none

`to_be_truthy`
==============
.. automethod:: Expr.to_be_truthy

`to_be_falsy`
=============
.. automethod:: Expr.to_be_falsy
