=============================
Managing (Unmet) Expectations
=============================


What is an Unmet Expectation?
===============================

When using compare, you will notice the term "Unmet Expectation" a lot.
Users coming from an xUnit background, can think of this as the  
equivalent of an "Assertion Error". You would usually run into assetion 
errors when your test code makes an assertion which fails e.g. ::

    class Person:
        def is_cool(self):
            return False
            
    class PersonTest(unittest.TestCase):
        def test_person_is_cool_by_default(self):
            joe = Person()
            self.assertTrue(joe.is_cool())

As you may have noticed, the above test will fail. The message you would 
see is something like::

    AssertionError: False is not True

Since the primary focus of compare is to keep you in the 
"specification by example" mindset, the general flow for creating an example 
is that you:

* define some **pre-conditions** for your target code
* perform an **action** or trigger an **event**
* **verify** that your code behaves appropriately under the given conditions

So based on the above philosopy, when your code behaves badly, or behaves in a manner 
you were not anticipating, compare tells you that your expectation was not met.
Thus we could recreate the example above as:: 

    ... snip ...
    expect(joe.is_cool()).to_be_true()
    
And the error message you would see is::
    
    "UnmetExpectation: Expected False to be True"

Note that the "UnmetExpectation" error, is a subclass of "AssertionError". You may 
read more about it here :class:`compare.UnmetExpectation`.


Why manage unmet expectations?
================================

The goal of writing "tests" before you write code is to build
a specification (a living documentation if you will) for the overall 
feature-set and technical design of your code. 

When you validate your software agaist the specifications (i.e. run the 
automated tests/specs), the resulting output should tell you:

* that the software meets the specs
* if it does not (i.e. a spec fails), why? 

When a spec fails, you want the resulting message to be specific yet 
provide enough contextual information so you can decide how to 
resolve the issue.

Considering the above discussion, I hope you agree that it is important to
**craft executable specifications that provide value when they fail.**

Now let's look at ways to get the most out of unmet expectations.


How to manage unmet expectations
==================================

Hint at the focus of the expectation
--------------------------------------

The base compare matchers and by extension, all custom matchers should 
aim to fail with enough contextual information to help an observer diagnose 
and potentially resolve the issue.

compare allows you to customize the output associated with unmet expectations. 
You may provide a `hint` to the matcher::


    # instead of this
    expect(joe.is_cool()).to_be_true()
    
    "UnmetExpectation: Expected False to be True"
    
The above is a basic generice failure message. It is possible to provide the 
matcher with a hint that better identifies the focus of the expectation.

    # try this
    expect(joe.is_cool()).to_be_true('joe.is_cool()')
    
    UnmetExpectation: Expected joe.is_cool() to be True but got False


Customize the failure message
-------------------------------

In certain cases you may wish to display a very specific message regarding 
the unmet expectation. To do this, provide a `fail_message` to the matcher::

    # provide a custom failure message
    expect(joe.is_cool()).to_be_true(fail_message='OMG! Joe is not cool.')
    
    UnmetExpectation: OMG! Joe is not cool.
    

Use appropriately named matchers
----------------------------------

Another way to manage unmet expectations, is to select a matcher that 
focuses a reader's attention on the behaviour being verified. Compared to 
the previous examples, you will notice that the matcher in the following 
example is more in tuse with our concern for the spec::

    # select an approprite matcher
    expect(joe.is_cool).to_return(True)
    
    UnmetExpectation: Expected callable to return True but got False
    
    # of course, you may provide a hint for clarity
    expect(joe.is_cool).to_return(True, 'joe.is_cool()')
    
    UnmetExpectation: Expected joe.is_cool() to return True but got False
    

Create custom matchers
-------------------------

One of the best ways to get the most for unmet expectations is to make sure that 
the matcher is implmented (name and code-wise) to expresses the behaviour 
you wish to describe. To this end compare makes it easy to create and (re)use 
custom matchers that handle specialized verifications.

Hopefully, the example below gives you a better idea of how a specialized matcher 
could improve the readability of your specs and provide priceless value when 
the spec fails::

    # create a custom matcher
    @matcher
    def to_be_cool(context, hint=None, msg=None):
        message = 'Expected %()s %(negate)s'
        ensure(context.is_cool(), True, message)
    
    expect(joe).to_be_cool(hint='joe')
        
The custom matcher above For more information on how to create custom matchers, please see 
:doc:`custom-matchers`.
