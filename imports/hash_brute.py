#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style
from ini_edit import config_get, config_set
import pexpect
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

def run_john(cmd):
    child = pexpect.spawn(str(cmd))
    try:
        child.expect('Press .*')
    except:
        colorprint("fatal",child.before)
        return
    print(child.before)
    child.sendline('a')
    while True:
        try:
            child.expect('.+g .*')
        except:
            return
        child.sendcontrol('a')
        time.sleep(1)
        colorprint("warn",child.after)


def hash_brute():
    check_call(["clear"])
    while True:
        print (logo)

        colorprint("warn", "This feature work better with John Jumbo package (available in the Kali distribution).")
        colorprint("warn", "Still standart John will work with well-known hashes.")
        colorprint("info", "Here, you can try to crack hashes with the wordlists you want.")
        colorprint("info", "'JohnTheRipper' will be used.")
        colorprint("info", "Also specified path will be used as text file containing the hash.")
        
        path = config_get('paths', 'path')

        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal","\n\tPlease specify one to continue:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        colorprint("success", "\n[*] Using "+path+"\n")
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")

        colorprint("info", "If you have a custom wordlist, please enter the path.")
        colorprint("warn", "Leave Empty-->Use default wordlist for JohnTheRipper.")

        wordlist_path = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")

        colorprint("info", "Do you want to enter a format parameter?")
        colorprint("warn", "Leave Empty-->Use default format detected by John.")

        format = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")

        if wordlist_path == "":
            if format == "":
                cmd = "john " + path
            else:
                cmd = "john " + path + " --format=" + format
        else:
            if format == "":
                cmd = "john " + path + " --wordlist=" + wordlist_path
            else:
                cmd = "john " + path + " --wordlist=" + wordlist_path + " --format=" + format

        run_john(cmd)

        std = Popen(["john", "--show", path], stdout=PIPE, stderr=PIPE)
        (out, err) = std.communicate()
        if err:
            colorprint("fatal", err)
        if out:
            colorprint("success", out)

        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")
        
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()

if __name__ == "__main__":
    hash_brute()
