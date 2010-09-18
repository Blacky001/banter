# Client program

from socket import *
from chat_client import *
# Set the socket parameters
host = "192.168.1.3" #remote host
port = 21567 
buf = 1024
addr = (host,port)
host1 = "192.168.1.4" #localhost
port1 = 57877
addr1=(host1,port1)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr1)
def_msg = "===sending first message to server==="
print "\n",def_msg

# Send messages

	
data = "calling"  
serversrc(3000)
if(UDPSock.sendto(data,addr)):
		print "Sending message '",data,"'....."

# Close socket
UDPSock.close()

