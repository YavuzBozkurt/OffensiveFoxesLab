# OffensiveFoxesLab
**Lab on Offensive 2IC80**
<p align="center">
  <img src="/markdown_images/fox_logo.png" alt="OpenAI Logo" width="30%" height="30%">
</p>

`Description` this repository contains the source code and documentation for an automated tool that performs DNS, ARP poisoning and SSL stripping attacks via the auxiliary of a GUI.  

`Lab Documentation:` https://www.overleaf.com/project/64620f7b145fd4a22f7b6f98

# Table of Contents
- [OffensiveFoxesLab](#offensivefoxeslab)
- [Table of Contents](#table-of-contents)
- [Dev. Planning](#dev-planning)
- [Attack Capabilities:](#attack-capabilities)
- [Attack Schemes](#attack-schemes)
- [GUI Scheme](#gui-scheme)
- [Attack Descriptions](#attack-descriptions)
  - [DNS Poisoning](#dns-poisoning)
  - [ARP Poisoning](#arp-poisoning)
  - [SSL Stripping](#ssl-stripping)
- [Tools](#tools)
- [Set-up](#set-up)
- [Commands](#commands)
- [Useful Links](#useful-links)


#  Dev. Planning
- [Trello Board](https://trello.com/invite/b/WSTP28RN/ATTI3e7f27a0a56151d7ad98b7b5a177b360BD2F4FB2/lab-on-offensive-2ic80-group-54-project)

# Attack Capabilities:
- `DNS Poisoning`
- `ARP Poisoning`
- `SSL Stripping`

# Attack Schemes
- [DNS poisoning scheme](https://tuenl-my.sharepoint.com/:u:/r/personal/y_bozkurt_student_tue_nl/Documents/DNS%20Poisoning%20Scheme.vsdx?d=waea298ea2c4b41cd9882ea4c142f3eda&csf=1&web=1&e=kBJcBN)
- [ARP poisoning scheme](https://tuenl-my.sharepoint.com/:u:/r/personal/y_bozkurt_student_tue_nl/Documents/ARP%20Poisoning%20Scheme.vsdx?d=wc116a15b5281439f98ed70fb7293f2c3&csf=1&web=1&e=TitkrE)
- [SSL stripping scheme](https://tuenl-my.sharepoint.com/:u:/r/personal/y_bozkurt_student_tue_nl/Documents/SSL%20Strip%20Scheme.vsdx?d=wdc038e7690fb4346967077ffc43a9b59&csf=1&web=1&e=DHzByf)

# GUI Scheme
- [Pencil Project GUI Prototyping](https://pencil.evolus.vn/)

# Attack Descriptions
## DNS Poisoning
  - `DNS (Domain Name System)` is the system used to translate domain names to IP addresses. When a client reequests a website with a given domain name, it contacts the DNS recursive resolver server it has access to. This server has a buffer named DNS cache, where it stores domain &rarr; IP mappings. If the domain name is not within this cache, then the resolver contacts the DNS root zone, and chooses a root server at random. The root server responds to the resolver by providing IP info for a TLD (Top Level Domain) server in the TLD zone. Resolver contacts the TLD server, then the TLD server responds by providing the IP address of a authoritative server. Then, the authoritative name server responds by providing the IP address of the website being requested. A demonstration is visualized down below
  <p align="center">
  <img src="/markdown_images/dns_system.png" alt="dns system" width="80%" height="80%">
  </p>
  
- `Vulnerability` of the system concerns the cache of the resolver server. If integrity of the cache is manipulated, then an attack can direct a user to his malicious website. The attacker only needs to impersonate an authoritative webserver by sending a fake DNS query response to the resolver server. Once done, the domain &rarr; Attacker IP mapping record will be in the webserver until it's TTL (Time to Live) expires, consequentially, all clients who try to access the queried domain name will be forwarded to the malicious web-page. The phenomena is demonstrated visually down below
<p align="center">
<img src="/markdown_images/dns_attack.png" alt="OpenAI Logo" width="80%" height="80%">
</p>
<p align="center">
<img src="/markdown_images/dns_consequence.png" alt="dns consequence" width="80%" height="100%">
</p>

## ARP Poisoning
  - `ARP (Adress Resolution Protocol)` is the link layer protocol used to map IP addresses of nodes (e.g. hosts, webservers, IoT, etc.) to MAC addresses, which are hardcoded 32-bit codes made by the manufactures to distinguish devices uniquely. When a node wants to communicate another node in it's LAN, it requires it's MAC address in the link layer. It first checks it's ARP cache, where mappings of IP address &rarr; MAC address are stored. If the IP address is not in this cache, then, it broadcasts a message, where it asks the MAC address for the corresponding node with the given IP address. The node that owns the IP address responds to the node with an ARP response, where it provides it's MAC address. The requesting node caches the appropriate mapping, and uses that mapping from that point on and onwards. Down below a visual demonstration of how the protocol works is provided:
   
<p align="center">
<img src="/markdown_images/arp_protocol.png" alt="arp protocol" width="80%" height="80%">
</p>

- `packets` of ARP are as below,
<p align="center">
<img src="/markdown_images/arp_packet.png" alt="arp protocol" width="80%" height="80%">
</p> 

- `Vulnerability` of the system concerns the cache of the node who is making the ARP request. If the integrity of the cache is manipulate, then the attacker can map a recorded IP address to the MAC address of a node he owns. He can do so by mimicking a legitimate ARP response. Normally, when a node that doesn't have the IP address being questioned drops the packet and does not response, the attacker can construct a packet with a spoofed IP address, send this to the requesting node so that it caches the response. Down below a visual demonstration is available
<p align="center">
<img src="/markdown_images/arp_attack.png" alt="arp attack" width="80%" height="80%">
</p>


## SSL Stripping
- `SSL (Secure Sockets Layer)` is a protocol that is used in HTTPs (HTTP seure), which is an application layer protocol that encrypts the channel between two communicating nodes. It uses certificates and public / private keys to create a chain of trust in the internet.
  
- `Vulnerability` is that in the old days, client browser would communicate with webservers via HTTP, which is not secure, and webservers would accept this. Requesting via HTTP is still possible, however well configured webservers usually demand that the client uses HTTPs instead for security purposes in response. The attacker can exploit this, by intercepting that webserver request, and establishing a secure connection, then strip off the s in HTTPs, and propogate the message to the client back, so that it looks as if the web-server has accepted HTTP communication. This attack is visualized down below.
<p align="center">
  <img src="/markdown_images/SSL_strip.png" alt="arp attack" width="65%" height="80%">
</p>

# Tools
- [Ettercap](https://www.ettercap-project.org/downloads.html)
- [Wireshark](https://www.wireshark.org/download.html)

# Set-up
| Profile                                         | IP Adress     |    MAC Address   |   OS     |
| ------------------------------------------------|:-------------:|:----------------:|:---------:
| [M1 VM (Victim)](https://www.virtualbox.org/)   | 192.168.56.101| 08:00:27:B7:C4:AF|Windows XP|
| [M2 VM (Server)](https://www.virtualbox.org/)   | 192.168.56.102| 08:00:27:CC:08:6F|Linux     |
| [M3 VM (Attacker)](https://www.virtualbox.org/) | 192.168.56.103| 08:00:27:D0:25:4B|Linux     |

# Commands

hello

# Useful Links