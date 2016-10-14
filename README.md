# Random Pun

[![Build Status](https://travis-ci.org/andrewmacheret/pun-server.svg?branch=master)](https://travis-ci.org/andrewmacheret/pun-server) [![Docker Stars](https://img.shields.io/docker/stars/andrewmacheret/pun-server.svg)](https://hub.docker.com/r/andrewmacheret/pun-server/) [![Docker Pulls](https://img.shields.io/docker/pulls/andrewmacheret/pun-server.svg)](https://hub.docker.com/r/andrewmacheret/pun-server/) [![License](https://img.shields.io/badge/license-MIT-lightgray.svg)](https://github.com/andrewmacheret/pun-server/blob/master/LICENSE.md)

Output a random pun (from punoftheday.com) by running the following command:

`./pun.py`

Prereqs:

* python
* py-bs4 (you can install it with `easy_install bs4`)

Usage:

* `./pun.py`

# Random Pun REST Server

Prereqs:

* [Node.js](https://nodejs.org)

Usage:

* `npm install`

* `node pun-server.js`

# Docker Server

Prereqs:

* [Docker](https://docker.com)

Usage:

* `docker run --rm -it -p 9999:80 andrewmacheret/pun-server`

* `curl localhost:9999`

# Random Pun MOTD

To install the motd updater so you see a new random pun every time you ssh into your server, run:

`sudo motd/setup.sh`

Result:

![MOTD screenshot](motd.png?raw=true "MOTD screenshot")
