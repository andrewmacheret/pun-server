#!/usr/bin/python

# imports
from pprint import pprint
import urllib2
import socket
import sys
#import re
from bs4 import BeautifulSoup
#from pymongo import MongoClient

# read the html content of the random pun page into a string
try:
  html_content = urllib2.urlopen('http://www.punoftheday.com/cgi-bin/randompun.pl', timeout = 1).read()
except urllib2.URLError, e:
  sys.stderr.write("(url error waiting for pun)\n")
  sys.exit(1)
except socket.timeout, e:
  sys.stderr.write("(socket timeout waiting for pun)\n")
  sys.exit(1)

# create a beautiful soup object out of the raw html (the prettify is probably not necessary)
soup = BeautifulSoup(html_content, "html.parser")
soup.prettify()

# find and print the pun... it's the text in the element: div#main-content div.dropshadow1
pun = soup.find('div', {'id': 'main-content'}).find('div', {'class': 'dropshadow1'}).text

pun = pun.strip()

print pun

#try:
#  client = MongoClient()
#  db = client['pundb']
#  collection = db['puns']
#  punDict = {"full": pun}
#  collection.update(punDict, punDict, True)
#except:
#  # do nothing on insertion error
#  pass


