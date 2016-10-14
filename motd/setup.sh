#!/bin/bash -e

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$CURRENT_DIR"

# this is the file that will be produced
result_file="/etc/update-motd.d/70-pun"

# copy pun-motd to the intended destination
echo "Copying pun-motd to $result_file ..."
cp pun-motd "$result_file"

# make sure ownership and permissions are good enough (probably unnecessary)
echo "Setting ownership and permissions on $result_file ..."
chown root:root "$result_file"
chmod +x "$result_file"
