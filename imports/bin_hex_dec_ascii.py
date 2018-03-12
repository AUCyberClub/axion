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
        colorprint("info", "Bu bölümde decimal, hexadecimal, binary ve ascii'yi birbirlerine çevirebilirsiniz.")
        colorprint("info", "1-->Hexadecimal'den Ascii'ye çevir.")
        colorprint("info", "2-->Binary'den Ascii'ye çevir.")
        colorprint("info", "3-->Decimal'den Ascii'ye çevir.")
        colorprint("info", "4-->Hexadecimal'den Decimal'e çevir.")
        colorprint("info", "5-->Decimal'den Binary'ye çevir.")
        colorprint("info", "6-->Binary'den Decimal'e çevir.")
        colorprint("info", "7-->Binary'den Hexadecimal'e çevir.")
        colorprint("info", "8-->Decimal'den Hexadecimal'e çevir.")
        colorprint("info", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        choice = input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/bin_hex_dec_ascii" + Style.RESET_ALL + ")-->")

        colorprint("info", "Lütfen sayıyı girin.")
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
            colorprint("fatal", "Yanlış girdi girdiniz")
            continue

        colorprint("info", "Dönüşüm tamamlandı.")
        print ("Mesaj:\n--> %s" % return_msg)

        colorprint("info", "Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/bin_hex_dec_ascii" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return

if __name__ == "__main__":
    bin_hex_dec_ascii()
