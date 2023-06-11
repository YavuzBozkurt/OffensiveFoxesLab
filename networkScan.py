from scapy.all import *


def auto_scan():

    (interface,ipA,ipG) = conf.route.route("0.0.0.0")

    ip_range = ipG + "/24"

    print("\ninterface: " + interface)
    print("own IP: " + ipA)
    print("gateway IP: " + ipG + "\n")

    arp_result = arping(ip_range)
    
    close = raw_input()
    

def manual_scan(ipG,subnet_mask):

    cidr = sum([str(bin(int(octet))).count("1") for octet in subnet_mask.split(".")])
    cidr_str = str(cidr)
    
    ip_range = ipG + "/" + cidr_str

    arp_result = arping(ip_range)
    
    close = raw_input()
