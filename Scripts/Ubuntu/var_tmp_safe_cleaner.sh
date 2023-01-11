#!/bin/bash

# Usage: This script prompts the user to select files older than 5 days, in /var/tmp, to delete. It also checks for the existence and writability of the /var/tmp directory before proceeding with the deletion.

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
    exit 0
fi

# check if /var/tmp directory is writeable
if [ -w "/var/tmp" ]; then
    echo "/var/tmp directory is writeable"
else
    echo "/var/tmp directory is not writeable"
    exit 1
fi

# list all files older than 5 days from /var/tmp
files_to_delete=($(find /var/tmp -type f -mtime +5))

if [ ${#files_to_delete[@]} -eq 0 ]; then
    echo "No files older than 5 days found"
    exit 0
fi

# prompt user to select files to delete
echo "The following files are older than 5 days:"
PS3='Select the files you want to delete: '
select file in "${files_to_delete[@]}" "Quit"; do
    if [ "$file" == "Quit" ]; then
        break
    fi
    echo "Deleting $file"
    rm "$file"
done
