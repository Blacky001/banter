import gobject, pygst
pygst.require("0.10")
import gst
import gobject
import sys
import os
player1=player2=None
def serversrc(PORT_NO):
		player1=gst.parse_launch ('udpsrc port='+str(PORT_NO)+' ! application/x-rtp,media=audio, clock-rate=44100, width=16, height=16, encoding-name=L16, encoding-params=1, channels=1, channel-positions=1, payload=96 ! rtpL16depay ! alsasink sync=false')
		player1.set_state(gst.STATE_PLAYING)
		
		
def streamer(HOST_NAME,PORT_NO ):
		player2= gst.parse_launch('gconfaudiosrc ! audioconvert ! audio/x-raw-int,channels=1,depth=16,width=16,rate=44100 ! rtpL16pay  ! udpsink host='+HOST_NAME+' port='+str(PORT_NO))
		player2.set_state(gst.STATE_PLAYING)
		
		
		

