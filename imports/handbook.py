#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen,PIPE,check_call
from colorama import Fore, Style
import time

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


def handbook():
    while True:

        check_call(["cp", "-r", "./handbook_files/reverse/images", "/tmp/images"])

        check_call(["clear"])
        print (logo)
        colorprint("info", "You can find lot of information about CTFs here.")
        colorprint("info", "Please select a topic.")
        colorprint("info", "1-->Reverse Engineering (.exe .elf)")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/handbook"+Style.RESET_ALL+")\n-->")

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        elif choice == "1":
            std = Popen(["markdown_edit", "-w", "./handbook_files/reverse/reverse.md"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
            time.sleep(1)
            std.communicate(input="q\n")

        raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    handbook()


