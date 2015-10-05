# -*- coding: utf-8 -*-

def right_to_left(card):
    """ If the password from the card is read from right to left """
    data = card.m.getA1().flatten()
    results = data.tolist()
    results.reverse()
    return results
