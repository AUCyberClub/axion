#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, time
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

def rar2john():
    colorprint("info", "Enter file path to get hashed password out of RAR file.")
    rar_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/rar2john" + Style.RESET_ALL + ")\n-->")

    colorprint("info", "Waiting for output path...")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/rar2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["rar2john", rar_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "No such file or directory!")
    elif err:
        colorprint("fatal", err)


def zip2john():
    colorprint("info", "Enter file path to get hashed password out of ZIP archive.")
    zip_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/zip2john" + Style.RESET_ALL + ")\n-->")

    colorprint("info", "Waiting for output path...")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/zip2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["zip2john", zip_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "No such file or directory!")
    elif err:
        colorprint("fatal", err)


def truecrypt2john():
    colorprint("info", "Enter file path to get hashed password out of TrueCrypt file.")
    truecrypt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/truecrypt2john" + Style.RESET_ALL + ")\n-->")

    colorprint("info", "Waiting for output path...")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/truecrypt2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["truecrypt2john", truecrypt_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "No such file or directory!")
    elif err:
        colorprint("fatal", err)


def hash_extractor():
    check_call(["clear"])
    while True:
        print (logo)

        colorprint("warn", "To use this feature you must have the John Jumbo package (available in the Kali distribution).")
        colorprint("info", "In this section, you can get hashed passwords out of ZIP, RAR and TrueCrypt files.")
        colorprint("info", "'JohntheRipper' utilities will be used to do this.")
        colorprint("info", "1-->RAR files")
        colorprint("info", "2-->ZIP archives")
        colorprint("info", "3-->TrueCrypt files")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor" + Style.RESET_ALL + ")\n-->")

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        elif choice == "1":
            rar2john()
        elif choice == "2":
            zip2john()
        elif choice == "3":
            truecrypt2john()

        raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)


if __name__ == "__main__":
    hash_extractor()
