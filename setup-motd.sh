#!/bin/bash

# set up the message of the day
cp pun-motd /etc/update-motd.d/70-pun
chown root:root /etc/update-motd.d/70-pun
chmod +x /etc/update-motd.d/70-pun

