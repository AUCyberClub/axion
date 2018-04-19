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
        colorprint("info", "In this section, you can decode Morse encoded messages.")
        colorprint("info", "Enter the Morse code:")
        colorprint("warn", "i.e -> .-- . / .-.. --- ...- . / .- ..- -.-. -.-.   ")
        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")

        morse_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_decoder" + Style.RESET_ALL + ")\n-->")

        if morse_msg == "9":
            return
        elif morse_msg == "0":
            sys.exit()
        else:
            text_msg = decode_morse(morse_msg)
            colorprint("success", "Your message decoded.")
            print ("Message:\n--> %s" %text_msg)

        raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    morse_decoder()
