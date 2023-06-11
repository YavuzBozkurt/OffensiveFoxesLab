from sslPlagiarism import *
from twisted.internet import reactor

reactor.listenTCP(10000, strippingFactory)
reactor.run()
