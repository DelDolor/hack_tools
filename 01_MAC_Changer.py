#!/usr/bin/env python3

""" This script allows you to change your MAC address.
- Hide your Identity
- Impersonate other devices
- Bypass Filters
- Perform MAC Spoofing attack
"""

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Chancing mac address for " + interface + " to " + new_mac)

    # lets use argument list instead of string
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

#object = module.Class()
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface which MAC-address you want to change")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC-address to set in use")

# options contains values from user, arguments contains titles of values (-i, -m)
(options, arguments) = parser.parse_args()

# Call functions with user given arguments
change_mac(options.interface, options.new_mac)

