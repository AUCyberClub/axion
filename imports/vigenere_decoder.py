#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style

def colorprint(verbosity, text):
    if verbosity == "fatal":
        print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
    if verbosity == "warn":
        print(Fore.YELLOW + text + Style.RESET_ALL)
    if verbosity == "info":
        print(Style.DIM + Fore.WHITE + text + Style.RESET_ALL)
    if verbosity == "success":
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)

# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)

def decode_vigenere(vigenere_msg, key, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in vigenere_msg:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)


def vigenere_decoder():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "In here, you can decrypt messages encrypted with Vigenere.")
        colorprint("info", "Enter the cipher:.")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        vigenere_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")\n-->")

        if vigenere_msg == "9":
            return
        elif vigenere_msg == "0":
            sys.exit()
        else:
            colorprint("info", "Type the key:")
            key = raw_input(
                "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")\n-->")

            colorprint("info", "Do you wanna specify a charset? Y/N")
            colorprint("warn", "'ABCDEFGHIJKLMNOPQRSTUVWXYZ' will be used as predefined charset.")
            choice = raw_input(
                "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")\n-->")
            if choice == 'Y':
                colorprint("warn", "You can set a charset now:")
                LETTERS = raw_input(
                    "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")\n-->")
                text_msg = decode_vigenere(vigenere_msg, key, LETTERS)

            else:
                text_msg = decode_vigenere(vigenere_msg, key)
            colorprint("success","Your message decrypted.")
            print ("Plaintext:\n--> %s" %text_msg)

        colorprint("info", "Another operation? Y/N")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")\n-->")

        if choice == 'N':
            return

if __name__ == "__main__":
    vigenere_decoder()
