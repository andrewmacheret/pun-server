# Random Pun

Output a random pun (from punoftheday.com) by running the following command:

`./pun.py`

Every run, the pun will be stored in a local mongodb database `pundb` in collection `puns`.


Prereqs:
* mongodb
* python

Setup:
* `git clone <clone url>`
* `sudo easy_install pymongo`

# Random Pun MOTD

To install the motd updater so you see a new random pun every time you ssh into your server, run:

`sudo motd/setup-motd.sh`

Result:

![MOTD screenshot](motd.png?raw=true "MOTD screenshot")
