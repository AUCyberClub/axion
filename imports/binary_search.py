#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time,progressbar
from subprocess import Popen,PIPE,check_call
from colorama import Fore, Back, Style

def errprint(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
def succesprint(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)
def warnprint(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def progress_bar():
    bar = progressbar.ProgressBar()
    for i in bar(range(100)):
        time.sleep(0.025)

def binary_search():

    check_call(["clear"])
    while (1):
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____ 
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |    
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___ 
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        succesprint("Binary taraması için 'binwalk' tool'u kullanılacak.")
        succesprint("Taramada bulunan dosyalar 'foremost' tool'u ile çıkartılacak.")
        succesprint("Dosyanın yolunu girin lütfen...")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çık")


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
                    while(1):
                        print("Lütfen çıktı klasörü yolunu belirtin.")
                        warnprint("İşlem iptali için '9'")
                        errprint("Çıkmak için '0' girin.")
                        path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")-->")

                        if path == "9":
                            break
                        elif path == "0":
                            sys.exit()
                        
                        std = Popen(["foremost",file_path,"-o",path], stdout=PIPE,stderr=PIPE)
                        (out,err) = std.communicate()

                        if out.find("ERROR") == -1:
                            succesprint("Bulunan dosyalar " + path + " yoluna yazılıyor.\n")
                            progress_bar()
                            break
                        else:
                            errprint("Girdiğiniz çıktı yolunda zaten mevcut başka bir yol belirtin.")
            else:
                errprint("Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")
                progress_bar()
                check_call(["clear"])
                    
if __name__ == "__main__":
    binary_search()


