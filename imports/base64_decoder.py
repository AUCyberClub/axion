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
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)


def decode_base64(base64_msg):
    text_msg = ""
    text_msg = base64.b64decode(base64_msg)
    return text_msg


def base64_decoder():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Bu bölümde base64 encode edilmiş mesajları çözebilirsiniz.")
        colorprint("info", "Lütfen şifreli mesajı girin.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        base64_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/base64_decoder" + Style.RESET_ALL + ")-->")

        if base64_msg == "9":
            return
        elif base64_msg == "0":
            sys.exit()
        else:
            text_msg = decode_base64(base64_msg)
            colorprint("info","Mesajınız dönüştürüldü.")
            print ("Mesaj:\n--> %s" % text_msg)

        colorprint("info", "Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/base64_decoder" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return

if __name__ == "__main__":
    base64_decoder()
