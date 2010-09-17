from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class Echo(Protocol):

    def connectionMade(self):
        self.transport.write(self.factory.quote+'\r\n')
	self.transport.write("An apple a day keeps the doctor away\r\n") 
	print "connection from", self.transport.getPeer()
	
    def dataReceived(self,data):
	print "Client says :",data
	self.transport.write("ok")


class EchoFactory(Factory):	
	
    protocol = Echo

    def __init__(self, quote=None):
        self.quote = quote or 'An apple a day keeps the doctor away'

reactor.listenTCP(8007, EchoFactory("configurable quote"))
reactor.run()

