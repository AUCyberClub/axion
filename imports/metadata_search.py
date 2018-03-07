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
        succesprint(s_out+e_out)
    else:
        errprint("Keyword bulunamadı.")
    progress_bar(0.025)

def metadata_search():

    check_call(["clear"])
    while (1):
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____ 
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |    
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___ 
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        succesprint("MetaData taraması için 'exiftool' ve 'strings' kullanılacak.")
        succesprint("Dosyanın yolunu girin lütfen...")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çık")

        file_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")-->")

        if file_path == "9":
            return
        elif file_path == "0":
            sys.exit()
        else:
            while(1):
                std = Popen(["file",file_path], stdout=PIPE,stderr=PIPE)
                (out,err) = std.communicate()
                if out.find("No such file or directory") == -1:
                    succesprint("1-->MetaData ve strings çıktısında berlirli bir keyword ile arama yap.")
                    succesprint("2-->MetaData'yı göster.")
                    succesprint("3-->Strings çıktısını göster.")
                    warnprint("9-->Başka bir dosya yolu gir.")
                    errprint("0-->Çık.")
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
                        errprint("Yanlış girdi.\nTekrar başlatılıyor...\n")  
                        progress_bar(0.025)
                        check_call(["clear"])
                else:
                    errprint("Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")
                    progress_bar(0.025)
                    check_call(["clear"])
                    break
                 
if __name__ == "__main__":
    metadata_search()


