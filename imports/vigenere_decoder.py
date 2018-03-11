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
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)

# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)

def decode_vigenere(vigenere_msg, key, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in vigenere_msg:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)


def vigenere_decoder():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Bu bölümde şifreli vigenere mesajlarını decode edebilirsiniz.")
        colorprint("info", "Lütfen şifreli mesajı girin.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        vigenere_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")

        colorprint("info", "Lütfen anahtarı giriniz.")

        key = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")

        if vigenere_msg == "9":
            return
        elif vigenere_msg == "0":
            sys.exit()
        else:
            colorprint("info", "Alfabeyi belirlemek ister misiniz? E/H")
            colorprint("warn", "Ön tanımlı olarak ABCDEFGHIJKLMNOPQRSTUVWXYZ kullanılacak.")
            choice = raw_input(
                "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")
            if choice == 'E':
                colorprint("warn", "Kullanmak istediğiniz alfabeyi girin.")
                LETTERS = raw_input(
                    "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")
                text_msg = decode_vigenere(vigenere_msg, key, LETTERS)

            else:
                text_msg = decode_vigenere(vigenere_msg, key)
            colorprint("info","Mesajınız dönüştürüldü.")
            print ("Mesaj:\n--> %s" %text_msg)

        colorprint("info", "Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return

if __name__ == "__main__":
    vigenere_decoder()
