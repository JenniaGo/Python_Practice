#!/bin/bash

# Set your Cloudflare API token, zone ID, and domain name
auth_email="your_email@example.com"
auth_key="your_api_key"
zone_id="your_zone_id"
domain_name="yourdomain.com"

# Check the overall health of the Cloudflare service
health_status=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/health" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result')
echo "Cloudflare overall health status: $health_status"

# Check for any active threats
threats=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/security/events" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result[] | select(.action == "challenge")')
if [ -z "$threats" ]; then
  echo "No active threats detected"
else
  echo "Active threats detected:"
  echo "$threats"
fi

# Check for any blocked IPs
blocked_ips=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/firewall/access_rules/rules" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result[] | select(.action == "block") | .config.target')
if [ -z "$blocked_ips" ]; then
  echo "No blocked IPs detected"
else
  echo "Blocked IPs:"
  echo "$blocked_ips"
fi

# Check for SSL certificate expiration
ssl_cert=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_id/ssl/certificate" \
  -H "Content-Type:application/json" \
  -H "X-Auth-Email: $auth_email" \
  -H "X-Auth-Key: $auth_key" \
  -H "cache-control: no-cache" \
  | jq -r '.result.certificate')
expiration_date=$(echo "$ssl_cert" | openssl x509 -text | grep 'Not After' | awk '{print $4,$5,$7}')
echo "SSL certificate expiration date: $expiration_date"
