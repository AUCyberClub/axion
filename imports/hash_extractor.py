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


def rar2john():
    succesprint("Rar dosyasından hash çıkartmak için lütfen dosya yolunu giriniz.")
    rar_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/rar2john" + Style.RESET_ALL + ")-->")
    succesprint("Çıkartılacak olan dosya için lütfen dosya yolunu giriniz.")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/rar2john" + Style.RESET_ALL + ")-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["rar2john", rar_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        errprint("Hata dosya bulunamadı!")
    elif err:
        errprint(err)
    progress_bar(0.05)


def zip2john():
    succesprint("Zip dosyasından hash çıkartmak için lütfen dosya yolunu giriniz.")
    zip_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/zip2john" + Style.RESET_ALL + ")-->")
    succesprint("Çıkartılacak olan dosya için lütfen dosya yolunu giriniz.")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/zip2john" + Style.RESET_ALL + ")-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["zip2john", zip_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        errprint("Hata dosya bulunamadı!")
    elif err:
        errprint(err)
    progress_bar(0.05)


def truecrypt2john():
    succesprint("TrueCrypt dosyasından hash çıkartmak için lütfen dosya yolunu giriniz.")
    truecrypt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/truecrypt2john" + Style.RESET_ALL + ")-->")
    succesprint("Çıkartılacak olan dosya için lütfen dosya yolunu giriniz.")
    hashtxt_path = raw_input(
        "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor/truecrypt2john" + Style.RESET_ALL + ")-->")

    with open(hashtxt_path, 'w') as out:
        std = Popen(["truecrypt2john", truecrypt_path], stdout=out, stderr=PIPE)
        (out, err) = std.communicate()
    if err.find("No such file or directory") != -1:
        errprint("Hata dosya bulunamadı!")
    elif err:
        errprint(err)
    progress_bar(0.05)


def hash_extractor():
    check_call(["clear"])
    while (1):
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        succesprint("Bu bölümde rar, zip ve trueCrypt hashlerini dosyaların içerisinden çıkartabilirsiniz.")
        succesprint("Bu iş için 'JohntheRipper' araçları kullanılacak.")
        succesprint("1-->Rar dosyaları.")
        succesprint("2-->Zip dosyaları.")
        succesprint("3-->TrueCrypt dosyaları.")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çık")

        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor" + Style.RESET_ALL + ")-->")

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

        succesprint("Başka bir dosyadan hash çıkartmak ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_extractor" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return


if __name__ == "__main__":
    hash_extractor()
