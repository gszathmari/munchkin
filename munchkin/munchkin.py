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

from colorama import Fore, Back, Style, init
from __about__ import __version__, __author__, __description__, __copyright__, __website__
from core.card import Card
from core.utils import supported_python_version

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

def password_dumper(args, card):
    """ Displays card and passwords or dumps them to file """
    # If this is a real terminal, display password card on screen
    if sys.stdout.isatty():
        logging.info(Fore.GREEN + "Printing password card" + Fore.RESET)
        print("\n%s" % card.print_card)
    # Dump passwords to file if this option was selected
    if args.file:
        f = args.file
        logging.info(Fore.CYAN + "Dumping to file: {0}".format(f.name) + Fore.RESET)
        for password in card.passwords:
            f.write("%s\n" % password)
        f.close()
        logging.info(Fore.GREEN + "Write completed" + Fore.RESET)
    # Just display the passwords if user pipes this command
    else:
        for password in card.passwords:
            print(password)

def generate_card_pcard(args, card):
    """ Generate card similar to ones on http://passwordcard.org """
    card.generate_password_card(symbols=args.symbols, digits=args.digits)
    password_dumper(args, card)

def generate_card_custom(args, card):
    """ Generate custom, user supplied password card """
    data = []
    print(Fore.YELLOW + Style.BRIGHT + "Please copy-paste password card below (press ENTER twice when done):\r\n")
    # Read card from terminal
    try:
        while True:
            input_str = raw_input()
            # Finish reading when user leaves line empty
            if input_str == "":
                break
            else:
                row = list(input_str)
                data.append(row)
    # Handle if user presses CTRL + C
    except KeyboardInterrupt:
        print("User interrupt")
        sys.exit(2)
    card.generate_custom_card(data)
    password_dumper(args, card)

def menu():
    """ Contains input arguments and launches controller """
    version_info = Fore.CYAN + "Munchkin wordlist generator version {0} by {1} {2}".format(__version__, __author__, __website__)

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
    wordlist_options.add_argument('-z', '--zig-zag', help='read card zig-zag from top left', action='store_true')
    wordlist_options.add_argument('-x', '--zig-zag-rev', help='read card zig-zag from bottom right', action='store_true')
    wordlist_options.add_argument('-d', '--diagonal', help='read card diagonally', action='store_true')
    wordlist_options.add_argument('-A', '--angled', help='read card at right-angle directions', action='store_true')
    wordlist_options.add_argument('-S', '--spiral', help='read card in spiral directions', action='store_true')
    wordlist_options.add_argument('-a', '--all', help='use each read strategy from above', action='store_true')

    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='Generate wordlist based on cards from:')
    parser_pc = subparsers.add_parser('pcard', help="http://passwordcard.org", parents=[parent_parser])
    parser_custom = subparsers.add_parser('custom', help="your terminal", parents=[parent_parser])

    passwordcard_options = parser_pc.add_argument_group('passwordcard options')
    passwordcard_options.add_argument('-s', '--seed', help='card number (e.g. 7eb3fbfa560d1d1e)', required=True, metavar='str')
    passwordcard_options.add_argument('--symbols', help='include symbols', action='store_true')
    passwordcard_options.add_argument('--digits', help='incude digits', action='store_true')

    # Set controller functions
    passwordcard_options.set_defaults(func=generate_card_pcard)
    parser_custom.set_defaults(func=generate_card_custom)

    args = parser.parse_args()

    controller(args)

def controller(args):
    """ Verifies arguments and dispatches appropriate functions """
    # Verifies whether at least one strategy was selected
    if (args.left_to_right or
        args.right_to_left or
        args.top_down or
        args.bottom_up or
        args.zig_zag or
        args.zig_zag_rev or
        args.diagonal or
        args.angled or
        args.spiral or
        args.all) is False:
        logging.error("Please select at least one algorithm (hint: -l/-r/-t/-b/-z/-x/-d/-A/--all)\r\n")
        sys.exit(3)

    if args.all:
        args.left_to_right = True
        args.right_to_left = True
        args.top_down = True
        args.bottom_up = True
        args.zig_zag = True
        args.zig_zag_rev = True
        args.diagonal = True
        args.angled = True
        args.spiral = True

    # Create card and start processing
    card = Card(args)
    args.func(args, card)

# Displays banner and program version
def banner():
    """ Generates fancy banner """
    banner = """
 _______           _        _______           _       _________ _
(       )|\     /|( (    /|(  ____ \|\     /|| \    /\\__   __/( (    /|
| () () || )   ( ||  \  ( || (    \/| )   ( ||  \  / /   ) (   |  \  ( |
| || || || |   | ||   \ | || |      | (___) ||  (_/ /    | |   |   \ | |
| |(_)| || |   | || (\ \) || |      |  ___  ||   _ (     | |   | (\ \) |
| |   | || |   | || | \   || |      | (   ) ||  ( \ \    | |   | | \   |
| )   ( || (___) || )  \  || (____/\| )   ( ||  /  \ \___) (___| )  \  |
|/     \|(_______)|/    )_)(_______/|/     \||_/    \/\_______/|/    )_)\r\n"""
    print(Style.BRIGHT + "Munchkin {0} {1}".format(__version__, __description__))
    print(Fore.BLUE + "{0}".format(__copyright__))
    print(Style.DIM + banner)

def main(argv=None):
    """ Main program entry point """
    if supported_python_version() is False:
        print("Error: This utility only supports Python 2.6.x and 2.7.x")
        sys.exit(2)

    # Initialize colorama
    init(autoreset=True)

    # Only display the banner if the output is terminal
    if sys.stdout.isatty():
        banner()
    menu()
