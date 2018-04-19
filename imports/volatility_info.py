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

  
def volatility_info():

    while True:

        check_call(["clear"])
        print (logo)
        colorprint("info","'volatility' will be used to determine profile(to model OS).")
        colorprint("info","Waiting for file location...")
        colorprint("warn","9-->Go back to the top menu")
        colorprint("fatal","0-->Quit")

        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis/volatility_info"+Style.RESET_ALL+")\n-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()

        colorprint("warn", "Please wait...")

        std = Popen("volatility -f " + file_path + " imageinfo | grep Suggested | cut -d ',' -f1 | cut -d ':' -f2", shell=True, stdout=PIPE,stderr=PIPE)
        (out, err) = std.communicate()

        if err.find("The requested file doesn't exist") != -1:
            colorprint("fatal" ,err)

        else:
            out = out.rstrip()

            if out.find("No") != -1:
                colorprint("warn", out)
                colorprint("fatal", "This file is not a RAM Dump file Restarting...")
            else:
                colorprint("success", out.replace(" ", ""))

        raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    volatility_info()