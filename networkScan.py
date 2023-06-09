from scapy.all import *

def auto_scan():
    gw = conf.route.route("0.0.0.0")[2]

    ip_range = gw + "/24"

    arp_result = arping(ip_range)
    
def manual_scan(gateway,subnet_mask):

    cidr = sum([str(bin(int(octet))).count("1") for octet in subnet_mask.split(".")])
    cidr_str = str(cidr)
    
    ip_range = gateway + "/" + cidr_str

    arp_result = arping(ip_range)