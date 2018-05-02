#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style
from ini_edit import config_get, config_set
import pexpect
import time

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

format_list = ("""
  des/bsdi/md5/bf/afs/lm/
  dynamic_n/bfegg/dmd5/dominosec/epi/hdaa/ipb2/krb4/
  krb5/mschapv2/mysql-fast/mysql/netlm/netlmv2/netntlm/
  netntlmv2/nethalflm/md5ns/nt/phps/po/xsha/crc32/
  hmac-md5/lotus5/md4-gen/mediawiki/mscash/mscash2/
  mskrb5/mssql/mssql05/mysql-sha1/nsldap/nt2/oracle11/
  oracle/phpass-md5/pix-md5/pkzip/raw-md4/raw-md5thick/
  raw-md5/raw-sha1/raw-sha/raw-md5u/salted-sha1/sapb/
  sapg/sha1-gen/raw-sha224/raw-sha256/raw-sha384/
  raw-sha512/xsha512/hmailserver/sybasease/crypt/trip/
  ssh/pdf/rar/zip/dummy
               """)

def run_john(cmd):
    child = pexpect.spawn(str(cmd))
    child.expect('.+')

    if child.after.find("No pass") != -1:
        colorprint("fatal", child.after)
        return
    if child.after.find("No such") != -1:
        colorprint("fatal", child.after)
        return

    child.sendline('a')
    while True:
        child.expect('.+')
        child.sendline('a')
        if child.after.find("DONE") != -1:
            return
        else:
            colorprint("warn",child.after)


def hash_brute():
    check_call(["clear"])
    while True:
        print (logo)

        colorprint("info", "Here, you can try to crack hashes with the wordlists you want.")
        colorprint("info", "'JohnTheRipper' will be used.")
        colorprint("info", "Also specified path will be used as text file containing the hash.")
        
        path = config_get('paths', 'path')

        if path == '':
            colorprint("fatal", "\n\tOh, it seems there is no path stored before :(")
            colorprint("fatal","\n\tPlease specify one to continue:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nWell, we'll store this path for next operations...\n")

        colorprint("success", "\n[*] Using "+path+"\n")
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue or 'p' to new path..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n--> New path: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")

        colorprint("info", "If you have a custom wordlist, please enter the path.")
        colorprint("warn", "Leave Empty-->Use default wordlist for JohnTheRipper.")

        wordlist_path = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")

        colorprint("info", "Do you want to enter a format parameter?")
        colorprint("warn", "1          -->List all formats for hashes.")
        colorprint("warn", "Leave Empty-->Use default format detected by John.")

        format = raw_input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis/hash_brute" + Style.RESET_ALL + ")-->")

        if format == "1":
            colorprint("warn",format_list)
            raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
            continue

        if wordlist_path == "":
            if format == "":
                cmd = "./john_files/john " + path
            else:
                cmd = "./john_files/john " + path + " --format=" + format
        else:
            if format == "":
                cmd = "./john_files/john " + path + " --wordlist=" + wordlist_path
            else:
                cmd = "./john_files/john " + path + " --wordlist=" + wordlist_path + " --format=" + format

        run_john(cmd)

        std = Popen(["./john_files/john", "--show", path], stdout=PIPE, stderr=PIPE)
        (out, err) = std.communicate()
        if err:
            colorprint("fatal", err)
        if out:
            colorprint("success", out)

        colorprint("warn", "9-->Go back to the top menu")
        colorprint("fatal", "0-->Quit")
        
        choice = raw_input(Style.DIM + Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()

if __name__ == "__main__":
    hash_brute()
