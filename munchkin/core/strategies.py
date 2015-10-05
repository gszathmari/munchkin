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

def _generate_spiral_stream(card, rows, columns, posX=0, posY=0):
    """Generate spiral from a selected location on the card"""
    x = y = 0
    dx, dy = 0, -1
    data = []
    matrix = card.tolist()

    for i in range(max(rows, columns) ** 2):
        if (-rows / 2 < x <= rows / 2) and (-columns / 2 < y <= columns / 2):
            # Select starting position
            row = y + posX
            column = x + posY
            # Return results if we hit the wall
            if (row == -1) or (column == -1) or (row == rows) or (column == columns):
                return ''.join(data)
            # Add next character to array
            else:
                data.append(str(matrix[row][column]))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

def spiral(card, rows, columns):
    """If the password is read in a spiral shape from the card"""
    data = []
    # Cycle through all postitions on the card
    for i in range(0, rows):
        for j in range(0, columns):
            stream = _generate_spiral_stream(card, rows, columns, i, j)
            data.append(stream)
    return data
