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
    - DNS (Domain Name System) is the system used to translate domain names to IP addresses. When a client reequests a website with a given domain name, it contacts the DNS recursive resolver server it has access to. This server has a buffer named DNS cache, where it stores domain &rarr; IP mappings. If the domain name is not within this cache, then the resolver contacts the DNS root zone, and chooses a root server at random. The root server responds to the resolver by providing IP info for a TLD (Top Level Domain) server in the TLD zone. Resolver contacts the TLD server, then the TLD server responds by providing the IP address of a authoritative server. 
