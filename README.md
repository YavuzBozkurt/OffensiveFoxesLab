# OffensiveFoxesLab
Lab on Offensive 2IC80
<p align="center">
  <img src="https://i.pinimg.com/originals/41/ab/b9/41abb961ee0dd2491841d278392893b1.jpg" alt="OpenAI Logo" width="50%" height="50%">
</p>

Lab Documentation: https://www.overleaf.com/project/64620f7b145fd4a22f7b6f98

# Project Attack Capabilities:
- DNS Poisoning
- ARP Poisoning
- SSL Stripping

# Project Attack Descriptions
- DNS Poisoning
    - DNS (Domain Name System): is the system used to translate domain names to IP addresses. When a client reequests a website with a given domain name, it contacts the DNS recursive resolver server it has access to. This server has a buffer named DNS cache, where it stores domain &rarr; IP mappings. If the domain name is not within this cache, then the resolver contacts the DNS root zone, and chooses a root server at random. The root server responds to the resolver by providing IP info for a TLD (Top Level Domain) server in the TLD zone. Resolver contacts the TLD server, then the TLD server responds by providing the IP address of a authoritative server. Then, the authoritative name server responds by providing the IP address of the website being requested. A demonstration is visualized down below
    <p align="center">
    <img src="/markdown_images/dns_system.png" alt="dns system" width="80%" height="80%">
    </p>
    - Vulnerability: of the system concerns the cache of the resolver server. If integrity of the cache is manipulated, then an attack can direct a user to his malicious website. The attacker only needs to impersonate an authoritative webserver by sending a fake DNS query response to the resolver server. Once done, the domain &rarr; Attacker IP mapping record will be in the webserver until it's TTL (Time to Live) expires, consequentially, all clients who try to access the queried domain name will be forwarded to the malicious web-page. The phenomena is demonstrated visually down below
   	<p align="center">
    <img src="/markdown_images/dns_attack.png" alt="OpenAI Logo" width="80%" height="80%">
    </p>
    <p align="center">
    <img src="/markdown_images/dns_consequence.png" alt="dns consequence" width="80%" height="100%">
    </p>
- ARP Poisoning
    - ARP (Adress Resolution Protocol): is the link layer protocol used to map IP addresses of nodes (e.g. hosts, webservers, IoT, etc.) to MAC addresses, which are hardcoded 32-bit codes made by the manufactures to distinguish devices uniquely. When a node wants to communicate another node in it's LAN, it requires it's MAC address in the link layer. It first checks it's ARP cache, where mappings of IP address &rarr; MAC address are stored. If the IP address is not in this cache, then, it broadcasts a message, where it asks the MAC address for the corresponding node with the given IP address. The node that owns the IP address responds to the node with an ARP response, where it provides it's MAC address. The requesting node caches the appropriate mapping, and uses that mapping from that point on and onwards. Down below a visual demonstration of how the protocol works is provided:
    <p align="center">
    <img src="/markdown_images/arp_protocol.png" alt="arp protocol" width="80%" height="80%">
    </p>
    - packets: of ARP is as below,
    <p align="center">
    <img src="/markdown_images/arp_packet.png" alt="arp protocol" width="80%" height="80%">
    </p> 
    - Vulnerability: of the system concerns the cache of the node who is making the ARP request. If the integrity of the cache is manipulate, then the attacker can map a recorded IP address to the MAC address of a node he owns. He can do so by mimicking a legitimate ARP response. Normally, when a node that doesn't have the IP address being questioned drops the packet and does not response, the attacker can construct a packet with a spoofed IP address, send this to the requesting node so that it caches the response. Down below a visual demonstration is available
    <p align="center">
    <img src="/markdown_images/arp_attack.png" alt="arp attack" width="80%" height="80%">
    </p>
- SSL Stripping