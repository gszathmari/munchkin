# -*- coding: utf-8 -*-

import itertools

def diagonal(card, rows, columns):
    """ If the password from the card is read diagonally """
    diagonals = []
    for i in range(rows * -1, columns):
        diagonals.append(card.diagonal(offset=i).tolist()[0])
    results = list(itertools.chain.from_iterable(diagonals))
    return results
