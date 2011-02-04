=============
API reference
=============

compare module
==============

.. automodule:: compare


Main exports
------------

.. autodata:: expect
.. autofunction:: matcher


Basic matchers
--------------

Compare ships with some generic/base matchers that focus on handling 
simple comparisons. If you need use-case specific matchers, it is very 
easy to create and attach your own matcher to the Expr class. In fact 
you are encouraged to create custom matchers since they make your 
assertions more readable and concise.

Here are the matchers that are available by default:

.. class:: Expr

    .. automethod:: to_be
    .. automethod:: to_return
    .. automethod:: to_equal


Core components
---------------

.. autoclass:: Expr
.. autoclass:: UnmetExpectation


Utility functions
-----------------

.. autofunction:: ensure
