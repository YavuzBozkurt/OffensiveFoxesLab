from scapy.all import *
from prompt_toolkit.shortcuts import button_dialog, input_dialog

"""
import scapy.all as scapy
  
request = scapy.ARP()
  
request.pdst = '131.155.244.192,131.155.244.1'
broadcast = scapy.Ether()
  
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]
for element in clients:
    print(element[1].psrc + "      " + element[1].hwsrc)

#gw = conf.route.route("0.0.0.0")[2]

gateway = "192.168.68.1"
subnet_mask = "255.255.0.0"

cidr = sum([str(bin(int(octet))).count("1") for octet in subnet_mask.split(".")])
cidr_str = str(cidr)
    
ip_range = gateway + "/" + cidr_str

print(ip_range)
"""
urls = None

if urls:
    print("fu")
else:
    print("fm")