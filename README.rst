########
munchkin
########

Wordlist generator based on password cards

Munchkin generates a possible combinations of passwords from a password card

.. image:: https://codeclimate.com/github/gszathmari/munchkin/badges/gpa.svg
   :target: https://codeclimate.com/github/gszathmari/munchkin
   :alt: Code Climate

What is a password card?
========================

Password (aka. grid) card is a physical card that allows you to memorize your
passwords easier.

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/docs/images/password_card.png
  :scale: 40
  :alt: Password Card

The card contains a block of random alphanumeric characters. You just need to
choose and memorize a row, a column and a direction to pick a password from the
card.

Security
--------

Passwords cards heavily rely on physical security. The card should be kept in
your wallet or pocket, far away from watchful eyes around you.

In case the card is lost or recorded with a camera (e.g. CCTV), your password
shall be considered as compromised and changed immediately.

Features
========

Munchkin can generate wordlists from compromised password cards.

This utility generates potential passwords and dumps them onto the screen or
into a text file.

Supported Strategies
--------------------

Munchkin can generate passwords based on the following card reading strategies.

Left to right
^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/docs/images/left-to-right.png
   :scale: 20
   :alt: Left to Right

Right to left
^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/docs/images/right-to-left.png
   :scale: 20
   :alt: Right to Left

Top down
^^^^^^^^

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/docs/images/top-down.png
   :scale: 20
   :alt: Top Down

Bottom up
^^^^^^^^^

.. image:: https://raw.githubusercontent.com/gszathmari/munchkin/docs/images/bottom-up.png
   :scale: 20
   :alt: Bottom Up

Supported Cards
---------------

* Cards from http://passwordcard.org
* Any user-supplied custom card

Usage Instructions
==================

Munchkin has two operation modes: one is for generating passwords based on cards
from http://passwordcard.org, and the other is for user supplied custom cards.

Operation Modes
---------------

passwordcard.org Cards
^^^^^^^^^^^^^^^^^^^^^^

Use the ``pcard`` selector to generate passwords from passwordcard.org cards ::

  $ munchkin pcard -h

This selector recognises the following options:

  -s str, --seed str  card number (e.g. *7eb3fbfa560d1d1e*)
  --symbols           include symbols (**broken**)
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

Contributors
============

* Gabor Szathmari - `@gszathmari`_

.. _@gszathmari: https://www.twitter.com/gszathmari

Credits
=======

* Python port of passwordcard.org algorithm: `olasd/passwordcard`_

.. _olasd/passwordcard: https://github.com/olasd/passwordcard
