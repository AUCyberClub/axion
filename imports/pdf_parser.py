#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from colorama import Fore, Style
from subprocess import Popen,PIPE
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

def func(path):
    while True:
        os.system('clear')
        print (logo)

        colorprint("warn", "To use this feature you must have the PdfParser package (available in the Kali distribution).")
        colorprint("info", "1-->Information about PDF content")
        colorprint("info", "2-->Look for embedded file info")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal","0-->Quit")

        choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/pdf_parser"+Style.RESET_ALL+")-->")
        
        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        elif choice == "1":
            std = Popen(["pdf-parser "+path+" | grep /ProcSet"], stdout=PIPE,stderr=PIPE,shell=True)
            (s_out,err) = std.communicate()
            if s_out:
                colorprint("success", s_out)
            if err:
                colorprint("fatal", err)

            raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

        elif choice == "2":
            std = Popen(["pdf-parser -s Embeddedfile --raw --filter "+path+" | grep PDF"], stdout=PIPE,stderr=PIPE,shell=True)
            (s_out,err) = std.communicate()
            if s_out:
                colorprint("success", s_out)
            if err:
                colorprint("fatal", err)
            else:
                colorprint("warn", "\n\tEmbedded file not found.\n")

            raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

def pdf_parser():
    while True:
        os.system('clear')
        print (logo)

        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal","\n\tPlease specify one to continue:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/find_file_ext"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        colorprint("success", "\n[*] Using "+path+"\n")
        
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal","0-->Quit")

        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")

        std = Popen(["pdf-parser",path], stdout=PIPE,stderr=PIPE)
        (out,err) = std.communicate()

        if out.find("No such file or directory") == -1:
            func(path)
        else:
            colorprint("fatal", "There is no such file.\nRestarting...\n")

if __name__ == "__main__":
    pdf_parser()
