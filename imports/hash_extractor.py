#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, time
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

def rar2john():
    colorprint("info", "Rar dosyasından hash çıkartmak için lütfen dosya yolunu giriniz.")
    rar_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/rar2john" + Style.RESET_ALL + ")\n-->")
    colorprint("info", "Çıkartılacak olan dosya için lütfen dosya yolunu giriniz.")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/rar2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["rar2john", rar_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "Hata dosya bulunamadı!")
    elif err:
        colorprint("fatal", err)


def zip2john():
    colorprint("info", "Zip dosyasından hash çıkartmak için lütfen dosya yolunu giriniz.")
    zip_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/zip2john" + Style.RESET_ALL + ")\n-->")
    colorprint("info", "Çıkartılacak olan dosya için lütfen dosya yolunu giriniz.")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/zip2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["zip2john", zip_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "Hata dosya bulunamadı!")
    elif err:
        colorprint("fatal", err)


def truecrypt2john():
    colorprint("info", "TrueCrypt dosyasından hash çıkartmak için lütfen dosya yolunu giriniz.")
    truecrypt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/truecrypt2john" + Style.RESET_ALL + ")\n-->")
    colorprint("info", "Çıkartılacak olan dosya için lütfen dosya yolunu giriniz.")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/truecrypt2john" + Style.RESET_ALL + ")\n-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["truecrypt2john", truecrypt_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        colorprint("fatal", "Hata dosya bulunamadı!")
    elif err:
        colorprint("fatal", err)


def hash_extractor():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("warn", "Bu özelliği kullanmak için John Jumbo paketine sahip olmalısınız(Kali dağıtımında mevcut)")
        colorprint("info", "Bu bölümde rar, zip ve trueCrypt hashlerini dosyaların içerisinden çıkartabilirsiniz.")
        colorprint("info", "Bu iş için 'JohntheRipper' araçları kullanılacak.")
        colorprint("info", "1-->Rar dosyaları.")
        colorprint("info", "2-->Zip dosyaları.")
        colorprint("info", "3-->TrueCrypt dosyaları.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor" + Style.RESET_ALL + ")\n-->")

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        elif choice == "1":
            rar2john()
        elif choice == "2":
            zip2john()
        elif choice == "3":
            truecrypt2john()

        colorprint("info", "Başka bir dosyadan hash çıkartmak ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor" + Style.RESET_ALL + ")\n-->")

        if choice == 'H':
            return


if __name__ == "__main__":
    hash_extractor()
