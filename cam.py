#!/bin/bash
gst-launch-1.0 v4l2src device=/dev/video4 ! xvimagesink

#gst-launch may be a different version, if error try changing version number.
#list video devices ls -ltrh /dev/video*



