#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
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
    while True:
        print (logo)
        colorprint("info", "Bu bölümde şifreli morse mesajlarını decode edebilirsiniz.")
        colorprint("info", "Lütfen şifreli mesajı girin.")
        colorprint("warn", "Örnek mesaj formatı    .-- . / .-.. --- ...- . / .- ..- -.-. -.-.   ")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        morse_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_decoder" + Style.RESET_ALL + ")\n-->")

        if morse_msg == "9":
            return
        elif morse_msg == "0":
            sys.exit()
        else:
            text_msg = decode_morse(morse_msg)
            colorprint("success", "Mesajınız dönüştürüldü.")
            print ("Mesaj:\n--> %s" %text_msg)

        colorprint("info", "Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_decoder" + Style.RESET_ALL + ")\n-->")

        if choice == 'H':
            return

if __name__ == "__main__":
    morse_decoder()
