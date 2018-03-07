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

def volatility_iehistory():

    colorprint("info","RAM dump Internet Explorer geçmişini görüntülemek için 'volatility' tool'u kullanılacak")
    colorprint("info","Dosyanın yolunu girin lütfen...")
    colorprint("warn","9-->Üst menüye dön.")
    colorprint("fatal","0-->Çıkmak istiyorum.")

    while True:
        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis/volatility_iehistory"+Style.RESET_ALL+")-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        
        op_system = os.popen("volatility -f " + file_path + " imageinfo | grep Suggested | cut -d ',' -f1 | cut -d ':' -f2").read()
        command = "volatility -f " + file_path + " --profile" + op_system.rstrip() + " iehistory"
        
        if op_system != "":
            colorprint("info",os.popen(command).read())
        
        else:
            colorprint("fatal","Böyle bir dosya yok.")

if __name__ == "__main__":
    volatility_iehistory()