import nmap

def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.0.0/24', arguments='-sS')
    for host in nm.all_hosts():
        print(f'Host: {host}')
        print(f'State: {nm[host].state()}')
        print(f'OS: {nm[host].os()}')
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                print(f'Port: {port}  State: {nm[host][proto][port]["state"]}  Service: {nm[host][proto][port]["name"]}')

scan_network()
