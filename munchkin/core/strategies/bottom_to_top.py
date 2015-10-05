# -*- coding: utf-8 -*-

def bottom_to_top(card):
    """ If the password from the card is read from bottom to up """
    data = card.m.getT().getA1().flatten()
    results = data.tolist()
    results.reverse()
    return results
