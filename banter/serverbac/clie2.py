from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout
from twisted.internet import reactor

class Echo(Protocol):
    def dataReceived(self, data):
	global connection
        print "Server Says :",data
	connection.transport.write(raw_input("Message: "))


class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print 'Started to connect.'
    	#self.transport.write("Hello server, I am the client!\r\n")

    def buildProtocol(self, addr):
        print 'Connected.'
	print addr
        return Echo()
    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason

connection=reactor.connectTCP("localhost", 8007, EchoClientFactory())
reactor.run()

