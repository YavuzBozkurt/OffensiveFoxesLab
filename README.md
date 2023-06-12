This tool has been developed for the 2IC80 Lab on offensive computer security course of the TU/e. \
It contains an arp-poisoning attack, combined with dns-spoofing and SSL-stripping.

<img src="/markdown_images/fox_logo.png" alt="Offensive Foxes Logo" width="5%" height="5%">

# user manual
The program can be used by running the tool.py file on Linux based terminal as follows.
```
python tool.py
```
The Tool should be easy to understand enough such that user can guide himself through it. \
The user needs to consider the followings
```
- to cancel an operation on the tool dialogue, do not leave the boxes empty and press on 
  <ok> button, instead, press on the provided <cancel> button, otherwise the program may
  crash
- after completing a LAN scan, press on the provided <enter> button to close the hosts 
  found list
- to stop an ongoing attack, press Ctrl + C on your keyboard
```
There are several dependencies that need to be installed via Linux terminal, these are,
- scapy
- twisted
- netifaces
- prompt_toolkit 
\
\
You may install them using the command
```
pip3 install <dependency-name> 
```
To observe packets that are being intercepted, you may use [Wireshark](https://www.wireshark.org/)
