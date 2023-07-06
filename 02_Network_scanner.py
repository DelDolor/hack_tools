#!/usr/bin/env python3

""" This script uses ARP protocol to scan network and discover all clients.
    I dont use arping because I want to write my own and learn more python.
       scapy.arping("192.168.104.1/24")

    Example of usage: ./02_Network_scanner.py 192.168.104.2/24
"""

import scapy.all as scapy
from Lokittaja import Lokittaja

def scan(ip):
    arp_request = scapy.ARP()
        #scapy.ls(scapy.ARP()) >> lists all attributes that we can set to ARP request
    arp_request.pdst = ip
        #arp_request.show()
        #print(arp_request.summary()) >>ARP who has Net("192.168.104.150/24") says 192.168.104.150
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        #broadcast.show()

    broadcast_ARP_req = broadcast/arp_request
    broadcast_ARP_req.show()


scan("192.168.104.1/24")
log_util = Lokittaja()
print(log_util.kirjoita("error","viesti"))
