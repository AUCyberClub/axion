#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time,progressbar
from subprocess import Popen,PIPE,check_call
from colorama import Fore, Back, Style

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

def progress_bar():
    bar = progressbar.ProgressBar()
    for i in bar(range(100)):
        time.sleep(0.025)

def binary_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Binary taraması için 'binwalk' tool'u kullanılacak.")
        colorprint("info", "Taramada bulunan dosyalar 'foremost' tool'u ile çıkartılacak.")
        colorprint("info", "Dosyanın yolunu girin lütfen...")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")


        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            #komut = binwalk file_path
            #binwalk ile çalışırken terminal çıktısını ikiye ayrılıyor stderr ve stdout olarak.
            #Komutta bir hata varsa binwalk hatası err'ye yoksa normal binwalk çıktısı out'a yazılıyor.
            #Ne varki foremost tool'unu aynı şekilde kontrol edemiyoruz.
            #Bu yüzden orda farklı bir yaklaşım kullandım.
            #Foremost tool'unun hataları err'ye düşmüyor out'a düşüyor.İçinde hata bulmak için find kullandım
            std = Popen(["binwalk",file_path], stdout=PIPE,stderr=PIPE)
            (out,err) = std.communicate()

            if not err:
                print(out)
                print("Gömülü dosyaları çıkartmak ister misiniz? E/H")
                extract_choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")-->")
                if(extract_choice == "E"):
                    while True:
                        print("Lütfen çıktı klasörü yolunu belirtin.")
                        colorprint("warn", "İşlem iptali için '9'")
                        colorprint("fatal", "Çıkmak için '0' girin.")
                        path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")-->")

                        if path == "9":
                            break
                        elif path == "0":
                            sys.exit()
                        
                        std = Popen(["foremost",file_path,"-o",path], stdout=PIPE,stderr=PIPE)
                        (out,err) = std.communicate()

                        if out.find("ERROR") == -1:
                            colorprint("info", "Bulunan dosyalar " + path + " yoluna yazılıyor.\n")
                            progress_bar()
                            break
                        else:
                            colorprint("fatal", "Girdiğiniz çıktı yolunda zaten mevcut başka bir yol belirtin.")
            else:
                colorprint("fatal", "Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")
                progress_bar()
                check_call(["clear"])
                    
if __name__ == "__main__":
    binary_search()


