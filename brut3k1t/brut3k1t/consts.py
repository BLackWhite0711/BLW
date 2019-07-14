 # -*- coding: utf-8 -*-
import sys

from time import sleep
from random import *

reload(sys)
sys.setdefaultencoding('utf8')

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

TIMEOUT = "Please wait a few minutes before you try again."

# Contains the services/protocols that can be utilized in our program
PROTOCOLS = ["ssh", "ftp", "smtp", "telnet", "xmpp"]
WEB = ["instagram", "twitter", "facebook"]
HASHCRACK = ["md5", "sha1", "sha224"]

HEADER = """

  _                _   _____ _    _ _
 | |__  _ __ _   _| |_|___ /| | _/ | |_
 | '_ \| '__| | | | __| |_ \| |/ / | __|
 | |_) | |  | |_| | |_ ___) |   <| | |_
 |_.__/|_|   \__,_|\__|____/|_|\_\_|\__|
    Written by: @ex0dus-0x
 """
