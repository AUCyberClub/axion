#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from colorama import Fore, Back, Style

def colorprint(verbosity, text):
    if verbosity == "fatal":
        print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
    if verbosity == "warn":
        print(Fore.YELLOW + text + Style.RESET_ALL)
    if verbosity == "info":
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)

def volatility_screenshot():
    os.system('clear')
    print (logo)
    colorprint("info","RAM dump screenshot çekmek için 'volatility' tool'u kullanılacak")
    colorprint("info","Dosyanın yolunu girin lütfen...")
    colorprint("warn","9-->Üst menüye dön.")
    colorprint("fatal","0-->Çıkmak istiyorum.")

    while True:
        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis/volatility_screenshot"+Style.RESET_ALL+")-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        
        op_system = os.popen("volatility -f " + file_path + " imageinfo | grep Suggested | cut -d ',' -f1 | cut -d ':' -f2").read()
        command = "volatility -f " + file_path + " --profile" + op_system.rstrip() + " screenshot -D screenshots/"
         # 
        if op_system != "":
            os.popen("mkdir screenshots").read()
            colorprint("info",os.popen(command).read())
            colorprint("info","Çekilen screenshotlar 'screenshots' dizinine kaydedilmiştir.")
        else:
            colorprint("fatal","Böyle bir dosya yok.")

if __name__ == "__main__":
    volatility_screenshot()