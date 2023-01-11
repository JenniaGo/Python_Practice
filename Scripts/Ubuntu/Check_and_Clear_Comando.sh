#!/bin/bash

# check if /var/tmp directory exists
if [ -d "/var/tmp" ]; then
    echo "/var/tmp directory exists"
else
    echo "/var/tmp directory does not exist"
    exit 1
fi

# check if /var/tmp directory is empty
if [ "$(ls -A /var/tmp)" ]; then
    echo "/var/tmp directory is not empty"
else
    echo "/var/tmp directory is empty"
fi

# check if /var/tmp directory is writeable
if [ -w "/var/tmp" ]; then
    echo "/var/tmp directory is writeable"
else
    echo "/var/tmp directory is not writeable"
fi

# Care for this command, it's Comando Style: remove all files older than 5 days from /var/tmp
# find /var/tmp -type f -mtime +5 -delete
# echo "Removed files older than 5 days from /var/tmp"

# check the current disk usage of /var/tmp
tmp_usage=$(du -sh /var/tmp | cut -f1)
echo "Current disk usage of /var/tmp: $tmp_usage"
