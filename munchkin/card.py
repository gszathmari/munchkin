# -*- coding: utf-8 -*-

import logging
import sys
import itertools
import numpy as np

from passwordcard import passwordcard

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

class Card:
    def __init__(self, args):
        # Store card as matrix
        self._m = None
        # Stores password streams generated from the card
        self._args = vars(args)
        self._seed = self._args.get('seed')
        self._header = None

    # Validates custom cards supplied by the user
    def _validate_matrix(self, m):
        try:
            matrix = np.matrix(m)
        except:
            logging.error("Invalid password card format")
            sys.exit(2)

        # Check whether each line of matrix is equal
        for i in range(0, len(m)-1):
            if not len(m[i]) == len(m[i+1]):
                logging.error("Invalid password card format")
                sys.exit(2)
        else:
            return matrix

    # --------------------------------------------------------
    #
    # Stream generators
    #
    # --------------------------------------------------------

    # If the password from the card is read from left to right
    def _left_to_right(self):
        data = self._m.getA1().flatten()
        return data.tolist()

    # If the password from the card is read from right to left
    def _right_to_left(self):
        data = self._left_to_right()
        data.reverse()
        return data

    # If the password from the card is read from top to down
    def _top_to_down(self):
        data = self._m.getT().getA1().flatten()
        return data.tolist()

    # If the password from the card is read from bottom to up
    def _bottom_to_top(self):
        data = self._top_to_down()
        data.reverse()
        return data

    def _zig_zag(self):
        rows = self._m.getA().tolist()
        for i in range(len(rows)):
            # Reverse order on every second line
            if i % 2 <> 0:
                rows[i].reverse()
        # Flatten list
        data = list(itertools.chain.from_iterable(rows))
        return data

    def _zig_zag_reverse(self):
        rows = self._m.getA().tolist()
        rows.reverse()
        for i in range(len(rows)):
            # Reverse order on every second line
            if i % 2 == 0:
                rows[i].reverse()
        # Flatten list
        data = list(itertools.chain.from_iterable(rows))
        return data

    def _diagonal(self):
        diagonals = []
        for i in range(self.rows * -1, self.columns):
            diagonals.append(self._m.diagonal(offset=i).tolist()[0])
        data = list(itertools.chain.from_iterable(diagonals))
        return data

    # --------------------------------------------------------

    # Adds appropriate character streams based on the selected card reading strategies
    def _generate_data_streams(self):
        streams = []
        if self._args.get('left_to_right') or self._args.get('all'):
            streams.append(self._left_to_right())
        if self._args.get('right_to_left') or self._args.get('all'):
            streams.append(self._right_to_left())
        if self._args.get('top_down') or self._args.get('all'):
            streams.append(self._top_to_down())
        if self._args.get('bottom_up') or self._args.get('all'):
            streams.append(self._bottom_to_top())
        if self._args.get('zig_zag') or self._args.get('all'):
            streams.append(self._zig_zag())
        if self._args.get('zig_zag_reverse') or self._args.get('all'):
            streams.append(self._zig_zag_reverse())
        if self._args.get('diagonal') or self._args.get('all'):
            streams.append(self._diagonal())
        return streams

    # Generator that dumps the passwords for each card read strategy
    def _passwords_generator(self, streams, pwlen):
        # Iterate through streams (strategies)
        for stream in streams:
            counter = 0
            # Generate passwords with certain length from the card
            while counter+pwlen < len(stream)+1:
                result = stream[counter:counter+pwlen]
                # Return result back
                yield ''.join(result)
                counter += 1

    # Generate password card as on http://passwordcard.org
    def generate_password_card(self, digits=False, symbols=False):
        m = []
        # Generate card
        header, card = passwordcard.generate_card(self._seed, digits=digits, symbols=symbols)
        # Add lists to a list and generate matrix from that with NumPy
        for row in card:
            m.append(list(row))
        # Validate and generate matrix with NumPy
        self._m = self._validate_matrix(m)
        self._header = header
        # Save card dimensions
        return self._m

    # Generates custom password card
    def generate_custom_card(self, m):
        # Validate and generate matrix with NumPy
        self._m = self._validate_matrix(m)
        # Save card dimensions
        return self._m

    # Get number of password card rows
    @property
    def rows(self):
        return self._m.shape[0]

    # Get number of password card columns
    @property
    def columns(self):
        return self._m.shape[1]

    # Generates fancy password card box
    @property
    def m(self):
        output = []
        # Assign text header
        try:
            # Display seed in case of passwordcard.org cards
            header = " %s " % self._seed
        except AttributeError:
            # Display generic title for custom cards
            header = " PASSWORD CARD "
        # Verify wether card is wide enough to display header text
        if len(header)+2 > self.columns:
            # Box is too narrow, do not add text header
            top = "+-" + ("-" * self.columns) + "-+\r"
        else:
            # Add text header
            top = "+-%s-+\r" % header.center(self.columns, "-")
        output.append(top)
        # Add empty line between top and body
        empty_line = "| " + (" " * self.columns) + " |"
        output.append(empty_line)
        # Add header of symbols if card is from passwordcard.org
        if self._header:
            row = "| %s |" % self._header.center(self.columns)
            output.append(row)
            output.append(empty_line)
        # Add password card body
        for i in range(len(self._m)):
            row = ''.join(self._m.tolist()[i])
            row = "| %s |" % row.center(self.columns)
            output.append(row)
        # Add empty line between body and bottom
        output.append(empty_line)
        # Add bottom with password card dimensions
        dimensions = " %sx%s " % (self.rows, self.columns)
        bottom = "+%s+\r" % dimensions.center(self.columns+2, "-")
        output.append(bottom)
        output.append("\r")
        # Return full box with password card as the output
        return '\r\n'.join(output)

    # Dumps passwords from the password card
    @property
    def passwords(self):
        # Generate streams based on the card read strategies
        streams = self._generate_data_streams()
        # Iterate through all password lengths between minimum and maximum
        for pwlen in range(int(self._args.get('minlen')), int(self._args.get('maxlen'))+1):
            # Dump password on the screen constructed by the generator above
            for password in self._passwords_generator(streams, pwlen):
                yield password
