'''
hashcrack.py - Core module for vulnerable hash bruteforcing

Category: Core
Description:
    This module provides the methods for hashcracking vulnerable one-way
    functions. This is achieved by recursively checking each cleartext's hash
    against the current hashstring. Since Python's hashlib library provides
    extensive support for many hashing algorithms, here are those that are
    currently being supported:
    - md5
    - sha1
    - sha224

Dependencies: hashlib

Version: v1.0.0
Author: ex0dus
License: GPL-3.0 || https://opensource.org/licenses/GPL-3.0

'''

from consts import *

import hashlib

class HashCrack:
    def __init__(self, service, targetHash, wordlist, delay):
        self.targetHash = targetHash
        self.wordlist = wordlist
        self.delay = delay

        if service == "md5":
	       self.hashtype = hashlib.md5()
        elif service == "sha1":
           self.hashtype = hashlib.sha1()
        elif service == "sha224":
           self.hashtype = hashlib.sha224()

    def execute(self):
        wordlist = open(self.wordlist, 'r')
        for i in wordlist.readlines():
            password = i.strip("\n")
            self.hashtype.update(password.encode('utf-8'))
            checkedHash = self.hashtype.hexdigest()

            try:
                if checkedHash != self.targetHash:
                    print O + "[*] Target Hash: %s | [*] Current Hash: %s | [*] Cleartext: %s | Incorrect!\n" % (self.targetHash, checkedHash, password) + W
                    sleep(self.delay)
                elif checkedHash == self.targetHash:
                    print G + "[*] Target Hash: %s | [*] Current Hash: %s | [*] Cleartext: %s | Found!\n" % (self.targetHash, checkedHash, password) + W
                    wordlist.close()
                    exit(0)
            except KeyboardInterrupt:
                wordlist.close()
                exit(1)
