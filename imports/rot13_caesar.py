#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import check_call
from colorama import Fore, Style
from string import maketrans, translate


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


def shift(alphabet, n):
    alphabet = list(alphabet)
    for i in range(len(alphabet) - n):
        alphabet[i] = chr(ord(alphabet[i]) + n)
    for i in range(n):
        alphabet[25 - i] = chr(ord(alphabet[25 - i]) + n - 26)
    alphabet = ''.join(alphabet)
    return alphabet


def rot_to_text(n, text):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper_rot = shift(upper, n)
    lower_rot = shift(lower, n)
    rot = maketrans(upper + lower, upper_rot + lower_rot)
    return translate(text, rot)


def rot13_caesar():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Bu bölümde sezar ve rot şifreli mesajlarını çözebilirsiniz.")
        colorprint("info", "Lütfen şifreli mesajı girin.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        caesar_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/base64_decoder" + Style.RESET_ALL + ")-->")

        if caesar_msg == "9":
            return
        elif caesar_msg == "0":
            sys.exit()
        else:
            colorprint("info", "Tüm ihtimaller aşağıdadır.")
            for i in range(1,26):
                rot_msg = rot_to_text(i,caesar_msg)
                colorprint("info", "rot" + str(i) + ":  " + rot_msg)

        colorprint("info", "Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/base64_decoder" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return


if __name__ == "__main__":
    rot13_caesar()
