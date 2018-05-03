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

def volatility_pslist():

    while True:

        check_call(["clear"])
        print (logo)
        colorprint("info","'volatility' will be used to list processes.")

        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal","\n\tPlease specify one to continue:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis/volatility_pslist"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        colorprint("success", "\n[*] Using "+path+"\n")

        colorprint("warn","9-->Go back to the top menu")
        colorprint("fatal","0-->Quit")

        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis/volatility_pslist"+Style.RESET_ALL+")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")
        
        colorprint("warn", "Please wait...")

        std = Popen("volatility -f " + path + " imageinfo | grep Suggested | cut -d ',' -f1 | cut -d ':' -f2", shell=True, stdout=PIPE,stderr=PIPE)
        (out, err) = std.communicate()

        if err.find("The requested file doesn't exist") != -1:
            colorprint("fatal" ,err)

        else:
            out = out.rstrip()

            if out.find("No") != -1:
                colorprint("warn", out)
                colorprint("fatal", "This file is not a RAM Dump file Restarting...")

            else:
                std = Popen("volatility -f " + path + " --profile" + out + " pslist", shell=True, stdout=PIPE,stderr=PIPE)
                (out, err) = std.communicate()

                colorprint("success", out)

        raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    volatility_pslist()
