def nameorso(pkt):

    if pkt[TCP].payload:
        raw = packet[TCP].payload.load
        if "GET" in raw:
            print(raw)
    return

def sslStripping(a):
    
    hwA = a["attacker MAC"]
    ipV = a["victim MAC"]
    hwV = a["victim IP"]
    ipG = a["gateway IP"]

    while(True):
    
        pkt = sniff(filter="tcp port 80", prn=nameorso)[0]
        