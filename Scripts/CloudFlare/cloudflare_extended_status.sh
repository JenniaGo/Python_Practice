#!/bin/bash

# Set your Cloudflare API token, zone ID, and domain name
auth_email="your_email@example.com"
auth_key="your_api_key"
zone_id="your_zone_id"
domain_name="yourdomain.com"

# Check for any active challenges on your domain
challenges=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/challenges" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result[] | select(.status == "pending")')
if [ -z "$challenges" ]; then
  echo "No active challenges detected"
else
  echo "Active challenges:"
  echo "$challenges"
fi

# Check your domain name server status
dns_status=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/dns_records?type=NS" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result[] | .content')
echo "Domain name server status: $dns_status"

# Check current number of requests on your zone
request_count=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/analytics/dashboard" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result.totals.requests.all')
echo "Current number of requests: $request_count"

# Check current number of threats blocked on your zone
threats_blocked=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/analytics/dashboard" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result.totals.threats.all')
echo "Current number of threats blocked: $threats_blocked"
