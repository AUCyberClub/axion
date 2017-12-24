#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from colorama import Fore, Back, Style

def errprint(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
def succesprint(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)
def warnprint(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def find_file_ext():

    os.system('clear')
    print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____ 
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |    
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___ 
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|

    """)
    succesprint("Dosyanın türünü bulmak için 'file' tool'u kullanılacak")
    succesprint("Dosyanın yolunu girin lütfen...")
    warnprint("9-->Üst menüye dön.")
    errprint("0-->Çık")
    while (1):
        file_path = raw_input("Axion TERMINAL(/file_analysis/find_file_ext)-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        elif os.popen("file " + file_path + " | grep 'cannot open'").read():
            print("Böyle bir dosya yok.")
        elif os.popen("file " + file_path + " | grep 'PDF'").read():
            print("Bu bir pdf dosyası.")
        elif os.popen("file " + file_path + " | grep 'directory' ").read():
            print("Bu bir klasör.")
        elif os.popen("file " + file_path + " | grep ELF").read():
            print("Bu bir ELF çalıştırılabilir dosyası (Dikkatli olun!).")
        elif os.popen("file " + file_path + " | grep 'C program text' ").read():
            print("Bu bir C program dosyası.")
        elif os.popen("file " + file_path + " | grep 'gzip compressed data' ").read():
            print("Bu bir gzip sıkıştırılmış dosya.")
        elif os.popen("file " + file_path + " | grep 'Python script' ").read():
            print("Bu bir Python betiği.")
        elif os.popen("file " + file_path + " | grep 'HTML document' ").read():
            print("Bu bir HTML dosyası.")
        elif os.popen("file " + file_path + " | grep 'MP4' ").read():
            print("Bu bir mp4 video dosyası.")
        elif os.popen("file " + file_path + " | grep 'Audio' ").read():
            print("Bu bir ses dosyası.")
        elif os.popen("file " + file_path + " | grep 'Excel' ").read():
            print("Bu bir Microsoft Exel dosyası.")
        elif os.popen("file " + file_path + " | grep 'Microsoft Word' ").read():
            print("Bu bir Microsoft Word dosyası.")
        elif os.popen("file " + file_path + " | grep 'DOS/MBR boot sector' ").read():
            print("Bu bir DOS/MBR disk dosyası.Belki mount edilebilir.")
        elif os.popen("file " + file_path + " | grep 'Zip archive' ").read():
            print("Bu bir zip sıkıştırılmış dosyası.")
        elif os.popen("file " + file_path + " | grep 'PNG' ").read():
            print("Bu bir PNG resim dosyası.")
        elif os.popen("file " + file_path + " | grep '7-zip archive data' ").read():
            print("Bu bir 7-zip sıkıştırılmış dosyası.")
        elif os.popen("file " + file_path + " | grep 'RAR archive data' ").read():
            print("Bu bir rar sıkıştırılmış dosyası.")
        elif os.popen("file " + file_path + " | grep 'XML' ").read():
            print("Bu bir XML dosyası.")
        elif os.popen("file " + file_path + " | grep 'UTF-8 Unicode text' ").read():
            print("Bu bir metin belgesi.")
        elif os.popen("file " + file_path + " | grep 'ASCII text' ").read():
            print("Bu bir metin belgesi.")
        else:
            errprint("Ne dosyası olduğunu bulamadım")

if __name__ == "__main__":
    find_file_ext()


