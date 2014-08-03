#!/usr/bin/python

from pprint import pprint
import urllib2
from BeautifulSoup import BeautifulSoup

html_content = urllib2.urlopen('http://www.punoftheday.com/cgi-bin/randompun.pl').read()

soup = BeautifulSoup(html_content)
soup.prettify()

print soup.find('div', {'id': 'main-content'}).find('div', {'class': 'dropshadow1'}).text

