#!/bin/bash

# Set your Cloudflare API token and zone ID
auth_email="your_email@example.com"
auth_key="your_api_key"
zone_id="your_zone_id"

# Get the zone details from the Cloudflare API
zone_details=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache")

# Extract the zone status from the response
zone_status=$(echo "$zone_details" | jq -r '.result.status')
echo "Cloudflare zone status: $zone_status"

# Check if the zone is active
if [ "$zone_status" == "active" ]; then
  echo "Cloudflare zone is active"
else
  echo "Cloudflare zone is not active"
fi

# Get the list of DNS records from the Cloudflare API
dns_records=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/dns_records" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache")

# Extract the DNS record count from the response
dns_record_count=$(echo "$dns_records" | jq -r '.result | length')
echo "Number of DNS records: $dns_record_count"

# Loop through the DNS records and print their details
for i in $(seq 0 $(($dns_record_count - 1))); do
  record_name=$(echo "$dns_records" | jq -r ".result[$i].name")
  record_type=$(echo "$dns_records" | jq -r ".result[$i].type")
  record_status=$(echo "$dns_records" | jq -r ".result[$i].status")
  echo "DNS record: $record_name ($record_type) - $record_status"
done
