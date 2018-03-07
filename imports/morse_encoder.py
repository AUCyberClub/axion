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

morse_table = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '(': '-.--.-',
        '8': '---..',           ')': '-.--.-',
        '9': '----.',           '_': '..--.-',
        ' ': '/',
}

def encode_morse(text_msg):
    morse_msg = ""
    for i in list(text_msg):
        morse_msg = morse_msg + morse_table[i] + " "
    return morse_msg


def morse_encoder():
    check_call(["clear"])
    while (1):
        print ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)
        succesprint("Bu bölümde metin mesajlarını morse alfabesi şeklinde encode edebilirsiniz.")
        succesprint("Lütfen metni girin.")
        warnprint("9-->Üst menüye dön.")
        errprint("0-->Çık")

        text_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_encoder" + Style.RESET_ALL + ")-->")

        if text_msg == "9":
            return
        elif text_msg == "0":
            sys.exit()
        else:
            morse_msg = encode_morse(text_msg)
            succesprint ("Mesajınız dönüştürüldü.")
            print "Mesaj:\n--> ", morse_msg

        succesprint("Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_encoder" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return

if __name__ == "__main__":
    morse_encoder()