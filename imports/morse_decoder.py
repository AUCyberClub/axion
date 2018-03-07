#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style

def errprint(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)

def succesprint(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

def warnprint(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

morseAlphabet ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/"
    }
inverseMorseAlphabet = dict((v,k) for (k,v) in morseAlphabet.items())

def decode_morse(morse_msg):
    text_msg = ""
    for item in morse_msg.split(' '):
        text_msg = text_msg + inverseMorseAlphabet[item]
    return text_msg

def morse_decoder():
    check_call(["clear"])
    while (1):
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        succesprint("Bu bölümde şifreli morse mesajlarını decode edebilirsiniz.")
        succesprint("Lütfen şifreli mesajı girin.")
        warnprint("Örnek mesaj formatı    .-- . / .-.. --- ...- . / .- ..- -.-. -.-.   ")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çık")

        morse_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_decoder" + Style.RESET_ALL + ")-->")

        if morse_msg == "9":
            return
        elif morse_msg == "0":
            sys.exit()
        else:
            text_msg = decode_morse(morse_msg)
            succesprint ("Mesajınız dönüştürüldü.")
            print ("Mesaj:\n--> %s" %text_msg)

        succesprint("Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_decoder" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return

if __name__ == "__main__":
    morse_decoder()
