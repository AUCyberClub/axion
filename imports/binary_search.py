#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
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


def binary_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "The 'binwalk' tool will be used for binary searching.")
        colorprint("info", "If a file signature match is found in the search, it will be extracted with the 'foremost' tool.")
        colorprint("info", "Waiting for path to file...")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")


        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            std = Popen(["binwalk",file_path], stdout=PIPE,stderr=PIPE)
            (out,err) = std.communicate()

            if not err:
                print(out)

                print("Extract embedded files? Y/N")
                extract_choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")
                if(extract_choice == "Y"):
                    while True:
                        print("Specify the output path:")
                        colorprint("warn", "Abort -> 9")
                        colorprint("fatal", "Quit -> 0")

                        path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")

                        if path == "9":
                            break
                        elif path == "0":
                            sys.exit()
                        
                        std = Popen(["foremost",file_path,"-o",path], stdout=PIPE,stderr=PIPE)
                        (out,err) = std.communicate()

                        if out.find("ERROR") == -1:
                            colorprint("success", "Found files are written to the " + path + ".\n")
                            break
                        else:
                            colorprint("fatal", "The file already exists in the output path you specify, try another one.")
                            raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
            else:
                colorprint("fatal", "No such file was found.\nResetting...\n")
                raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
                    
if __name__ == "__main__":
    binary_search()


