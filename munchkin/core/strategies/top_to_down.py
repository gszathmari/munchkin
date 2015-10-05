# -*- coding: utf-8 -*-

def top_to_down(card):
    """ If the password from the card is read from top to down """
    data = card.m.getT().getA1().flatten()
    results = data.tolist()
    return results
