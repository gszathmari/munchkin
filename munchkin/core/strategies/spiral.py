# -*- coding: utf-8 -*-

def generate_spiral_stream(card, rows, columns, posX=0, posY=0):
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
    results = []
    # Cycle through all postitions on the card
    for i in range(0, rows):
        for j in range(0, columns):
            stream = generate_spiral_stream(card, rows, columns, i, j)
            results.append(stream)
    return results
