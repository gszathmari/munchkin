# -*- coding: utf-8 -*-

import munchkin

from nose.tools import *
from munchkin.card import Card
from args import Args

def left_to_right():
    args = Args()
    card = Card(args)
    output = munchkin.generate_card_pcard(args, card)
    print(output)
    raise
