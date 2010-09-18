from socket import *
from chat_client import *

# Set the socket parameters
host = "192.168.1.3"
port = 21567
buf = 1024
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)
def_msg = "======================================================";

print "\n",def_msg

while 1:	
	data,addr = UDPSock.recvfrom(buf)
	if data in "calling":
	
			print addr
			addr=(addr[0],21567)
			print "\nReceived message '", data,"'"
			data="accepted"
			streamer(addr[0],3000)
			serversrc(5000)
			if(UDPSock.sendto(data,addr)):
				print "Sending message '",data,"'....."
	else:	
			streamer(addr[0],5000)
			print "to be edited"
		


# Close socket
UDPSock.close()

