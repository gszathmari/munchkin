# -*- coding: utf-8 -*-

import munchkin

from nose.tools import *
from munchkin.card import Card
from args import Args

args = Args()
card = Card(args)

def setup():
    card.generate_password_card()

def test_rows_and_columns():
    eq_(card.rows, 8)
    eq_(card.columns, 29)

def test_print_card():
    ok_("+-------------- 1 --------------+" in card.m)
    ok_("|                               |" in card.m)
    ok_("| reEPzAChZQVD2p4XGrVCVG9TLhWEa |" in card.m)
    ok_("| nUDcvWmxWY6pxnj7fBkML8SaBqN2P |" in card.m)
    ok_("| Dh6EGA67xud8R2Dwnhy6aTNr4cj5X |" in card.m)
    ok_("| qrp2nCmcRLFvtZnxWhKQ3bq3Rsxvw |" in card.m)
    ok_("| mcUcrY6GYr8QSyrePvkgsRWRxKBYG |" in card.m)
    ok_("| 2877gzYz7ujCMs6wt3KmsQSqzUvq9 |" in card.m)
    ok_("| Yme4MXNQU8qUfHmCDz6JnSQYuvLsL |" in card.m)
    ok_("| EphFJDHnL8DaJra54RwZ8yaYPWMyK |" in card.m)
    ok_("+------------- 8x29 ------------+" in card.m)

def test_left_to_right():
    chars = card._left_to_right()
    stream = ''.join(chars)
    ok_("WEanUD" in stream)
    ok_("sLEphF" in stream)

def test_right_to_left():
    chars = card._right_to_left()
    stream = ''.join(chars)
    ok_("hpELsL" in stream)
    ok_("hDP2Nq" in stream)

def test_top_to_down():
    chars = card._top_to_down()
    stream = ''.join(chars)
    ok_("D6pU7ehPcE" in stream)
    ok_("LME25v" in stream)

def test_bottom_to_top():
    chars = card._bottom_to_top()
    stream = ''.join(chars)
    ok_("XPaysqY" in stream)
    ok_("6V88ur" in stream)

def test_zig_zag():
    chars = card._zig_zag()
    stream = ''.join(chars)
    ok_("4cj5Xwvx" in stream)
    ok_("7782Yme4" in stream)

def test_zig_zag_reverse():
    chars = card._zig_zag_reverse()
    stream = ''.join(chars)
    ok_("uvLsL9qvU" in stream)
    ok_("vcDUnreEPzAC" in stream)

def test_diagonal():
    chars = card._diagonal()
    stream = ''.join(chars)
    ok_("Yp2mhm8eFq" in stream)
    ok_("cxY9Lq" in stream)
    ok_("pRZrwD" in stream)

def test_symbols():
    card = Card(args)
    card.generate_password_card(symbols=True)
    ok_('kUBcYW}x[Yjp>nx7(BsMu89aFqP2)' in card.m)
    ok_('NmH42XeQH8vU4HNC%zvJJSjY{vEs/' in card.m)

def test_digits():
    card = Card(args)
    card.generate_password_card(digits=True)
    ok_('reEPzAChZQVD2p4XGrVCVG9TLhWEa' in card.m)
    ok_('30952342371574779679361685782' in card.m)

def test_symbols_and_digits():
    card = Card(args)
    card.generate_password_card(symbols=True, digits=True)
    ok_('kUBcYW}x[Yjp>nx7(BsMu89aFqP2)' in card.m)
    ok_('50069984619897882679198841295' in card.m)
