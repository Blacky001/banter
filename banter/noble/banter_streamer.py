#!/usr/bin/env python
# -=- encoding: utf-8 -=-

import gobject, pygst
pygst.require("0.10")
import gst
import gobject
import sys
import os
import readline

HOST_NAME = raw_input("Enter Host Name: ")
PORT_NO = raw_input("Enter Port Number: ")
pipeline=gst.Pipeline("client")

player = gst.parse_launch ('gconfaudiosrc ! audioconvert ! audio/x-raw-int,channels=1,depth=16,width=16,rate=44100  ! tcpclientsink host='+HOST_NAME+' port='+PORT_NO)
player.set_state(gst.STATE_PLAYING)
print "Callling.............(Press Enter to Exit)"
sys.stdin.readline()
player.set_state(gst.STATE_NULL)
