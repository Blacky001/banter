from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class QOTD(Protocol):

    def connectionMade(self):
        self.transport.write(self.factory.quote+'\r\n')
	self.transport.write("An apple a day keeps the doctor away\r\n") 
	print "connection from", self.transport.getPeer()
	self.transport.loseConnection()


class QOTDFactory(Factory):
    print "hello"	
	
    protocol = QOTD

    def __init__(self, quote=None):
        self.quote = quote or 'An apple a day keeps the doctor away'

reactor.listenTCP(8007, QOTDFactory("configurable quote"))
reactor.run()

