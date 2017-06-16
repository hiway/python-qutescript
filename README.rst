========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-qutescript/badge/?style=flat
    :target: https://readthedocs.org/projects/python-qutescript
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/hiway/python-qutescript.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/hiway/python-qutescript

.. |version| image:: https://img.shields.io/pypi/v/qutescript.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/qutescript

.. |commits-since| image:: https://img.shields.io/github/commits-since/hiway/python-qutescript/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/hiway/python-qutescript/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/qutescript.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/qutescript

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/qutescript.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/qutescript

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/qutescript.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/qutescript


.. end-badges

Painless userscripts for qutebrowser.

* Free software: BSD license

Installation
============

::

    pip install qutescript

Documentation
=============

https://python-qutescript.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
