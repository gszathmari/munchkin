# -*- coding: utf-8 -*-

import itertools

def diagonal(card):
    """ If the password from the card is read diagonally """
    diagonals = []
    for i in range(card.rows * -1, card.columns):
        diagonals.append(card.m.diagonal(offset=i).tolist()[0])
    results = list(itertools.chain.from_iterable(diagonals))
    return results
