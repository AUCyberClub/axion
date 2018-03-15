#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
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

def hash_brute():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("warn", "Bu özelliği kullanmak için John Jumbo paketine sahip olmalısınız(Kali dağıtımında mevcut)")
        colorprint("info", "Bu bölümde belirlediğiniz wordlistler ile hash kırabilirsiniz.")
        colorprint("info", "Bu iş için 'JohnTheRipper' kullanılacak.")
        colorprint("info", "Öncelikle hash'in bulunduğu metin belgesinin yolunu girin.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        hash_path = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")
        if hash_path == "9":
            return
        elif hash_path == "0":
            sys.exit()

        colorprint("info", "Eğer özel bir wordlist'iniz varsa lütfen yolunu girin.")
        colorprint("warn", "0-->JohnTheRipper'ın hazır wordlist'ini kullan.")

        wordlist_path = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")
        if wordlist_path == "0":
            std = Popen(["john", hash_path], stdout=PIPE, stderr=PIPE)
            (out, err) = std.communicate()
        else:
            std = Popen(["john", "--wordlist="+wordlist_path, hash_path], stdout=PIPE, stderr=PIPE)
            (out, err) = std.communicate()
        if err:
            colorprint("fatal", err)
        if out:
            colorprint("success", out)

        std = Popen(["john", "--show", hash_path], stdout=PIPE, stderr=PIPE)
        (out, err) = std.communicate()
        if err:
            colorprint("fatal", err)
        if out:
            colorprint("success", out)

        colorprint("info", "Başka bir hash kırmayı denemek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")\n-->")

        if choice == 'H':
            return


if __name__ == "__main__":
    hash_brute()
