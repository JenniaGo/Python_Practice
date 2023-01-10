import os

def install_zabbix():
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y zabbix-server-mysql zabbix-frontend-php zabbix-agent")

def configure_zabbix():
    os.system("sudo nano /etc/zabbix/zabbix_server.conf")
    os.system("sudo nano /etc/zabbix/apache.conf")
    os.system("sudo service apache2 reload")
    os.system("sudo service zabbix-server start")
    os.system("sudo service zabbix-agent start")

install_zabbix()
configure_zabbix()
