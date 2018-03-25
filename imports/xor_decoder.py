#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, base64
from subprocess import check_call
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


def decode_xor(xor_msg):
    text_msg = ""
    for character in base64.b64decode(xor_msg):
        text_msg += chr(ord(character) ^ ord('_'))
    return text_msg


def xor_decoder():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "In this section you can decrypt XOR-ed messages.")
        colorprint("info", "Enter the cipher:")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        xor_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/xor_decoder" + Style.RESET_ALL + ")\n-->")

        if xor_msg == "9":
            return
        elif xor_msg == "0":
            sys.exit()
        else:
            text_msg = decode_xor(xor_msg)
            colorprint("success","Your message decrypted.")
            print ("Plaintext:\n--> %s" % text_msg)

        colorprint("info", "Another operation? Y/N")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/xor_decoder" + Style.RESET_ALL + ")\n-->")

        if choice == 'N':
            return

if __name__ == "__main__":
    xor_decoder()
