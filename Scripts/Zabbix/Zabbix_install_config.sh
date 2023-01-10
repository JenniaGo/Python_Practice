#!/bin/bash

apt-get update
apt-get install -y zabbix-server-mysql zabbix-frontend-php zabbix-agent

nano /etc/zabbix/zabbix_server.conf
nano /etc/zabbix/apache.conf

service apache2 reload
service zabbix-server start
service zabbix-agent start
