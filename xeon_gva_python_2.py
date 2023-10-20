# ==============================================================================
# Copyright (C) 2018-2021 Intel Corporation
#
# SPDX-License-Identifier: MIT
# ==============================================================================

import sys
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
#import cv2
from gstgva import VideoFrame
count =0
DETECT_THRESHOLD = 0.5
import json
Gst.init(sys.argv)
#import pika 
import numpy as np
import pickle
import time 

"""gst-launch-1.0   rtspsrc location=rtsp://admin:admin#123@192.168.1.168:554/cam/realmonitor?channel=1&subtype=0 latency=100  ! rtpjitterbuffer  ! queue !  rtph264depay ! h264parse ! vaapidecodebin  !  videorate ! video/x-raw,width=312,height=312 ,framerate=1/1  ! videoconvert ! capsfilter  caps="video/x-raw,format=I420"  ! gvapython module=test_gvapython.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"1\\\"} ! fakesink"""

class custom_accumulator():

    def __init__(self,arg):
        self.temp_array = []
        # self.count = 0
        try:

            self.temp_dict = arg
            # {\\\"cam_no\\\":\\\"1\\\",\\\"accumulate_frames_no\\\":\\\"16\\\",\\\"rabbit_mq_pipeline\\\":\\\"fire_detection\\\"}
            # print(self.temp_dict["cam_no"],self.temp_dict["accumulate_frames_no"],self.temp_dict["rabbit_mq_name"])
            self.temp_dict["accumulate_frames_no"]=16
            print(self.temp_dict)
        except Exception as ec :
            print(ec)
#        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#        self.channel_temp = self.connection.channel()

    def process_frame(self,frame):

        # width = frame.video_info().width
        # height = frame.video_info().height
        with frame.data() as np_frame:
            # print(np_frame.shape,width,height,frame.video_info().finfo.format)
            # final_frame = cv2.cvtColor(np_frame, cv2.COLOR_YUV420p2RGB)
            final_frame = np_frame

            print(final_frame.shape,len(self.temp_array),"------------------",self.temp_dict["cam_no"])
            if len(self.temp_array) < self.temp_dict["accumulate_frames_no"]:
                self.temp_array.append(final_frame)
            elif len(self.temp_array) ==self.temp_dict["accumulate_frames_no"]:
                print("hurray","temp arrray filled ")
                # data = np.array(self.temp_array)
                # stacked_images_as_bytes = pickle.dumps(data)
                # try:

                #     self.channel_temp.basic_publish(exchange='',
                #             routing_key='fire_detection',
                #             properties=pika.BasicProperties(
                #                 headers={'camera_no': str(self.temp_dict['cam_no']),'current_time':str(time.time())} # Add a key/value header
                #             ),
                #             body=stacked_images_as_bytes)
                # except Exception as e:
                #     print("waht hapapedn",self.temp_dict["cam_no"],e)


                self.temp_array = []

            elif len(self.temp_array) >self.temp_dict["accumulate_frames_no"]:
                # data = np.array(self.temp_array[:16])
                # stacked_images_as_bytes = pickle.dumps(data)
                # try:

                #     self.channel_temp.basic_publish(exchange='',
                #             routing_key='fire_detection',
                #             properties=pika.BasicProperties(
                #                 headers={'camera_no': str(self.temp_dict['cam_no']),'current_time':str(time.time())} # Add a key/value header
                #             ),
                #             body=stacked_images_as_bytes)
                # except Exception as e:
                #     print("waht hapapedn",self.temp_dict["cam_no"],e)
                self.temp_array = self.temp_array[16:]

            # cv2.imwrite("sample_{}.png".format(count),final_frame)
        return True
