#!/bin/bash -e

# this is the file that will be produced
result_file="/etc/update-motd.d/70-pun"
pun_script="$( pwd )"/pun.py

# replace __PUN_SCRIPT__ in pun-motd and put the results in the intended destination
awk -v PUN_SCRIPT="${pun_script}" '{gsub("__PUN_SCRIPT__", PUN_SCRIPT); print}' motd/pun-motd > "$result_file" || exit 1

# make sure ownership and permissions are good enough (probably unnecessary)
chown root:root "$result_file" || exit 1
chmod +x "$result_file" || exit 1

