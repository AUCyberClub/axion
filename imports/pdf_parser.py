#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from colorama import Fore, Style
from subprocess import Popen,PIPE

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

def func(file_path):
    while(1):
        os.system('clear')
        print (logo)
        colorprint("info", "1-->Information about PDF content")
        colorprint("info", "2-->Look for embedded file info")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal","0-->Quit")
        choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/axion"+Style.RESET_ALL+")-->")
        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        elif choice == "1":
            term = os.popen("pdf-parser " + file_path + " | grep /ProcSet ").read()
            print(term)
        elif choice == "2":
            if os.popen("pdf-parser -s Embeddedfile --raw --filter " + file_path + " | grep 'PDF' ").read():
                emb_file = os.popen("pdf-parser -s Embeddedfile --raw --filter " + file_path).read()
                print(emb_file)
            else :
                colorprint("warn", "Embedded file not found.")
        colorprint("info","Do you wanna do something else? Y/N")
        cho1 = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/axion"+Style.RESET_ALL+")-->")
        if cho1 == 'N':
            return

def pdf_parser():
    while (1):
        os.system('clear')
        print (logo)

        colorprint("info","Waiting for file path...")
        colorprint("warn" ,"9-->Go back to the top menu")
        colorprint("fatal" ,"0-->Quit")
        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/axion"+Style.RESET_ALL+")-->")
        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            std = Popen(["pdf-parser",file_path], stdout=PIPE,stderr=PIPE)
            (out,err) = std.communicate()
            if out.find("No such file or directory") == -1:
                func(file_path)
            else:
                colorprint("fatal", "There is no such file.\nRestarting...\n")

        colorprint("info","Try another PDF file? Y/N")
        cho1 = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/axion" + Style.RESET_ALL + ")-->")
        if cho1 == 'N':
            return

if __name__ == "__main__":
    pdf_parser()
