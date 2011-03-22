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

The primary focus of compare is to keep you in the 
"specification by example" mindset. The general flow for creating an example 
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

When practicing TDD/BDD/ATDD/Specification by example, you will notice 
that the biggest win comes neither from "100% code coverage" 
nor having a "green build". On the contrary, your automated unit or 
acceptance tests are at their best when you have a broken build! 

Why? The end-goal of writing "tests" before you write code is to build
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

