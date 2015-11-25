#!/usr/bin/python

import sys
import json
from pymongo import MongoClient

client = MongoClient()
db = client['pundb']
collection = db['puns']

def insert_pun(pun):
  punDict = {"full": pun}
  collection.update(punDict, punDict, True)

input = sys.stdin.read().strip()
insert_pun(input)


