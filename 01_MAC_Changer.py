#!/usr/bin/env python3

""" This script allows you to change your MAC address.
- Hide your Identity
- Impersonate other devices
- Bypass Filters
- Perform MAC Spoofing attack
"""

import subprocess
import optparse

def read_args():
    # object = module.Class()
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface which MAC-address you want to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC-address to set in use")

    #options contains values from user, arguments contains titles of values (-i, -m)
    (options, arguments) = parser.parse_args()

    if not options.new_mac:
        #handle error
        parser.error("[-] Please specify a new MAC address. Use --help for more info. ")
    elif not options.interface:
        #handle error
        parser.error("[-] Please specify an interface. Use --help for more info. ")
    return options

def change_mac(iface, mac):
    print("[+] Chancing mac address for " + iface + " to " + mac)

    # lets use argument list instead of string
    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig", iface, "hw", "ether", mac])
    subprocess.call(["ifconfig", iface, "up"])
    subprocess.call(["ifconfig", iface])

#read user inputs.
options = read_args()

# Call functions with user given arguments
change_mac(options.interface, options.new_mac)

