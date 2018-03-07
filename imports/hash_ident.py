#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, progressbar, time
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style

def errprint(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
def succesprint(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)
def warnprint(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def progress_bar(timer):
    bar = progressbar.ProgressBar()
    for i in bar(range(100)):
        time.sleep(timer)

def hash_ident():
    check_call(["clear"])
    while (1):
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        succesprint("Hash tanımlaması için 'hashid' kullanılacak")
        succesprint("Hash'i girin lütfen...")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çık")

        raw_hash = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_ident" + Style.RESET_ALL + ")-->")

        if raw_hash == "9":
            return
        elif raw_hash == "0":
            sys.exit()
        else:
            std = Popen(["hashid", raw_hash], stdout=PIPE, stderr=PIPE)
            (out, err) = std.communicate()
            if out:
                succesprint(out)
            if err:
                errprint(err)
            progress_bar(0.05)

if __name__ == "__main__":
    hash_ident()


