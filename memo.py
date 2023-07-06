""" All the useless stuff that I wanted to keep for in safe for some reason"""""

#Python tutorial: https://www.tutorialspoint.com/python/index.htm

#list
tmp_list = [22,33,44,55,66]
print(tmp_list[0])

#dictionary
tmp_dict = {"eka":22,"toka":33}
print(tmp_dict["toka"])

# You can ask values from user
interface = input("Interface >")
new_mac = input("New MAC >")

# And use them as a part of code. Following is not recommended
# because it allows injections, for. example eth0; ls. So it's not secure
subprocess.call("ifconfig " + interface + " down", shell=True)

#build regex formulas here: pythex.org

#get all fields that scapy.ARP has to offer
scapy.ls(scapy.ARP())

