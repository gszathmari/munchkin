# -*- coding: utf-8 -*-

import munchkin

from nose.tools import *
from munchkin.card import Card
from args import Args

args = Args()
custom_card_data = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['Q', 'w', 'e', 'r', 't', 'Y', 'u'],
    ['9', '8', '7', '6', '5', '4', '3']
]
password_card = Card(args)
custom_card = Card(args)

def setup():
    password_card.generate_password_card()
    custom_card.generate_custom_card(custom_card_data)

def test_password_card_rows_and_columns():
    eq_(password_card.rows, 8)
    eq_(password_card.columns, 29)

def test_password_card_print_card():
    ok_("+-------------- 1 --------------+" in password_card.m)
    ok_("|                               |" in password_card.m)
    ok_("| reEPzAChZQVD2p4XGrVCVG9TLhWEa |" in password_card.m)
    ok_("| nUDcvWmxWY6pxnj7fBkML8SaBqN2P |" in password_card.m)
    ok_("| Dh6EGA67xud8R2Dwnhy6aTNr4cj5X |" in password_card.m)
    ok_("| qrp2nCmcRLFvtZnxWhKQ3bq3Rsxvw |" in password_card.m)
    ok_("| mcUcrY6GYr8QSyrePvkgsRWRxKBYG |" in password_card.m)
    ok_("| 2877gzYz7ujCMs6wt3KmsQSqzUvq9 |" in password_card.m)
    ok_("| Yme4MXNQU8qUfHmCDz6JnSQYuvLsL |" in password_card.m)
    ok_("| EphFJDHnL8DaJra54RwZ8yaYPWMyK |" in password_card.m)
    ok_("+------------- 8x29 ------------+" in password_card.m)

def test_custom_card_rows_and_columns():
    eq_(custom_card.rows, 4)
    eq_(custom_card.columns, 7)

def test_custom_card_print_card():
    ok_("| abcdefg |" in custom_card.m)
    ok_("| 1234567 |" in custom_card.m)
    ok_("| QwertYu |" in custom_card.m)
    ok_("| 9876543 |" in custom_card.m)
    ok_("|         |" in custom_card.m)
    ok_("+-- 4x7 --+" in custom_card.m)
