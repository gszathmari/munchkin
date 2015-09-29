########
munchkin
########

Wordlist generator based on password cards

.. image:: https://img.shields.io/travis/gszathmari/munchkin.svg
    :target: https://travis-ci.org/gszathmari/munchkin
    :alt: Travis CI

.. image:: https://img.shields.io/codacy/3f42d3ee8060406d81e77dc6274bb671.svg
   :target: https://www.codacy.com/app/gszathmari/munchkin
   :alt: Codacy

.. image:: https://www.quantifiedcode.com/api/v1/project/c42903be20d644809c9c87c9b8c6b81f/badge.svg
   :target: https://www.quantifiedcode.com/app/project/c42903be20d644809c9c87c9b8c6b81f
   :alt: QuantifiedCode

.. image:: https://img.shields.io/pypi/dm/munchkin.svg
   :target: https://pypi.python.org/pypi/munchkin
   :alt: PyPI

.. image:: https://img.shields.io/requires/github/gszathmari/munchkin.svg
   :target: https://requires.io/github/gszathmari/munchkin/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://img.shields.io/pypi/pyversions/munchkin.svg
   :alt: Python Versions

What is a password card?
========================

Password (aka. grid) card is a physical card that allows you to memorize your
passwords easier.

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/master/docs/images/password_card.png
  :alt: Password Card

The card contains a block of random alphanumeric characters. You just need to
choose and memorize a row, a column and a direction to pick a password from the
card.

Security
--------

Passwords cards heavily rely on physical security. The card should be kept in
your wallet or pocket, far away from watchful eyes around you.

In case the card is lost or recorded with a camera (e.g. CCTV), your password
is compromised therefore it should be changed immediately.

Features
========

Munchkin can generate wordlists from compromised password cards.

This utility generates potential passwords and dumps them onto the screen or
into a text file. The list of passwords can be used for brute-force attacks.

Supported Strategies
--------------------

Passwords from a password card can be chosen by the user based on different
strategies. He or she might read passwords from left to right, top to down or
diagonally.

Munchkin can generate passwords based on the most common card reading
strategies. The followings are samples only.

Left to Right
^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/master/docs/images/left-to-right.png
   :alt: Left to Right

Top Down
^^^^^^^^

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/master/docs/images/top-down.png
   :alt: Top Down

Refer to the documentation for a comprehensive list of `password generating strategies`_.

.. _password generating strategies: https://github.com/gszathmari/munchkin/blob/master/docs/strategies.rst

Supported Cards
---------------

* Cards from http://passwordcard.org
* Any user-supplied custom card

Installing Munchkin
===================

The latest package is available on `PyPI`_ ::

  $ pip install munchkin

.. _PyPI: https://pypi.python.org/pypi/munchkin

Requirements
------------

This utility only runs on Python *2.6.x* and *2.7.x*

Usage Instructions
==================

The following section explains the basic usage of Munchkin. You can also use
the ``-h`` switch for getting more information on the individual features.

Operation Modes
---------------

There are two operation modes available. The first one generates cards similar
to the ones from http://passwordcard.org, and the second allows to bring your
own password cards.

passwordcard.org Cards
^^^^^^^^^^^^^^^^^^^^^^

Use the ``pcard`` selector to generate passwords from passwordcard.org cards ::

  $ munchkin pcard -h

This selector recognises the following options:

  -s str, --seed str  card number (e.g. *7eb3fbfa560d1d1e*)
  --symbols           include symbols
  --digits            incude digits

Custom Cards
^^^^^^^^^^^^

The ``custom`` selector allows to supply password cards by pasting them as a
block of text ::

  $ munchkin custom -h

This selector does not require any special options.

Settings
--------

The following switches are recognized for both card types

Password Length
^^^^^^^^^^^^^^^

Choose the minimum and maximum length of passwords to generate:

  --minlen num  minimum password length (*default: 6*)
  --maxlen num  maximum password length (*default: 12*)

Read Strategies
^^^^^^^^^^^^^^^

Select one or more strategies to generate passwords (refer
to `Supported Strategies`_ section for further explanation)

  -l, --left-to-right   Left to right
  -r, --right-to-left   Right to left
  -t, --top-down        Top left corner to bottom right
  -b, --bottom-up       Bottom right corner to top left

File Output
^^^^^^^^^^^

Dump passwords to a file instead of the terminal:

  -f name, --file name  Dump passwords to file

Examples
--------

Generate 6-8 digit passwords from a password card generated with seed the
initial seed of *7eb3fbfa560d1d1e* ::

  $ munchkin pcard -s 7eb3fbfa560d1d1e -l

Supply your own password card and generate passwords with multiple read
strategies ::

  $ munchkin custom -l -r -t -b

Links
=====

* `Source code on GitHub`_
* `Package on PyPI`_

.. _Source code on GitHub: https://github.com/gszathmari/munchkin
.. _Package on PyPI: https://pypi.python.org/pypi/munchkin

Contributors
============

* Gabor Szathmari - `@gszathmari`_

.. _@gszathmari: https://www.twitter.com/gszathmari

Credits
=======

* Python port of passwordcard.org algorithm: `olasd/passwordcard`_

.. _olasd/passwordcard: https://github.com/olasd/passwordcard
