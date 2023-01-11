#!/bin/bash

# Set the domain name to check
domain_name="example.com"

# Use 'mtr' command to check latency and response time from multiple locations
echo "Checking latency and response time for $domain_name..."
mtr --report $domain_name  -c 10  --report-wide

# Use Apache JMeter to check response time under different loads
echo "Checking response time under different loads for $domain_name..."
jmeter -n -t $domain_name -l results.jtl

# Use Elasticsearch, Logstash, Kibana to store and visualize the results
echo "Storing and visualizing the results using ELK stack..."
logstash -f logstash.conf --path.settings /etc/logstash
