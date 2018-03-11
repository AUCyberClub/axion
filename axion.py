#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from imports.find_file_ext import find_file_ext
from imports.binary_search import binary_search
from imports.metadata_search import metadata_search
from imports.hash_ident import hash_ident
from imports.hash_extractor import hash_extractor
from imports.hash_brute import hash_brute
from imports.morse_decoder import morse_decoder
from imports.morse_encoder import morse_encoder
from imports.vigenere_decoder import vigenere_decoder
from imports.volatility_info import volatility_info
from imports.volatility_notepad import volatility_notepad
from imports.volatility_pslist import volatility_pslist
from imports.volatility_screenshot import volatility_screenshot
from imports.volatility_cmdscan import volatility_cmdscan
from imports.volatility_iehistory import volatility_iehistory

import gettext
tr = gettext.translation('axion', localedir='locale', languages=['tr'])
en = gettext.translation('axion', localedir='locale', languages=['en'])

def language_choice():
    print("1-->English")
    print("2-->Turkish")
    lang = raw_input("Please choose a language...")
    if lang == "1":
        en.install()
    if lang == "2":
        tr.install()

from colorama import Fore, Style
def colorprint(verbosity, text):
    if verbosity == "fatal":
        print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
    if verbosity == "warn":
        print(Fore.YELLOW + text + Style.RESET_ALL)
    if verbosity == "info":
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

import readline, glob
class tab_completer(object):
    def path_completer(self, text, state):
        return [x for x in glob.glob(text + '*')][state]
def auto_path_completer():
    tc = tab_completer()

    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")

    readline.set_completer(tc.path_completer)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)


def file_analysis():
    while True:
        os.system('clear')
        print (logo)
        print(_("Please make a choice"))
        colorprint("info", _("1-->Find file extension"))
        colorprint("info", _("2-->Find hidden files"))
        colorprint("info", _("3-->Search keyword in file's metadata and strings"))
        colorprint("warn", _("9-->Back to top menu"))
        colorprint("fatal", _("0-->Exit"))

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + _("/file_analysis") + Style.RESET_ALL + ")-->")
        if choice == 1:
            find_file_ext()
        elif choice == 2:
            binary_search()
        elif choice == 3:
            metadata_search()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", _("Wrong input, please try again..."))


def crypto():
    while True:
        os.system('clear')
        print (logo)
        print(_("Please make a choice"))
        colorprint("info", _("1-->Ident a hash"))
        colorprint("info", _("2-->Brute force attack for Zip, Rar, TrueCrypt"))
        colorprint("info", _("3-->Brute force attack for raw hash"))
        colorprint("info", _("4-->Vigenere decrypter"))
        colorprint("info", _("5-->Morse decrypter"))
        colorprint("info", _("6-->Morse encoder"))
        colorprint("warn", _("9-->Back to top menu"))
        colorprint("fatal", _("0-->Exit"))

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + _("/crypto") + Style.RESET_ALL + ")-->")
        if choice == 1:
            hash_ident()
        elif choice == 2:
            hash_extractor()
        elif choice == 3:
            hash_brute()
        elif choice == 4:
            vigenere_decoder()
        elif choice == 5:
            morse_decoder()
        elif choice == 6:
            morse_encoder()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", _("Wrong input, please try again..."))


def ram():
    while True:
        os.system('clear')
        print (logo)
        print(_("Please make a choice"))
        colorprint("info", _("1-->Extract OS info from RAM dump"))
        colorprint("info", _("2-->Read opened notepad's in RAM dump"))
        colorprint("info", _("3-->Show the procces list on RAM dump"))
        colorprint("info", _("4-->Take screenshots on RAM dump"))
        colorprint("info", _("5-->Read opened CMD's in RAM dump"))
        colorprint("info", _("6-->Show Internet Explorer history in RAM dump"))
        colorprint("warn", _("9-->Back top top menu"))
        colorprint("fatal", _("0-->Exit"))

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + _("/ram_analysis") + Style.RESET_ALL + ")-->")
        if choice == 1:
            volatility_info()
        elif choice == 2:
            volatility_notepad()
        elif choice == 3:
            volatility_pslist()
        elif choice == 4:
            volatility_screenshot()
        elif choice == 5:
            volatility_cmdscan()
        elif choice == 6:
            volatility_iehistory()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", _("Wrong input, please try again..."))


def main_menu():
    while True:
        os.system('clear')
        print ("""
                                               ░░▒█░░░░       ░░░░░░     ░░░▓█░░
                                                ░░████░░░ ░░░░█████▓░░░░░████░░
                                                ░░▓░░▒███▒███████████░▒███░░░▒
                                                ░░▓░ ░░████░░░▓▓▓███████░░  ░▓░
                                           ░░░░░░██░░░░▒███████████████▒░░░░▓▒
                              ░░  ░░░░░░░░▒███▓░░░█░▓█████████████████████▓░█░░
                   ░░░  ░  ░░░░░░░▒████▒░░░░░░░░░░█▒███████████████████████░█░
               ░░░░░░░░▒▓████████████████████████████████████████████████████░
               ░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░  ░░░████▒████████████▒████▒████░░░
              ░░███████░██▒░░██░███████░███████▓░██████░░░░░███████░░░░░██████░░
              ░███░███████░░███▓██░░▓██▒██░░▒██░░████████████████████████▒▓███░░
              ░████▓██▒██▓░░██▒██▓░░░░░███░░    ░░███████████▓░░░████████████░░
            ░░▒██░░░██▒███████▒██▒▒▒▒░░██▒▒▒▒░░ ░░▓█████████████████████████▒░
            ░░███░░▓█▓███████░▒███▓█▓█▒███▓░░░░ ░░░▒░█████████▒░▓█████████░░░░
            ░░░░░░░▓██████▒░░▒▒▓▓▓▒██░█▓███████████████████████████████▒░░░░░
                  ░░░░░██████░░░░░▒██▓▓░░ ░ ░░░ ░░░░░░░░░██▓███████▓██░░
                        ░░▓██████████░░                  ░░░░█████░░░░
                           ░░░░░░░░░░░░                     ░░▒█▓░░
                    _    __  _____ ___  _   _         _   _   _  ____ ____
                   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
                  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
                 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
                /_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
                ██------->CTF Framework Tool Project Version 0.5<--------██
        """)
        print(_("Please make a choice"))
        colorprint("info", _("1-->File Analysis"))
        colorprint("info", _("2-->Crypto and Hashing"))
        colorprint("info", _("3-->RAM dump analysis"))
        colorprint("fatal", _("0-->Exit"))

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/" + Style.RESET_ALL + ")-->")
        if choice == 1:
            file_analysis()
        elif choice == 2:
            crypto()
        elif choice == 3:
            ram()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", _("Wrong input, please try again..."))


if __name__ == "__main__":
    os.system('clear')
    auto_path_completer()
    language_choice()
    try:
        main_menu()
    except KeyboardInterrupt:
        colorprint("fatal", _("\nProgram is closing..!"))
        sys.exit()
