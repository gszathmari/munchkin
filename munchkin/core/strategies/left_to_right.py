# -*- coding: utf-8 -*-

def left_to_right(card):
    """ If the password from the card is read from left to right """
    data = card.m.getA1().flatten()
    results = data.tolist()
    return results
