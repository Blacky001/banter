
import gobject, pygst
pygst.require("0.10")
import gst
import gobject
import sys
import os
import readline
import subprocess

def on_message():
	
	print "Callling.............(Press Enter to Exit)"

#HOST_NAME = raw_input("Enter Host Name: ")

#PORT_NO = raw_input("Enter Port Number: ")
#player = gst.parse_launch ('tcpserversrc host=192.168.1.9 port=3000 ! audio/x-raw-int, endianness="(int)1234", signed="(boolean)true", width="(int)16", depth="(int)16", rate="(int)44100", channels="(int)1" ! gconfaudiosink' )
pipeline=gst.Pipeline("server")
tcpsrc=gst.element_factory_make("tcpserversrc","source")
tcpsrc.set_property("host","192.168.1.9")
tcpsrc.set_property("port",3005)
pipeline.add(tcpsrc)
capsfilter=gst.element_factory_make("capsfilter","caps")
capsfilter.set_property('caps',gst.caps_from_string('audio/x-raw-int, endianness=1234 , width=16, depth=16, rate=44100, channels=1'))
pipeline.add(capsfilter)
tcpsrc.link(capsfilter)
sink=gst.element_factory_make("gconfaudiosink","sink")
pipeline.add(sink)
capsfilter.link(sink)
pipeline.set_state(gst.STATE_PLAYING)

HOST_NAME = raw_input("Enter Host Name: ")
PORT_NO = raw_input("Enter Port Number: ")
#pipeline=gst.Pipeline("client")

player = gst.parse_launch ('gconfaudiosrc ! audioconvert ! audio/x-raw-int,channels=1,depth=16,width=16,rate=44100  ! tcpclientsink host='+HOST_NAME+' port='+PORT_NO)
player.set_state(gst.STATE_PLAYING)
sys.stdin.readline()
pipeline.set_state(gst.STATE_NULL)
player.set_state(gst.STATE_NULL)
