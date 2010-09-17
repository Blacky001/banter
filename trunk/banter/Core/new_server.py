#!/usr/bin/env python
# -=- encoding: utf-8 -=-

import gobject, pygst
pygst.require("0.10")
import gst
import gobject
import sys
import os
import readline
import subprocess


#HOST_NAME = raw_input("Enter Host Name: ")

#PORT_NO = raw_input("Enter Port Number: ")
pipeline=gst.Pipeline("server")
tcpsrc=gst.element_factory_make("tcpserversrc","source")
tcpsrc.set_property("host",'192.168.1.8')
tcpsrc.set_property("port",3000)
pipeline.add(tcpsrc)
capsfilter=gst.element_factory_make("capsfilter","caps")
capsfilter.set_property('caps',gst.caps_from_string('audio/x-raw-int, endianness=1234 , width=16, depth=16, rate=44100, channels=1'))
pipeline.add(capsfilter)
tcpsrc.link(capsfilter)
sink=gst.element_factory_make("gconfaudiosink","sink")
pipeline.add(sink)
capsfilter.link(sink)
pipeline.set_state(gst.STATE_PLAYING)
sys.stdin.readline()
pipeline.set_state(gst.STATE_NULL)
