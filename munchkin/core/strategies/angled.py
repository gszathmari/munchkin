# -*- coding: utf-8 -*-

def angled(card, rows):
    """ If the password from the card is read in a rotated 'L' shape """
    results = []
    for i in range(0, rows-1):
        # Select a row
        stream = card[i].tolist()[0]
        # Select last elements from each row below
        for j in range(i+1, rows):
            stream.append(card[j].tolist()[0][-1])
        results.append(stream)
    return results
