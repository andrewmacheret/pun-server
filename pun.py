#!/usr/bin/python

# imports
from pprint import pprint
import urllib2
from BeautifulSoup import BeautifulSoup

# read the html content of the random pun page into a string
html_content = urllib2.urlopen('http://www.punoftheday.com/cgi-bin/randompun.pl').read()

# create a beautiful soup object out of the raw html (the prettify is probably not necessary)
soup = BeautifulSoup(html_content)
soup.prettify()

# find and print the pun... it's the text in the element: div#main-content div.dropshadow1
print soup.find('div', {'id': 'main-content'}).find('div', {'class': 'dropshadow1'}).text

