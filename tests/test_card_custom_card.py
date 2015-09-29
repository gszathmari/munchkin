# -*- coding: utf-8 -*-

import munchkin

from nose.tools import *
from munchkin.core.card import Card
from args import Args

args = Args()
card_data = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['Q', 'w', 'e', 'r', 't', 'Y', 'u'],
    ['9', '8', '7', '6', '5', '4', '3']
]
custom_card = Card(args)

def setup():
    custom_card.generate_custom_card(card_data)

def test_rows_and_columns():
    eq_(custom_card.rows, 4)
    eq_(custom_card.columns, 7)

def test_print_card():
    ok_("| abcdefg |" in custom_card.print_card)
    ok_("| 1234567 |" in custom_card.print_card)
    ok_("| QwertYu |" in custom_card.print_card)
    ok_("| 9876543 |" in custom_card.print_card)
    ok_("|         |" in custom_card.print_card)
    ok_("+-- 4x7 --+" in custom_card.print_card)
