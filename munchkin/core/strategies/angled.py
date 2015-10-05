# -*- coding: utf-8 -*-

def angled(card):
    """ If the password from the card is read in a rotated 'L' shape """
    results = []
    for i in range(0, card.rows - 1):
        # Select a row
        stream = card.m[i].tolist()[0]
        # Select last elements from each row below
        for j in range(i+1, card.rows):
            stream.append(card.m[j].tolist()[0][-1])
        results.append(stream)
    return results
