# -*- coding: utf-8 -*-

import munchkin
from munchkin.core.strategies.left_to_right import left_to_right
from munchkin.core.strategies.right_to_left import right_to_left
from munchkin.core.strategies.top_to_down import top_to_down
from munchkin.core.strategies.bottom_to_top import bottom_to_top
from munchkin.core.strategies.zig_zag import zig_zag
from munchkin.core.strategies.zig_zag_reverse import zig_zag_reverse
from munchkin.core.strategies.diagonal import diagonal
from munchkin.core.strategies.angled import angled
from munchkin.core.strategies.spiral import spiral


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
    chars = left_to_right(card)
    stream = ''.join(chars)
    ok_("WEanUD" in stream)
    ok_("sLEphF" in stream)

def test_right_to_left():
    chars = right_to_left(card)
    stream = ''.join(chars)
    ok_("hpELsL" in stream)
    ok_("hDP2Nq" in stream)

def test_top_to_down():
    chars = top_to_down(card)
    stream = ''.join(chars)
    ok_("D6pU7ehPcE" in stream)
    ok_("LME25v" in stream)

def test_bottom_to_top():
    chars = bottom_to_top(card)
    stream = ''.join(chars)
    ok_("XPaysqY" in stream)
    ok_("6V88ur" in stream)

def test_zig_zag():
    chars = zig_zag(card)
    stream = ''.join(chars)
    ok_("4cj5Xwvx" in stream)
    ok_("7782Yme4" in stream)

def test_zig_zag_reverse():
    chars = zig_zag_reverse(card)
    stream = ''.join(chars)
    ok_("uvLsL9qvU" in stream)
    ok_("vcDUnreEPzAC" in stream)

def test_diagonal():
    chars = diagonal(card)
    stream = ''.join(chars)
    ok_("Yp2mhm8eFq" in stream)
    ok_("cxY9Lq" in stream)
    ok_("pRZrwD" in stream)

def test_angled():
    streams = angled(card)
    ok_("TLhWEaPXwG9LK" in ''.join(streams[0]))
    ok_("RxKBYG9LK" in ''.join(streams[4]))
    ok_("SQYuvLsLK" in ''.join(streams[6]))

def test_spiral():
    streams = spiral(card)
    ok_("pxR8d6VD2pn2ZtvFLuYQ" in streams)
    ok_("kgmK3vhKQ3ssnJ6zDtPWnhy6aTbRQSy8ZwR45Cwexw7fBkML8SNqWSQa" in streams)

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
