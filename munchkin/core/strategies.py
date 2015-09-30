# -*- coding: utf-8 -*-

import itertools

def left_to_right(card):
    """ If the password from the card is read from left to right """
    data = card.getA1().flatten()
    return data.tolist()

def right_to_left(card):
    """ If the password from the card is read from right to left """
    data = left_to_right(card)
    data.reverse()
    return data

def top_to_down(card):
    """ If the password from the card is read from top to down """
    data = card.getT().getA1().flatten()
    return data.tolist()

def bottom_to_top(card):
    """ If the password from the card is read from bottom to up """
    data = top_to_down(card)
    data.reverse()
    return data

def zig_zag(card):
    """ If the password from the card is read in zig-zag directions """
    rows = card.getA().tolist()
    for i in range(len(rows)):
        # Reverse order on every second line
        if i % 2 <> 0:
            rows[i].reverse()
    # Flatten list
    data = list(itertools.chain.from_iterable(rows))
    return data

def zig_zag_reverse(card):
    """ If the password from the card is read in reverse zig-zag directions """
    rows = card.getA().tolist()
    rows.reverse()
    for i in range(len(rows)):
        # Reverse order on every second line
        if i % 2 == 0:
            rows[i].reverse()
    # Flatten list
    data = list(itertools.chain.from_iterable(rows))
    return data

def diagonal(card, rows, columns):
    """ If the password from the card is read diagonally """
    diagonals = []
    for i in range(rows * -1, columns):
        diagonals.append(card.diagonal(offset=i).tolist()[0])
    data = list(itertools.chain.from_iterable(diagonals))
    return data

def angled(card, rows):
    """ If the password from the card is read in a rotated 'L' shape """
    data = []
    for i in range(0, rows-1):
        # Select a row
        stream = card[i].tolist()[0]
        # Select last elements from each row below
        for j in range(i+1, rows):
            stream.append(card[j].tolist()[0][-1])
        data.append(stream)
    return data
