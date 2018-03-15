#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
from subprocess import Popen,PIPE,check_call
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


def binary_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Binary taraması için 'binwalk' tool'u kullanılacak.")
        colorprint("info", "Taramada bulunan dosyalar 'foremost' tool'u ile çıkartılacak.")
        colorprint("info", "Dosyanın yolunu girin lütfen...")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")


        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            std = Popen(["binwalk",file_path], stdout=PIPE,stderr=PIPE)
            (out,err) = std.communicate()

            if not err:
                print(out)
                print("Gömülü dosyaları çıkartmak ister misiniz? E/H")
                extract_choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")
                if(extract_choice == "E"):
                    while True:
                        print("Lütfen çıktı klasörü yolunu belirtin.")
                        colorprint("warn", "İşlem iptali için '9'")
                        colorprint("fatal", "Çıkmak için '0' girin.")
                        path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")

                        if path == "9":
                            break
                        elif path == "0":
                            sys.exit()
                        
                        std = Popen(["foremost",file_path,"-o",path], stdout=PIPE,stderr=PIPE)
                        (out,err) = std.communicate()

                        if out.find("ERROR") == -1:
                            colorprint("success", "Bulunan dosyalar " + path + " yoluna yazılıyor.\n")
                            break
                        else:
                            colorprint("fatal", "Girdiğiniz çıktı yolunda zaten mevcut başka bir yol belirtin.")
            else:
                colorprint("fatal", "Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")
                    
if __name__ == "__main__":
    binary_search()


