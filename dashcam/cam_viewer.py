import subprocess

#gst-launch may be a different version, if error try changing version number.
#list video devices ls -ltrh /dev/video*

command = "gst-launch-1.0 v4l2src device=/dev/video4 ! xvimagesink"
subprocess.call(command, shell=True)

