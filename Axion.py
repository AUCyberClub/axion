#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from imports.find_file_ext import find_file_ext
from imports.binary_search import binary_search
from imports.metadata_search import metadata_search
from imports.hash_ident import hash_ident
from imports.hash_extractor import hash_extractor
from imports.hash_brute import hash_brute
from imports.morse_decoder import morse_decoder
from imports.morse_encoder import morse_encoder
from imports.vigenere_decoder import vigenere_decoder
from imports.volatility_info import volatility_info
from imports.volatility_notepad import volatility_notepad
from imports.volatility_pslist import volatility_pslist
from imports.volatility_screenshot import volatility_screenshot
from imports.volatility_cmdscan import volatility_cmdscan
from imports.volatility_iehistory import volatility_iehistory
import readline, glob
from colorama import Fore, Style

def colorprint(verbosity, text):
    if verbosity == "fatal":
        print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
    if verbosity == "warn":
        print(Fore.YELLOW + text + Style.RESET_ALL)
    if verbosity == "info":
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

class tab_completer(object):
    def path_completer(self, text, state):
        return [x for x in glob.glob(text + '*')][state]

def auto_path_completer():
    tc = tab_completer()

    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")

    readline.set_completer(tc.path_completer)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)


def file_analysis():
    while True:
        os.system('clear')
        print (logo)
        print("Bir seçim yapınız...")
        colorprint("info", "1-->Dosyanın türünü bul.")
        colorprint("info", "2-->Dosya'ya gizlenmiş başka bir dosya var mı ona bak.")
        colorprint("info", "3-->Dosya'nın MetaData'sında ve binary'sinde arama yap.")
        colorprint("info", "4-->Diğer işe yarar dosya tool'larına bak(pdftotext vs...)")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal","0-->Çıkmak istiyorum.")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis" + Style.RESET_ALL + ")-->")
        if choice == 1:
            find_file_ext()
        elif choice == 2:
            binary_search()
        elif choice == 3:
            metadata_search()
        elif choice == 4:
            other_file_tools()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", "Yanlış Girdi Tekrar deneyin...")


def crypto():
    while True:
        os.system('clear')
        print (logo)
        print("Bir seçim yapınız...")
        colorprint("info", "1-->Elimde ki string hash olabilir mi türü nedir?")
        colorprint("info", "2-->Zip, Rar, TrueCrypt kaba kuvvet saldırısı.")
        colorprint("info", "3-->Hash kaba kuvvet saldırısı.")
        colorprint("info", "4-->Vigenere çözücü.")
        colorprint("info", "5-->Morse çözücü.")
        colorprint("info", "6-->Morse oluşturucu.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çıkmak istiyorum.")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto" + Style.RESET_ALL + ")-->")
        if choice == 1:
            hash_ident()
        elif choice == 2:
            hash_extractor()
        elif choice == 3:
            hash_brute()
        elif choice == 4:
            vigenere_decoder()
        elif choice == 5:
            morse_decoder()
        elif choice == 6:
            morse_encoder()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", "Yanlış Girdi Tekrar deneyin...")


def ram():
    while True:
        os.system('clear')
        print (logo)
        print("Bir seçim yapınız...")
        colorprint("info", "1-->Ram dump işletim sistemi bulucu.")
        colorprint("info", "2-->Ram dump notdefteri okuyucu.")
        colorprint("info", "3-->Ram dump process listeleyici.")
        colorprint("info", "4-->Ram dump screenshot çekici.")
        colorprint("info", "5-->Ram dump CMD komut görüntüleyici.")
        colorprint("info", "6-->Ram dump Internet Explorer geçmişi görüntüleyici.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çıkmak istiyorum.")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/ram_analysis" + Style.RESET_ALL + ")-->")
        if choice == 1:
            volatility_info()
        elif choice == 2:
            volatility_notepad()
        elif choice == 3:
            volatility_pslist()
        elif choice == 4:
            volatility_screenshot()
        elif choice == 5:
        	volatility_cmdscan()
        elif choice == 6:
        	volatility_iehistory()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", "Yanlış Girdi Tekrar deneyin...")


def main_menu():
    while True:
        os.system('clear')
        print ("""
                                               ░░▒█░░░░       ░░░░░░     ░░░▓█░░
                                                ░░████░░░ ░░░░█████▓░░░░░████░░
                                                ░░▓░░▒███▒███████████░▒███░░░▒
                                                ░░▓░ ░░████░░░▓▓▓███████░░  ░▓░
                                           ░░░░░░██░░░░▒███████████████▒░░░░▓▒
                              ░░  ░░░░░░░░▒███▓░░░█░▓█████████████████████▓░█░░
                   ░░░  ░  ░░░░░░░▒████▒░░░░░░░░░░█▒███████████████████████░█░
               ░░░░░░░░▒▓████████████████████████████████████████████████████░
               ░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░  ░░░████▒████████████▒████▒████░░░
              ░░███████░██▒░░██░███████░███████▓░██████░░░░░███████░░░░░██████░░
              ░███░███████░░███▓██░░▓██▒██░░▒██░░████████████████████████▒▓███░░
              ░████▓██▒██▓░░██▒██▓░░░░░███░░    ░░███████████▓░░░████████████░░
            ░░▒██░░░██▒███████▒██▒▒▒▒░░██▒▒▒▒░░ ░░▓█████████████████████████▒░
            ░░███░░▓█▓███████░▒███▓█▓█▒███▓░░░░ ░░░▒░█████████▒░▓█████████░░░░
            ░░░░░░░▓██████▒░░▒▒▓▓▓▒██░█▓███████████████████████████████▒░░░░░
                  ░░░░░██████░░░░░▒██▓▓░░ ░ ░░░ ░░░░░░░░░██▓███████▓██░░
                        ░░▓██████████░░                  ░░░░█████░░░░
                           ░░░░░░░░░░░░                     ░░▒█▓░░
                    _    __  _____ ___  _   _         _   _   _  ____ ____
                   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
                  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
                 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
                /_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
                ██------->CTF Framework Tool Project Version 0.5<--------██
        """)
        print("Bir seçim yapınız...")
        colorprint("info", "1-->Dosya Analizi")
        colorprint("info", "2-->Kripto ve Şifreleme")
        colorprint("info", "3-->RAM Dump Analizi")
        colorprint("fatal", "0-->Çıkmak istiyorum.")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/" + Style.RESET_ALL + ")-->")
        if choice == 1:
            file_analysis()
        elif choice == 2:
            crypto()
        elif choice == 3:
            ram()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", "Yanlış Girdi Tekrar deneyin...")


if __name__ == "__main__":
    os.system('clear')
    auto_path_completer()
    try:
        main_menu()
    except KeyboardInterrupt:
        colorprint("fatal", "\nProgram Kapanıyor..!")
        sys.exit()