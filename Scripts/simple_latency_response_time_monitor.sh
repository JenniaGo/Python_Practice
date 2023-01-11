#!/bin/bash

# Set the domain name to check
domain_name="example.com"

# Use 'ping' command to check latency
echo "Checking latency for $domain_name..."
ping -c 5 "$domain_name" | tail -1| awk '{print $4}' | cut -d '/' -f 2

# Use 'curl' command to check response time
echo "Checking response time for $domain_name..."
curl -w "Lookup Time: %{time_namelookup}s\nConnect Time: %{time_connect}s\nStart Transfer Time: %{time_starttransfer}s\nTotal Time: %{time_total}s\n" -o /dev/null -s "$domain_name"
