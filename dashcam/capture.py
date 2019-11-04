#!/usr/bin/env python

import subprocess
import datetime
import os
import cam_viewer

ROOT_PATH = os.getenv("ROOT_PATH", "")
RECORDINGS_PATH = os.getenv("RECORDINGS_PATH", "recordings")
DATE_FMT = "%Y_%m_%d_%H_%M_%S"
SEGMENT_TIME = 10
ENCODING = os.getenv("ENCODING", "copy")

if(os.path.exists(RECORDINGS_PATH)):
    list_devices = 'ls -ltrh /dev/video'
    os.system(list_devices)

    recording_path = os.path.join(ROOT_PATH, RECORDINGS_PATH)
    new_dir = datetime.datetime.now().strftime(DATE_FMT)
    segments_path = os.path.join(recording_path, new_dir + "_%03d.avi")
    command = "ffmpeg -i /dev/video4 -c:v {} -segment_time {} -f segment {}".format(ENCODING, SEGMENT_TIME, segments_path)
    subprocess.call(command, shell=True)

    

else:
    os.mkdir(RECORDINGS_PATH)



