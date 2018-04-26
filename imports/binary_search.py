#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
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


def binary_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "The 'binwalk' tool will be used for binary searching.")
        colorprint("info", "If a file signature match is found in the search, it will be extracted with the 'foremost' tool.")

        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal","\n\tPlease specify one to continue:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        colorprint("success", "\n[*] Using "+path+"\n")
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")

        std = Popen(["binwalk",path], stdout=PIPE,stderr=PIPE)
        (out,err) = std.communicate()

        if not err:
            print(out)

            print("Extract embedded files? Y/N\n")
            colorprint("warn", "9-->Go back to the top menu")
            colorprint("fatal", "0-->Quit")

            extract_choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->").lower()

            if extract_choice == "9":
                return
            elif extract_choice == "0":
                sys.exit()
            elif extract_choice == "y":
                while True:
                    print("\nSpecify the output path:")
                    colorprint("warn", "Abort -> 9")
                    colorprint("fatal", "Quit -> 0")

                    out_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n--> Output path: ")

                    if out_path == "9":
                        return
                    elif out_path == "0":
                        sys.exit()
                        
                    std = Popen(["foremost",path,"-o",out_path], stdout=PIPE,stderr=PIPE)
                    (out,err) = std.communicate()

                    if out.find("ERROR") == -1:
                        if out_path == '':
                            colorprint("success", "Found files are written to the 'output/'\n")
                        else:
                            colorprint("success", "Found files are written to the " + out_path + ".\n")
                        raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
                        break
                    else:
                        colorprint("fatal", "The file already exists in the output path you specify, try another one.")
                        raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

        else:
            colorprint("fatal", "No such file was found.\nResetting...\n")
            raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)  
                    
if __name__ == "__main__":
    binary_search()


