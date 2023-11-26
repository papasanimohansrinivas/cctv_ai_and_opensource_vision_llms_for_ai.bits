# ==============================================================================
# Copyright (C) 2018-2021 Intel Corporation
#
# SPDX-License-Identifier: MIT
# ==============================================================================
import copy
import sys
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
# import cv2
from gstgva import VideoFrame
# count =0
# DETECT_THRESHOLD = 0.5
# import json
Gst.init(sys.argv)
import pika 
import numpy as np
import pickle
import time 

"""gst-launch-1.0   rtspsrc location=rtsp://admin:admin#123@192.self.temp_dict["accumulate_frames_no"]8.1.self.temp_dict["accumulate_frames_no"]8:554/cam/realmonitor?channel=1&subtype=0 latency=100  ! rtpjitterbuffer  ! queue !  rtph264depay ! h264parse ! vaapidecodebin  !  videorate ! video/x-raw,width=312,height=312 ,framerate=1/1  ! videoconvert ! capsfilter  caps="video/x-raw,format=I420"  ! gvapython module=test_gvapython.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"1\\\"} ! fakesink"""

class custom_accumulator():

    def __init__(self,arg):
        self.temp_array = []
        # self.count = 0
        try:
            self.a = time.time()

            self.temp_dict = arg
            print(self.temp_dict)
            # {\\\"cam_no\\\":\\\"1\\\",\\\"accumulate_frames_no\\\":\\\"self.temp_dict["accumulate_frames_no"]\\\",\\\"rabbit_mq_pipeline\\\":\\\"fire_detection\\\"}
            # print(self.temp_dict["cam_no"],self.temp_dict["accumulate_frames_no"],self.temp_dict["rabbit_mq_name"])
            self.temp_dict["accumulate_frames_no"]=int(self.temp_dict['accumulate_frames_no'])
            self.routing_key = self.temp_dict['rabbitmq_queue_name']
            print(self.temp_dict,"mohan")
        except Exception as ec :
            print(ec.__str__(),"what the fuck error")
        credentials = pika.PlainCredentials('cctv_ai', 'idmohanceo@ai.bits')
        try:
                self.connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',credentials=credentials,client_properties={"connection_name":self.temp_dict["cam_no"]}))
        except Exception as  excp:
                print(excp.__str__(),"what the actual fuck bro")

        # self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel_temp = self.connection.channel()
        self.numpy_stack_image = None

    def process_frame(self,frame):

        # width = frame.video_info().width
        # height = frame.video_info().height
        with frame.data() as np_frame:
            b = time.time()
            print("diff",b-self.a,"hoooo")
            self.a = b
            # print(np_frame.shape,width,height,frame.video_info().finfo.format)
            # final_frame = cv2.cvtColor(np_frame, cv2.COLOR_YUV420p2RGB)
            final_frame = np_frame
            if self.numpy_stack_image is None:
                self.numpy_stack_image = np.expand_dims(copy.deepcopy(np_frame), axis= 0)
            elif self.numpy_stack_image.shape[0]<self.temp_dict["accumulate_frames_no"]:
                self.numpy_stack_image = np.append(self.numpy_stack_image, np.expand_dims(copy.deepcopy(np_frame), axis= 0) , axis= 0)
            elif self.numpy_stack_image.shape[0]==self.temp_dict["accumulate_frames_no"]:
                stacked_images_as_bytes = pickle.dumps(self.numpy_stack_image)
                # c=0
                # for img in list(self.numpy_stack_image):
                #     cv2.imwrite("/home/mohan/backup_xeon_decoding_server_sep_21_2022/trial_{}_{}.png".format(self.temp_dict['cam_no'],c+1),img)
                #     c+=1
                
                try:

                    self.channel_temp.basic_publish(exchange='',
                            routing_key=self.routing_key,
                            properties=pika.BasicProperties(
                                headers={'camera_no': str(self.temp_dict['cam_no']),'current_time':str(time.time())} # Add a key/value header
                            ),
                            body=stacked_images_as_bytes)
                except Exception as e:
                    
                    print("waht hapapedn",self.temp_dict["cam_no"],e)
                    print("reconnecting ...")
                    credentials = pika.PlainCredentials('cctv_ai', 'idmohanceo@ai.bits')
                    self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials,client_properties={"connection_name":self.temp_dict["cam_no"]}))
                    # self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
                    self.channel_temp = self.connection.channel()
                self.numpy_stack_image = None

            elif self.numpy_stack_image.shape[0]>self.temp_dict["accumulate_frames_no"]:
                stacked_images_as_bytes = pickle.dumps(self.numpy_stack_image[:self.temp_dict["accumulate_frames_no"]])
                try:

                    self.channel_temp.basic_publish(exchange='',
                            routing_key=self.routing_key,
                            properties=pika.BasicProperties(
                                headers={'camera_no': str(self.temp_dict['cam_no']),'current_time':str(time.time())} # Add a key/value header
                            ),
                            body=stacked_images_as_bytes)
                except Exception as e:
                    
                    print("waht hapapedn",self.temp_dict["cam_no"],e)
                    print("reconnecting ...")
                    credentials = pika.PlainCredentials('cctv_ai', 'idmohanceo@ai.bits')
                    self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials,client_properties={"connection_name":self.temp_dict["cam_no"]}))
                    # self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
                    self.channel_temp = self.connection.channel()
                self.numpy_stack_image = self.numpy_stack_image[self.temp_dict["accumulate_frames_no"]:]

            print(frame.video_info().to_caps().to_string(),"----yooy")
            if self.numpy_stack_image is not None:

                print(self.numpy_stack_image.shape,"------------------",self.temp_dict["cam_no"])
            # if len(self.temp_array) < self.temp_dict["accumulate_frames_no"]:
            #     self.temp_array.append(final_frame)
            # elif len(self.temp_array) ==self.temp_dict["accumulate_frames_no"]:
            #     print("hurray","temp arrray filled ")
            #     data = np.array(self.temp_array)
            #     stacked_images_as_bytes = pickle.dumps(data)
            #     try:

            #         self.channel_temp.basic_publish(exchange='',
            #                 routing_key='fire_detection',
            #                 properties=pika.BasicProperties(
            #                     headers={'camera_no': str(self.temp_dict['cam_no']),'current_time':str(time.time())} # Add a key/value header
            #                 ),
            #                 body=stacked_images_as_bytes)
            #     except Exception as e:
                    
            #         print("waht hapapedn",self.temp_dict["cam_no"],e)
            #         print("reconnecting ...")

            #         self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            #         self.channel_temp = self.connection.channel()


            #     self.temp_array = []

            # elif len(self.temp_array) >self.temp_dict["accumulate_frames_no"]:
            #     data = np.array(self.temp_array[:self.temp_dict["accumulate_frames_no"]])
            #     stacked_images_as_bytes = pickle.dumps(data)
            #     try:

            #         self.channel_temp.basic_publish(exchange='',
            #                 routing_key='fire_detection',
            #                 properties=pika.BasicProperties(
            #                     headers={'camera_no': str(self.temp_dict['cam_no']),'current_time':str(time.time())} # Add a key/value header
            #                 ),
            #                 body=stacked_images_as_bytes)
            #     except Exception as e:
            #         print("waht hapapedn",self.temp_dict["cam_no"],e)
            #         print("reconnecting ...")
            #         self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            #         self.channel_temp = self.connection.channel()
                    
            #     self.temp_array = self.temp_array[self.temp_dict["accumulate_frames_no"]:]

            # cv2.imwrite("sample_{}.png".format(count),final_frame)
        return True
