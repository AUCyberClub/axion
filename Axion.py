#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from imports.find_file_ext import find_file_ext
from imports.binary_search import binary_search
from imports.metadata_search import metadata_search
from imports.hash_ident import hash_ident
from imports.hash_extractor import hash_extractor
from imports.hash_brute import hash_brute
from imports.morse_decoder import morse_decoder
from imports.morse_encoder import morse_encoder
from imports.vigenere_decoder import vigenere_decoder

from colorama import Fore, Back, Style

def errprint(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
def succesprint(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)
def warnprint(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def file_analysis():
    while (1):
        os.system('clear')
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____ 
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |    
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___ 
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        print("Bir seçim yapınız...")
        succesprint("1-->Dosyanın türünü bul.")
        succesprint("2-->Dosya'ya gizlenmiş başka bir dosya var mı ona bak.")
        succesprint("3-->Dosya'nın MetaData'sında ve binary'sinde arama yap.")
        succesprint("4-->Diğer işe yarar dosya tool'larına bak(pdftotext vs...)")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çıkmak istiyorum.")
    
        choice = input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis"+Style.RESET_ALL+")-->")
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
            errprint("Yanlış Girdi Tekrar deneyin...")  

def crypto():
    while (1):
        os.system('clear')
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____ 
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |    
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___ 
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        print("Bir seçim yapınız...")
        succesprint("1-->Elimde ki string hash olabilir mi türü nedir?")
        succesprint("2-->Zip, Rar, TrueCrypt kaba kuvvet saldırısı.")
        succesprint("3-->Hash kaba kuvvet saldırısı.")
        succesprint("4-->Vigenere çözücü.")
        succesprint("5-->Morse çözücü.")
        succesprint("6-->Morse oluşturucu.")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çıkmak istiyorum.")


        choice = input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/crypto"+Style.RESET_ALL+")-->")
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
            errprint("Yanlış Girdi Tekrar deneyin...")  
def ram():
    while (1):
        os.system('clear')
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____ 
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |    
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___ 
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        print("Bir seçim yapınız...")
        succesprint("1-->Ram dump işletim sistemi bulucu.")
        succesprint("2-->Ram dump notdefteri okuyucu.")
        succesprint("3-->Ram dump paint okuyucu.")
        succesprint("4-->Ram dump screenshot çekici.")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çıkmak istiyorum.")


        choice = input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis"+Style.RESET_ALL+")-->")
        if choice == 1:
            volatility_info()
        elif choice == 2:
            volatility_notepad()
        elif choice == 3:
            volatility_paint()
        elif choice == 4:
            volatility_screenshot()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            errprint("Yanlış Girdi Tekrar deneyin...")  
def main_menu():
    while (1):
        os.system('clear')
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____ 
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |    
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___ 
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        print("Bir seçim yapınız...")
        succesprint("1-->Dosya Analizi")
        succesprint("2-->Kripto ve Şifreleme")
        succesprint("3-->RAM Dump Analizi")
        errprint("0-->Çıkmak istiyorum.")

        choice = input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/"+Style.RESET_ALL+")-->")
        if choice == 1:
            file_analysis()
        elif choice == 2:
            crypto()
        elif choice == 3:
            ram()
        elif choice == 0:
            sys.exit()
        else:
            errprint("Yanlış Girdi Tekrar deneyin...")    

if __name__ == "__main__":
    os.system('clear')
    try:
        main_menu()
    except KeyboardInterrupt:
        errprint ("\nProgram Kapanıyor..!")
        sys.exit()

