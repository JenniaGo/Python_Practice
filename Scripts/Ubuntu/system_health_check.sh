#!/bin/bash

# check for available disk space
free_space=$(df -h / | awk '{print $4}' | grep -v Available)
echo "Free disk space: $free_space"

# check for high load average
load_avg=$(cat /proc/loadavg | awk '{print $1}')
max_load=2.0
if [ $(echo "$load_avg > $max_load" | bc) -eq 1 ]; then
  echo "High load average: $load_avg"
  echo "Load average is higher than $max_load"
else
  echo "Load average is normal"
fi

# check for running processes
top_procs=$(ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6)
echo "Top processes by memory usage:"
echo "$top_procs"

# check for open network connections
netstat_output=$(netstat -an | awk '{print $6}' | sort | uniq -c)
echo "Open network connections:"
echo "$netstat_output"
