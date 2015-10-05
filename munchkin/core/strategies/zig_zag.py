# -*- coding: utf-8 -*-

import itertools

def zig_zag(card):
    """ If the password from the card is read in zig-zag directions """
    rows = card.m.getA().tolist()
    for i in range(len(rows)):
        # Reverse order on every second line
        if i % 2 <> 0:
            rows[i].reverse()
    # Flatten list
    results = list(itertools.chain.from_iterable(rows))
    return results
