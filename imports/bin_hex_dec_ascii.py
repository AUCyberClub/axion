#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re
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


def hex_to_ascii(number):
    ascii = bytearray.fromhex(number).decode()
    return ascii
def bin_to_ascii(number):
    return "".join([chr(int(number[i:i + 8], 2)) for i in range(0, len(number), 8)])
def dec_to_ascii(number):
    ascii = re.sub('1?..', lambda m: chr(int(m.group())), number)
    return ascii
def hex_to_dec(number):
    dec = int(number, 16)
    return str(dec)
def dec_to_bin(number):
    return bin(int(number))[2:]
def bin_to_dec(number):
    return int(number, 2)
def bin_to_hex(number):
    return hex(int(number, 2))
def dec_to_hex(number):
    return hex(int(number))

def bin_hex_dec_ascii():
    check_call(["clear"])
    while True:
        print (logo)

        colorprint("info", "You can do convertion between decimal, hexadecimal, binary and ASCII in here.")
        colorprint("info", "1-->Hexadecimal to ASCII")
        colorprint("info", "2-->Binary to ASCII")
        colorprint("info", "3-->Decimal to ASCII")
        colorprint("info", "4-->Hexadecimal to Decimal")
        colorprint("info", "5-->Decimal to Binary")
        colorprint("info", "6-->Binary to Decimal")
        colorprint("info", "7-->Binary to Hexadecimal")
        colorprint("info", "8-->Decimal to Hexadecimal")
        colorprint("info", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        choice = input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/bin_hex_dec_ascii" + Style.RESET_ALL + ")\n-->")

        colorprint("info", "Input:")

        number = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/bin_hex_dec_ascii" + Style.RESET_ALL + ")\n-->")
        number = number.replace(" ", "")

        if choice == 1:
            return_msg = hex_to_ascii(number)
        elif choice == 2:
            return_msg = bin_to_ascii(number)
        elif choice == 3:
            return_msg = dec_to_ascii(number)
        elif choice == 4:
            return_msg = hex_to_dec(number)
        elif choice == 5:
            return_msg = dec_to_bin(number)
        elif choice == 6:
            return_msg = bin_to_dec(number)
        elif choice == 7:
            return_msg = bin_to_hex(number)
        elif choice == 8:
            return_msg = dec_to_hex(number)
        elif choice == 9:
            return
        elif choice == 0:
            sys.exit()
        else:
          
            colorprint("fatal", "Wrong input, please try again...")
            continue

        colorprint("success", "Conversion done.")
        print ("Output:\n--> %s" % return_msg)

        colorprint("info", "Would you like to do another conversion? Y/N")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/bin_hex_dec_ascii" + Style.RESET_ALL + ")\n-->")

        if choice == 'N':

            return

if __name__ == "__main__":
    bin_hex_dec_ascii()
