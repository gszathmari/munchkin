# -*- coding: utf-8 -*-

import argparse
import random
import string
import subprocess
import sys
import os
import logging

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))

from __about__ import __version__, __author__
from card import Card

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

# Displays card and passwords or dumps them to file
def password_dumper(args, card):
    # If this is a real terminal, display password card on screen
    if sys.stdout.isatty():
        logging.info("Printing password card")
        print("\n%s" % card.m)
    # Dump passwords to file if this option was selected
    if args.file:
        f = args.file
        logging.info("Dumping to file: %s ... " % f.name)
        for password in card.passwords:
            f.write("%s\n" % password)
        f.close()
        logging.info("Write completed")
    # Just display the passwords if user pipes this command
    else:
        for password in card.passwords:
            print(password)

# Generate card similar to ones on http://passwordcard.org
def generate_card_pcard(args, card):
    # FIXME: Symbols feature is broken
    if args.symbols:
        logging.error("Sorry, this feature is broken at the moment. :(")
        logging.error("Please select the custom card type and paste your card manually.")
        sys.exit(3)

    card.generate_password_card(symbols=args.symbols, digits=args.digits)
    password_dumper(args, card)

# Generate custom, user supplied password card
def generate_card_custom(args, card):
    data = []
    print("Please copy-paste password card below (press ENTER twice when done):\r\n")
    while True:
        input_str = raw_input()
        if input_str == "":
            break
        else:
            row = list(input_str)
            data.append(row)
    card.generate_custom_card(data)
    password_dumper(args, card)

# Contains input arguments and launches controller
def menu():
    version_info="Munchkin wordlist generator version %s by %s" % (__version__, __author__)
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--version', help='version information', action='version', version=version_info)

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-f', '--file', type=argparse.FileType('wb', 0), metavar='name', help='dump passwords to file')

    pwlen_options = parent_parser.add_argument_group('password lengths')
    pwlen_options.add_argument('--minlen', help='minimum password length (default: 6)', default=6, metavar='num')
    pwlen_options.add_argument('--maxlen', help='maximum password length (default: 12)', default=12, metavar='num')

    wordlist_options = parent_parser.add_argument_group('wordlist generator algorithms')
    wordlist_options.add_argument('-l', '--left-to-right', help='read card from top left to bottom right', action='store_true')
    wordlist_options.add_argument('-r', '--right-to-left', help='read card from bottom right to top left', action='store_true')
    wordlist_options.add_argument('-t', '--top-down', help='read card from top left to bottom left', action='store_true')
    wordlist_options.add_argument('-b', '--bottom-up', help='read card from bottom right to top right', action='store_true')

    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='Generate wordlist based on cards from:')
    parser_pc = subparsers.add_parser('pcard', help="http://passwordcard.org", parents=[parent_parser])
    parser_custom = subparsers.add_parser('custom', help="your terminal", parents=[parent_parser])

    passwordcard_options = parser_pc.add_argument_group('passwordcard options')
    passwordcard_options.add_argument('-s', '--seed', help='card number (e.g. 7eb3fbfa560d1d1e)', required=True, metavar='str')
    passwordcard_options.add_argument('--symbols', help='include symbols (broken)', action='store_true')
    passwordcard_options.add_argument('--digits', help='incude digits', action='store_true')

    # Set controller functions
    passwordcard_options.set_defaults(func=generate_card_pcard)
    parser_custom.set_defaults(func=generate_card_custom)

    args = parser.parse_args()

    controller(args)

def controller(args):
    # Verifies whether at least one strategy was selected
    if (args.left_to_right or args.right_to_left or args.top_down or args.bottom_up) is False:
        logging.error("Please select at least one algorithm (hint: -l/-r/-t/-b)\r\n")
        sys.exit(3)
    else:
        # Create card and start processing
        card = Card(args)
        args.func(args, card)

# Displays banner and program version
def banner():
    banner = """
 _______           _        _______           _       _________ _
(       )|\     /|( (    /|(  ____ \|\     /|| \    /\\__   __/( (    /|
| () () || )   ( ||  \  ( || (    \/| )   ( ||  \  / /   ) (   |  \  ( |
| || || || |   | ||   \ | || |      | (___) ||  (_/ /    | |   |   \ | |
| |(_)| || |   | || (\ \) || |      |  ___  ||   _ (     | |   | (\ \) |
| |   | || |   | || | \   || |      | (   ) ||  ( \ \    | |   | | \   |
| )   ( || (___) || )  \  || (____/\| )   ( ||  /  \ \___) (___| )  \  |
|/     \|(_______)|/    )_)(_______/|/     \||_/    \/\_______/|/    )_)\r\n"""
    print("Munchkin {0}\r".format(__version__))
    print(banner)

def main(argv=None):
    # Only display the banner if the output is terminal
    if sys.stdout.isatty():
        banner()
    menu()
