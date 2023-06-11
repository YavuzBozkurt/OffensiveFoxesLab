from sslStripping import *
from twisted.internet import reactor
from logging import basicConfig, DEBUG

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename='ssllog.log', filemode='w')

reactor.listenTCP(10000, strippingFactory)
reactor.run()
