# -*- coding: utf-8 -*-

import munchkin
import munchkin.core.strategies as strategies

from nose.tools import *
from munchkin.core.card import Card
from args import Args

args = Args()
card = Card(args)

def setup():
    card.generate_password_card()

def test_rows_and_columns():
    eq_(card.rows, 8)
    eq_(card.columns, 29)

def test_print_card():
    ok_("+-------------- 1 --------------+" in card.print_card)
    ok_("|                               |" in card.print_card)
    ok_("| reEPzAChZQVD2p4XGrVCVG9TLhWEa |" in card.print_card)
    ok_("| nUDcvWmxWY6pxnj7fBkML8SaBqN2P |" in card.print_card)
    ok_("| Dh6EGA67xud8R2Dwnhy6aTNr4cj5X |" in card.print_card)
    ok_("| qrp2nCmcRLFvtZnxWhKQ3bq3Rsxvw |" in card.print_card)
    ok_("| mcUcrY6GYr8QSyrePvkgsRWRxKBYG |" in card.print_card)
    ok_("| 2877gzYz7ujCMs6wt3KmsQSqzUvq9 |" in card.print_card)
    ok_("| Yme4MXNQU8qUfHmCDz6JnSQYuvLsL |" in card.print_card)
    ok_("| EphFJDHnL8DaJra54RwZ8yaYPWMyK |" in card.print_card)
    ok_("+------------- 8x29 ------------+" in card.print_card)

def test_left_to_right():
    chars = strategies.left_to_right(card.m)
    stream = ''.join(chars)
    ok_("WEanUD" in stream)
    ok_("sLEphF" in stream)

def test_right_to_left():
    chars = strategies.right_to_left(card.m)
    stream = ''.join(chars)
    ok_("hpELsL" in stream)
    ok_("hDP2Nq" in stream)

def test_top_to_down():
    chars = strategies.top_to_down(card.m)
    stream = ''.join(chars)
    ok_("D6pU7ehPcE" in stream)
    ok_("LME25v" in stream)

def test_bottom_to_top():
    chars = strategies.bottom_to_top(card.m)
    stream = ''.join(chars)
    ok_("XPaysqY" in stream)
    ok_("6V88ur" in stream)

def test_zig_zag():
    chars = strategies.zig_zag(card.m)
    stream = ''.join(chars)
    ok_("4cj5Xwvx" in stream)
    ok_("7782Yme4" in stream)

def test_zig_zag_reverse():
    chars = strategies.zig_zag_reverse(card.m)
    stream = ''.join(chars)
    ok_("uvLsL9qvU" in stream)
    ok_("vcDUnreEPzAC" in stream)

def test_diagonal():
    chars = strategies.diagonal(card.m, card.rows, card.columns)
    stream = ''.join(chars)
    ok_("Yp2mhm8eFq" in stream)
    ok_("cxY9Lq" in stream)
    ok_("pRZrwD" in stream)

def test_angled():
    streams = strategies.angled(card.m, card.rows)
    ok_("TLhWEaPXwG9LK" in ''.join(streams[0]))
    ok_("RxKBYG9LK" in ''.join(streams[4]))
    ok_("SQYuvLsLK" in ''.join(streams[6]))

def test_symbols():
    card = Card(args)
    card.generate_password_card(symbols=True)
    ok_('kUBcYW}x[Yjp>nx7(BsMu89aFqP2)' in card.print_card)
    ok_('NmH42XeQH8vU4HNC%zvJJSjY{vEs/' in card.print_card)

def test_digits():
    card = Card(args)
    card.generate_password_card(digits=True)
    ok_('reEPzAChZQVD2p4XGrVCVG9TLhWEa' in card.print_card)
    ok_('30952342371574779679361685782' in card.print_card)

def test_symbols_and_digits():
    card = Card(args)
    card.generate_password_card(symbols=True, digits=True)
    ok_('kUBcYW}x[Yjp>nx7(BsMu89aFqP2)' in card.print_card)
    ok_('50069984619897882679198841295' in card.print_card)
