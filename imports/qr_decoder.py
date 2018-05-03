#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style
from ini_edit import config_get, config_set


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


def qr_decoder():
    while True:
        check_call(["clear"])
        print (logo)
        colorprint("info", "The 'zbarimg' command will be used to decode QRCode")

        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal", "\n\tPlease specify one to continue:\n")

            path = raw_input(
                "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/qr_decoder" + Style.RESET_ALL + ")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        colorprint("success", "\n[*] Using " + path + "\n")
        choice = raw_input(
            Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input(
                "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/qr_decoder" + Style.RESET_ALL + ")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using " + path + "\n")

        std = Popen(["zbarimg", path], stdout=PIPE, stderr=PIPE)
        (out, err) = std.communicate()

        if out.find("No") == -1:
            colorprint("success", out)
        else:
            colorprint("fatal", out)

        if err:
            colorprint("fatal", err)

        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/qr_decoder" + Style.RESET_ALL + ")\n-->").lower()

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()


if __name__ == "__main__":
    qr_decoder()


