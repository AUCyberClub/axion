#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style

def errprint(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)


def succesprint(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)


def warnprint(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)


def hash_brute():
    check_call(["clear"])
    while (1):
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        succesprint("Bu bölümde belirlediğiniz wordlistler ile hash kırabilirsiniz.")
        succesprint("Bu iş için 'JohnTheRipper' kullanılacak.")
        succesprint("Öncelikle hash'in bulunduğu metin belgesinin yolunu girin.")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çık")

        hash_path = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")
        if hash_path == "9":
            return
        elif hash_path == "0":
            sys.exit()

        succesprint("Eğer özel bir wordlist'iniz varsa lütfen yolunu girin.")
        warnprint("0-->JohnTheRipper'ın hazır wordlist'ini kullan.")

        wordlist_path = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")
        if wordlist_path == "0":
            std = Popen(["john", hash_path], stdout=PIPE, stderr=PIPE)
            (out, err) = std.communicate()
        else:
            std = Popen(["john", "--wordlist="+wordlist_path, hash_path], stdout=PIPE, stderr=PIPE)
            (out, err) = std.communicate()
        if err:
            errprint(err)
        if out:
            succesprint(out)

        std = Popen(["john", "--show", hash_path], stdout=PIPE, stderr=PIPE)
        (out, err) = std.communicate()
        if err:
            errprint(err)
        if out:
            succesprint(out)

        succesprint("Başka bir hash kırmayı denemek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return


if __name__ == "__main__":
    hash_brute()
