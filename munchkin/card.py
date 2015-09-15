# -*- coding: utf-8 -*-

import logging
import sys
import numpy as np

from passwordcard import passwordcard

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

class Card:
    def __init__(self, args):
        # Store card as matrix
        self._m = None
        self._dimensions = {
            "rows": None,
            "columns": None,
        }
        # Stores password streams generated from the card
        self._streams = []
        self._patterns = {
            "left_to_right": args.left_to_right,
            "right_to_left": args.right_to_left,
            "top_down": args.top_down,
            "bottom_up": args.bottom_up
        }
        self._options = {
            "minlen": int(args.minlen),
            "maxlen": int(args.maxlen)
        }
        try:
            # Passwordcard.org seed
            self._seed = str(args.seed)
        except AttributeError:
            pass

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

    # Generate password card as on http://passwordcard.org
    def generate_password_card(self, digits=False, symbols=False):
        m = []
        width, height = 29, 8
        # Select appropriate character sets
        if symbols:
            top_charset = passwordcard.CHARSETS['original.alphanumeric_with_symbols']
        else:
            top_charset = passwordcard.CHARSETS['original.alphanumeric']
        if digits:
            bottom_charset = passwordcard.CHARSETS['original.digits']
        elif symbols:
            bottom_charset = passwordcard.CHARSETS['original.alphanumeric_with_symbols']
        else:
            bottom_charset = passwordcard.CHARSETS['original.alphanumeric']
        header = passwordcard.HEADERS['original']
        seed = int("0x%s" % self._seed, 16)
        # Generate card
        header, card = passwordcard.generate_card(seed, width, height, top_charset, bottom_charset, header)

        # Add lists to a list and generate matrix from that with NumPy
        for row in card:
            m.append(list(row))

        # Validate and generate matrix with NumPy
        self._m = self._validate_matrix(m)
        # Save card dimensions
        self._dimensions['rows'] = len(m)
        self._dimensions['columns'] = len(m[0])
        return self._m

    # Generates custom password card
    def generate_custom_card(self, m):
        # Validate and generate matrix with NumPy
        self._m = self._validate_matrix(m)
        # Save card dimensions
        self._dimensions['rows'] = len(m)
        self._dimensions['columns'] = len(m[0])
        return self._m

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

    # --------------------------------------------------------

    # Adds appropriate streams based on the selected strategies
    def _generate_data_streams(self):
        streams = []
        # In case the password is read from left to right
        if self._patterns['left_to_right'] is True:
            streams.append(self._left_to_right())
        # In case the password is read from right to left
        if self._patterns['right_to_left'] is True:
            streams.append(self._right_to_left())
        # In case the password is read from top left to bottom right
        if self._patterns['top_down'] is True:
            streams.append(self._top_to_down())
        # In case the password is read from bottom right to top left
        if self._patterns['bottom_up'] is True:
            streams.append(self._bottom_to_top())
        # Save streams
        self._streams = streams
        return streams

    # Displays card dimensions
    def _get_dimensions(self):
        data = "%sx%s" % (self._dimensions['rows'], self._dimensions['columns'])
        return str(data)

    # Get number of password card rows
    @property
    def rows(self):
        return self._dimensions['rows']

    # Get number of password card columns
    @property
    def columns(self):
        return self._dimensions['columns']

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

        # Add password card body
        for i in range(len(self._m)):
            row = ''.join(self._m.tolist()[i])
            row = "| %s |" % row.center(self.columns)
            output.append(row)

        # Add empty line between body and bottom
        output.append(empty_line)

        # Add bottom with password card dimensions
        dimensions = " %s " % self._get_dimensions()
        bottom = "+%s+\r" % dimensions.center(self.columns+2, "-")
        output.append(bottom)
        output.append("\r")

        # Return full box with password card as the output
        return '\r\n'.join(output)

    # Generator that dumps the passwords for each card read strategy
    def _passwords_generator(self, pwlen):
        # Iterate through streams (strategies)
        for stream in self._streams:
            counter = 0
            # Generate passwords with certain length from the card
            while counter+pwlen < len(stream)+1:
                result = stream[counter:counter+pwlen]
                # Return result back
                yield ''.join(result)
                counter += 1

    # Dumps passwords from the password card
    @property
    def passwords(self):
        # Generate streams based on the card read strategies
        self._generate_data_streams()
        # Iterate through all password lengths between minimum and maximum
        for pwlen in range(self._options['minlen'], self._options['maxlen']+1):
            # Dump password on the screen constructed by the generator above
            for password in self._passwords_generator(pwlen):
                yield password
