#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from colorama import Fore, Back, Style
from subprocess import Popen,PIPE,check_call

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

def func(file_path):
    while(1):
        os.system('clear')
        print (logo)
        colorprint("info", "1-->PDF'in içeriği hakkında bilgi almak için")
        colorprint("info", "2-->PDF'in içine gömülü veri hakkında bilgi")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal","0-->Çık")
        choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/axion"+Style.RESET_ALL+")-->")
        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        elif choice == "1":
            term = os.popen("pdf-parser " + file_path + " | grep /ProcSet ").read()
            print(term)
        elif choice == "2":
            if os.popen("pdf-parser -s Embeddedfile --raw --filter " + file_path + " | grep 'PDF' ").read():
                emb_file = os.popen("pdf-parser -s Embeddedfile --raw --filter " + file_path).read()
                print(emb_file)
            else :
                colorprint("warn", "Gömülü veri bulunamadı")
        colorprint("info","Başka bir işlem ister misiniz? E/H")
        cho1 = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/axion"+Style.RESET_ALL+")-->")
        if cho1 == 'H':
            return

def pdf_parser():
    while (1):
        os.system('clear')
        print (logo)
        colorprint("info","Dosyanın yolunu girin lütfen...")
        colorprint("warn" ,"9-->Üst menüye dön.")
        colorprint("fatal" ,"0-->Çık")
        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/axion"+Style.RESET_ALL+")-->")
        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            std = Popen(["pdf-parser",file_path], stdout=PIPE,stderr=PIPE)
            (out,err) = std.communicate()
            if out.find("No such file or directory") == -1:
                func(file_path)
            else:
                colorprint("fatal", "Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")

        colorprint("info","Başka bir PDF ile işlem ister misiniz? E/H")
        cho1 = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/axion" + Style.RESET_ALL + ")-->")
        if cho1 == 'H':
            return

        '''elif choice == "H":
            return
        elif choice == "E" :

            #succesprint("Yukarıda gördüğünüz /(Obje)'lerden içeriğini çıkarmak istersiniz lütfen girdi yapınız.")
            #warnprint("Girdiniz lütfen sayi olsun.")
            obj = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + Style.RESET_ALL + ")-->")
            #ext_data = os.popen("./source_pdf_parser.py --object "+ obj + " --raw --filter " + file_path).read()
            #print(ext_data)
'''
if __name__ == "__main__":
    find_file_ext()
