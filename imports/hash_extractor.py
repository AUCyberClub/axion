#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, time
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

def rar2john(rar_path):

    colorprint("info", "Waiting for output path...")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/rar2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["./john_files/rar2john", rar_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "No such file or directory!")
    elif err:
        colorprint("fatal", err)
    else:
        colorprint("success", "\nHash is written to the " + hashtxt_path + ".\n")


def zip2john(zip_path):

    colorprint("info", "Waiting for output path...")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/zip2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["./john_files/zip2john", zip_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "No such file or directory!")
    elif err:
        colorprint("fatal", err)
    else:
        colorprint("success", "\nHash is written to the " + hashtxt_path + ".\n")


def truecrypt2john(truecrypt_path):

    colorprint("info", "Waiting for output path...")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/truecrypt2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["./john_files/truecrypt2john", truecrypt_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "No such file or directory!")
    elif err:
        colorprint("fatal", err)
    else:
        colorprint("success", "\nHash is written to the " + hashtxt_path + ".\n")

def hash_extractor():
    check_call(["clear"])
    while True:
        print (logo)

        colorprint("info", "In this section, you can get hashed passwords out of ZIP, RAR and TrueCrypt files.")
        colorprint("info", "'JohntheRipper' utilities will be used to do this.")

        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal","\n\tPlease specify one to continue:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_extractor"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        colorprint("success", "\n[*] Using "+path+"\n")
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_extractor"+Style.RESET_ALL+")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")

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
            rar2john(path)
        elif choice == "2":
            zip2john(path)
        elif choice == "3":
            truecrypt2john(path)

        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()

if __name__ == "__main__":
    hash_extractor()
