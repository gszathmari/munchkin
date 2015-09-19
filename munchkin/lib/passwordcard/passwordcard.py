#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# passwordcard - A passwordcard generator compatible with passwordcard.org
#
# Copyright © 2012 Nicolas Dandrimont <nicolas.dandrimont@crans.org>
#
#   This file is part of PasswordCard.
#
#   PasswordCard is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import javarandom

CHARSETS = {
    'original.digits': u"0123456789",
    'original.alphanumeric': u"23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ",
    'original.alphanumeric_with_symbols': u"23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ@#$%&*<>?€+{}[]()/\\"
    }

HEADERS = {
    'original': u"■□▲△○●★☂☀☁☹☺♠♣♥♦♫€¥£$!?¡¿⊙◐◩�",
    }

# Construct the appropriate character sets
def generate_character_sets(symbols, digits):
    characters = {}
    # Select characters for the card
    if symbols and not digits:
        characters['top_odd'] = list(CHARSETS['original.alphanumeric'])
        characters['top_even'] = list(CHARSETS['original.alphanumeric_with_symbols'])
        characters['bottom_odd'] = list(CHARSETS['original.alphanumeric'])
        characters['bottom_even'] = list(CHARSETS['original.alphanumeric_with_symbols'])
    elif symbols and digits:
        characters['top_odd'] = list(CHARSETS['original.alphanumeric'])
        characters['top_even'] = list(CHARSETS['original.alphanumeric_with_symbols'])
        characters['bottom_odd'] = list(CHARSETS['original.digits'])
        characters['bottom_even'] = list(CHARSETS['original.digits'])
    elif not symbols and digits:
        characters['top_odd'] = list(CHARSETS['original.alphanumeric'])
        characters['top_even'] = list(CHARSETS['original.alphanumeric'])
        characters['bottom_odd'] = list(CHARSETS['original.digits'])
        characters['bottom_even'] = list(CHARSETS['original.digits'])
    elif not symbols and not digits:
        characters['top_odd'] = list(CHARSETS['original.alphanumeric'])
        characters['top_even'] = list(CHARSETS['original.alphanumeric'])
        characters['bottom_odd'] = list(CHARSETS['original.alphanumeric'])
        characters['bottom_even'] = list(CHARSETS['original.alphanumeric'])
    else:
        raise Exception("Cannot choose charset for password card")
    return characters

def generate_card(seed, width=29, height=8, symbols=False, digits=False):
    characters = generate_character_sets(symbols, digits)

    seed = int("0x%s" % seed, 16)

    """Generate a password card with the given parameters"""
    rng = javarandom.JavaRandom(seed)

    header = list(HEADERS['original'])

    rng.shuffle(header)

    contents = []

    midheight = 1 + (height/2)

    for i in range(1, midheight):
        line = []
        for j in range(width):
            # Even columns
            if j % 2 == 0:
                line.append(characters['top_even'][rng.next_int(len(characters['top_even']))])
            # Odd columns
            else:
                line.append(characters['top_odd'][rng.next_int(len(characters['top_odd']))])
        contents.append(u''.join(line))
    for j in range(midheight, height+1):
        line = []
        for j in range(width):
            # Even columns
            if j % 2 == 0:
                line.append(characters['bottom_even'][rng.next_int(len(characters['bottom_even']))])
            # Odd columns
            else:
                line.append(characters['bottom_odd'][rng.next_int(len(characters['bottom_odd']))])
        contents.append(u''.join(line))

    return u''.join(header), contents
