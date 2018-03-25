#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen,PIPE,check_call
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

def strings_out(file_path):
    std = Popen(["strings",file_path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def exiftool_out(file_path):
    std = Popen(["exiftool",file_path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def searcher(file_path):

    print("Enter a keyword which may be found in the flag.")
    print("e.g : Strings/characters like 'CTF' or '_{' can be used to search for a 'CTF_{flag_is_here}' flag format.")
    
    flag_keyword = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->")

    std = Popen("strings "+file_path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
    (s_out,err) = std.communicate()

    std = Popen("exiftool "+file_path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
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
        colorprint("info", "Waiting for file path...")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            while True:
                std = Popen(["file",file_path], stdout=PIPE,stderr=PIPE)
                (out,err) = std.communicate()
                if out.find("No such file or directory") == -1:
                    colorprint("info", "1-->Search for a specific keyword in 'exiftool' and 'strings' output")
                    colorprint("info", "2-->Print meta-data information")
                    colorprint("info", "3-->Print 'strings' output")
                    colorprint("warn", "9-->Specify another file path")
                    colorprint("fatal", "0-->Quit")
                    choose = input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->")
                    if choose == 1:
                        searcher(file_path)
                    elif choose == 2:
                        colorprint("warn", exiftool_out(file_path))
                    elif choose == 3:
                        colorprint("warn", strings_out(file_path))
                    elif choose == 9:
                        break
                    elif choose == 0:
                        sys.exit()
                    else:
                        colorprint("fatal", "Wrong input.\nResetting...\n")
                else:
                    colorprint("fatal", "There is no such file.\nRestarting...\n")
                    break
                 
if __name__ == "__main__":
    metadata_search()


