#!/bin/bash

log_status=$(systemctl is-active syslog.service)
if [ $log_status == "active" ]; then
  echo "syslog service is running"
else
  echo "syslog service is not running"
fi

spool_status=$(systemctl is-active cups.path)
if [ $spool_status == "active" ]; then
  echo "spool service is running"
else
  echo "spool service is not running"
fi

tmp_status=$(systemctl is-active tmp.service)
if [ $tmp_status == "active" ]; then
  echo "tmp service is running"
else
  echo "tmp service is not running"
fi

lib_status=$(systemctl is-active packagekit.service)
if [ $lib_status == "active" ]; then
  echo "lib service is running"
else
  echo "lib service is not running"
fi

cache_status=$(systemctl is-active apt-cacher-ng.service)
if [ $cache_status == "active" ]; then
  echo "cache service is running"
else
  echo "cache service is not running"
fi
