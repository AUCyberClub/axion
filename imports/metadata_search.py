#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen,PIPE,check_call
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

def strings_out(path):
    std = Popen(["strings",path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def exiftool_out(path):
    std = Popen(["exiftool",path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def searcher(path):

    print("Enter a keyword which may be found in the flag.")
    print("e.g : Strings/characters like 'CTF' or '_{' can be used to search for a 'CTF_{flag_is_here}' flag format.")
    
    flag_keyword = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->")

    std = Popen("strings "+path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
    (s_out,err) = std.communicate()

    std = Popen("exiftool "+path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
    (e_out,err) = std.communicate()

    if s_out+e_out:
        colorprint("success", s_out+e_out)
    else:
        colorprint("fatal", "It seems there is no word like that in meta-data or strings output :(")

def metadata_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "'exiftool' and 'strings' will be used to search for a string you specify.")
        
        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal","\n\tPlease specify one to continue:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        
        colorprint("success", "\n[*] Using "+path+"\n")
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")

        std = Popen(["file",path], stdout=PIPE,stderr=PIPE)
        (out,err) = std.communicate()
        if out.find("No such file or directory") == -1:

            colorprint("info", "1-->Search for a specific keyword in 'exiftool' and 'strings' output")
            colorprint("info", "2-->Print meta-data information")
            colorprint("info", "3-->Print 'strings' output")
            colorprint("warn", "9-->Go back to the top menu")
            colorprint("fatal", "0-->Quit")
            choose = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->").lower()
            if choose == "1":
                searcher(path)
                raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
            elif choose == "2":
                colorprint("warn", exiftool_out(path))
                raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
            elif choose == "3":
                colorprint("warn", strings_out(path))
                raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
            elif choose == "9":
                return
            elif choose == "0":
                sys.exit()
            else:
                colorprint("fatal", "Wrong input.\nResetting...\n")
                raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
        else:
            colorprint("fatal", "There is no such file.\nRestarting...\n")
            raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
            break
                 
if __name__ == "__main__":
    metadata_search()


