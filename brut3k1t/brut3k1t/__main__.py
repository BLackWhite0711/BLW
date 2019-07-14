#!/usr/bin/env python2
from consts import *

import hashcrack
import protocols
import web

import argparse
import sys
import os

def main():

    print HEADER

    parser = argparse.ArgumentParser(description='Bruteforce framework written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Provide a service being attacked.\
                          The Protocols and Services supported are SSH, FTP, SMTP, XMPP, TELNET, INSTAGRAM, FACEBOOK, TWITTER, MD5, SHA1, SHA224",\
                          metavar='', choices=['ssh', 'ftp', 'smtp', 'xmpp', 'telnet', 'instagram', 'facebook', 'twitter', 'md5', 'sha1', 'sha224'])
    # if submitting a hashstring, also use this argument!
    required.add_argument('-u', '--username', dest='username', help='Provide a valid username/hashstring for service/protocol/hashcrack being executed')
    required.add_argument('-w', '--wordlist', dest='wordlist', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-a', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-p', '--port', type=int, dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')
    parser.add_argument('-d', '--delay', type=int, dest='delay', help='Provide the number of seconds the program delays as each password is tried')

    args = parser.parse_args()

    # Specify mandatory options.
    man_options = ['username', 'wordlist']
    for m in man_options:
        if not args.__dict__[m]:
            # Print help for convenience
            parser.print_help()
            print R + "[!] You have to specify a username AND a wordlist! [!]" + W
            exit(1)

    # Detect if service arg is provided
    if args.service is None:
        print R + "[!] No service provided! [!]" + W
        exit(1)

    # Detect is wordlist path is correct
    if os.path.exists(args.wordlist) == False:
        print R + "[!] Wordlist not found! [!]" + W
        exit(1)


    # Check if the service provided is for hashcracking.
    if args.service in HASHCRACK:
        print (O + "[!] Hashcrack detected! [!]") + W
        print (G + "[*] Hashstring: %s " % args.username) + W
    else:
        print (G + "[*] Username: %s " % args.username) + W

    sleep(0.5)

    # Print path to wordlist supplied
    print (G + "[*] Wordlist: %s " % args.wordlist) + W

    sleep(0.5)

    # Print service being utilized
    print (C + "[*] Service: %s "  % args.service) + W

    if args.delay is None:
        print O + "[?] Delay not set! Default to 1 [?]" + W
        args.delay = 1

    sleep(0.5)

    # main program execution
    if args.service in PROTOCOLS:

        # perform protocol-based bruteforce
        p = protocols.ProtocolBruteforce(args.service, args.address, args.username, args.wordlist, args.port, args.delay)
        p.execute()

    elif args.service in WEB:

        # Web services do not require addresses or ports
        if args.address or args.port:
            print R + "[!] NOTE: You don't need to provide an address OR port [!]" + W
            exit(1)

        # perform web-based bruteforce
        w = web.WebBruteforce(args.service, args.username, args.wordlist, args.delay)
        w.execute()

    elif args.service in HASHCRACK:

        # Hashcrack does not require address or port
        if args.address or args.port:
            print R + "[!] NOTE: You don't need to provide an address OR port [!]" + W
            exit(1)

        # perform hashcracking
        h = hashcrack.HashCrack(args.service, args.username, args.wordlist, args.delay)
        h.execute()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print R + "\n[!] Keyboard Interrupt detected! Killing program... [!]" + W
        exit(1)
