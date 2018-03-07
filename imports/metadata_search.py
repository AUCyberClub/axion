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

def progress_bar(timer):
    bar = progressbar.ProgressBar()
    for i in bar(range(100)):
        time.sleep(timer)

def strings_out(file_path):
    std = Popen(["strings",file_path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def exiftool_out(file_path):
    std = Popen(["exiftool",file_path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def searcher(file_path):

    print("Aranacak flag'ın içerdiği bir keyword giriniz.")
    print("Örnek : CTF_{flag_burda} gibi bir flag için 'CTF' ya da '_{' gibi keywordler uygundur.")
    
    flag_keyword = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")-->")

    std = Popen("strings "+file_path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
    (s_out,err) = std.communicate()

    std = Popen("exiftool "+file_path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
    (e_out,err) = std.communicate()

    if s_out+e_out:
        colorprint("info", s_out+e_out)
    else:
        colorprint("fatal", "Keyword bulunamadı.")
    progress_bar(0.025)

def metadata_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "MetaData taraması için 'exiftool' ve 'strings' kullanılacak.")
        colorprint("info", "Dosyanın yolunu girin lütfen...")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            while True:
                std = Popen(["file",file_path], stdout=PIPE,stderr=PIPE)
                (out,err) = std.communicate()
                if out.find("No such file or directory") == -1:
                    colorprint("info", "1-->MetaData ve strings çıktısında berlirli bir keyword ile arama yap.")
                    colorprint("info", "2-->MetaData'yı göster.")
                    colorprint("info", "3-->Strings çıktısını göster.")
                    colorprint("warn", "9-->Başka bir dosya yolu gir.")
                    colorprint("fatal", "0-->Çık.")
                    choose = input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")-->")
                    if choose == 1:
                        searcher(file_path)
                    elif choose == 2:
                        print(exiftool_out(file_path))
                        progress_bar(0.025)
                    elif choose == 3:
                        print(strings_out(file_path))
                        progress_bar(0.025)
                    elif choose == 9:
                        check_call(["clear"])
                        break
                    elif choose == 0:
                        sys.exit()
                    else:
                        colorprint("fatal", "Yanlış girdi.\nTekrar başlatılıyor...\n")  
                        progress_bar(0.025)
                        check_call(["clear"])
                else:
                    colorprint("fatal", "Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")
                    progress_bar(0.025)
                    check_call(["clear"])
                    break
                 
if __name__ == "__main__":
    metadata_search()


