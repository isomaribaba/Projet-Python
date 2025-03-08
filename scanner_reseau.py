import  nmap
import os


def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sV')
    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Port: {port}, State: {nm[host][proto][port]['state']}")
                if 'product' in nm[host][proto][port]:
                    print(f"Product: {nm[host][proto][port]['product']}")
                if 'version' in nm[host][proto][port]:
                    print(f"Version: {nm[host][proto][port]['version']}")

# Example usage
scan_network("192.168.1.0/24")