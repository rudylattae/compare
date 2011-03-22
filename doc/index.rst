.. compare documentation master file, created by
   sphinx-quickstart on Wed Feb 02 21:16:08 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _compare source: https://github.com/rudylattae/compare
.. _Jasmine BDD: http://pivotal.github.com/jasmine
.. _PySpec: http://pyspec.codeplex.com/
.. _should-dsl: http://www.should-dsl.info/

====================================================
Compare : alternative syntax for your Python asserts
====================================================

::

    expect(`your expectations`).to_be_met()

You get the idea...


Updates
=======

.. toctree::
   :maxdepth: 2
   
   releases


.. include:: ../README.rst


User guide
==========

.. toctree::
   :maxdepth: 1
   
   usage/get-started
   usage/managing-expectations
   usage/not
   usage/custom-matchers


API reference
=============

.. toctree::
   :maxdepth: 2

   core-api
   core-matchers


Contribute
==========

To contribute to the project, fork the `compare source`_, make your modifications 
and create a pull request. I'll be more than happy to merge in your work.

Please ensure that you provide supporting specs for your contribution. Also if you are 
creating a new feature or fixing a bug, I encourage you to create an issue for it 
in order to minimize duplication of effort.


Acknowledgements
================

The expect syntax used in compare was inspired by and/or builds on ideas from:

* `Jasmine BDD`_ 
* `PySpec`_
* `should-dsl`_


License
=======

The compare code and documentation are released to the general public under the BSD Licence.

.. include:: ../LICENSE.txt


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

