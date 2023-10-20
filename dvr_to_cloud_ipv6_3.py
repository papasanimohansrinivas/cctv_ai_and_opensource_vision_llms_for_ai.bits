# coding=utf-8
import sys
from ctypes import *
import numpy as np
#import cv2
from NetSDK.NetSDK import NetClient
from NetSDK.SDK_Callback import fDisConnect, fHaveReConnect, fDecCBFun, fRealDataCallBackEx2
from NetSDK.SDK_Enum import SDK_RealPlayType, EM_LOGIN_SPAC_CAP_TYPE, EM_REALDATA_FLAG
from NetSDK.SDK_Struct import C_LLONG, sys_platform, NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY, NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY, PLAY_FRAME_INFO

#import PIL.Image as Image
from io import StringIO
import io
import subprocess as sp
import shlex
#from PIL import Image
import threading
# import av
import pickle 
# import pika
import time 
from queue import Queue
import socket
import os 
import configparser
import sys

#import cv2
count  = 0
class RealPlayDemo:
    def __init__(self):

        # NetSDK用到的相关变量和回调
        self.loginID = C_LLONG()
        self.playID = C_LLONG()
        self.playID_1 = C_LLONG()
        self.playID_2 = C_LLONG()
        self.playID_3 = C_LLONG()
        self.playID_4 = C_LLONG()
        self.playID_5 = C_LLONG()
        self.playID_6 = C_LLONG()
        self.playID_7 = C_LLONG()
        self.playID_8 = C_LLONG()
        self.playID_9 = C_LLONG()
        self.playID_10 = C_LLONG()
        self.playID_11 = C_LLONG()
        self.playID_12 = C_LLONG()
        self.playID_13 = C_LLONG()
        self.playID_14 = C_LLONG()
        self.playID_15 = C_LLONG()
        self.freePort = c_int()
        self.m_DisConnectCallBack = fDisConnect(self.DisConnectCallBack)
        self.m_ReConnectCallBack = fHaveReConnect(self.ReConnectCallBack)
        self.m_RealDataCallBack = fRealDataCallBackEx2(self.RealDataCallBack)

        self.m_RealDataCallBack_1 = fRealDataCallBackEx2(self.RealDataCallBack_1)
        self.m_RealDataCallBack_2 = fRealDataCallBackEx2(self.RealDataCallBack_2)
        self.m_RealDataCallBack_3 = fRealDataCallBackEx2(self.RealDataCallBack_3)
        self.m_RealDataCallBack_4 = fRealDataCallBackEx2(self.RealDataCallBack_4)
        self.m_RealDataCallBack_5 = fRealDataCallBackEx2(self.RealDataCallBack_5)
        self.m_RealDataCallBack_6 = fRealDataCallBackEx2(self.RealDataCallBack_6)
        self.m_RealDataCallBack_7 = fRealDataCallBackEx2(self.RealDataCallBack_7)
        self.m_RealDataCallBack_8 = fRealDataCallBackEx2(self.RealDataCallBack_8)
        self.m_RealDataCallBack_9 = fRealDataCallBackEx2(self.RealDataCallBack_9)
        self.m_RealDataCallBack_10 = fRealDataCallBackEx2(self.RealDataCallBack_10)
        self.m_RealDataCallBack_11 = fRealDataCallBackEx2(self.RealDataCallBack_11)
        self.m_RealDataCallBack_12 = fRealDataCallBackEx2(self.RealDataCallBack_12)
        self.m_RealDataCallBack_13 = fRealDataCallBackEx2(self.RealDataCallBack_13)
        self.m_RealDataCallBack_14 = fRealDataCallBackEx2(self.RealDataCallBack_14)
        self.m_RealDataCallBack_15 = fRealDataCallBackEx2(self.RealDataCallBack_15)

        # 获取NetSDK对象并初始化
        self.sdk = NetClient()
        self.sdk.InitEx(self.m_DisConnectCallBack)
        self.sdk.SetAutoReconnect(self.m_ReConnectCallBack)
        # self.sdk.InitEx(None)
        # self.sdk.SetAutoReconnect(None)
        config = configparser.ConfigParser()

        ini_file_name = sys.argv[1]

        config.read(ini_file_name)

        self.client_name = config.get("client_details","client_name")

        self.static_ip = config.get("client_details","static_ip")

        self.user_name  = config.get("client_details","username")

        self.password_  = config.get("client_details","password")

        self.port_  = int(config.get("client_details","port"))

        self.cam_list = [int(cam_num_from_list) for cam_num_from_list in config.get("client_details","cam_list").split(",")]

        self.udp_ports_list = [int(udp_port_num) for udp_port_num in  config.get("client_details","udp_ports").split(",")]

        self.udp_port_1 = None
        self.udp_port_2 = None
        self.udp_port_3 = None
        self.udp_port_4 = None
        self.udp_port_5 = None
        self.udp_port_6 = None
        self.udp_port_7 = None
        self.udp_port_8 = None
        self.udp_port_9 = None
        self.udp_port_10 = None
        self.udp_port_11 = None
        self.udp_port_12 = None
        self.udp_port_13 = None
        self.udp_port_14 = None
        self.udp_port_15 = None
        self.udp_port_16 = None
        # self.


        self.ip = ''
        self.port = 0
        self.username = ''
        self.password = ''
        if 1 in self.cam_list:

            self.channel = 0
            # self.cam_list.index(1)
            self.udp_port_1 = self.udp_ports_list[self.cam_list.index(1)]
        else:
            self.channel = None
        
        self.streamtype = 0
        if 2 in self.cam_list:
            self.channel_1 = 1
            self.udp_port_2 = self.udp_ports_list[self.cam_list.index(2)]
        else:
            self.channel_1 = None
        
        self.streamtype_1 = 0 
        if 3 in self.cam_list:
            self.channel_2 = 2

            self.udp_port_3 = self.udp_ports_list[self.cam_list.index(3)]
        else:
            self.channel_2 = None
        
        self.streamtype_1 = 0

        if 4 in self.cam_list:
            self.channel_3 = 3

            self.udp_port_4 = self.udp_ports_list[self.cam_list.index(4)]
        else:
            self.channel_3 = None
        

        self.streamtype_1 = 0
        if 5 in self.cam_list:

            self.channel_4 = 4

            self.udp_port_5 = self.udp_ports_list[self.cam_list.index(5)]
        else:
            self.channel_4 = None

        self.streamtype_1 = 0

        if 6 in self.cam_list:
            self.channel_5 = 5

            self.udp_port_6 = self.udp_ports_list[self.cam_list.index(6)]
        else:
            self.channel_5 = None

        self.streamtype_1 = 0
        if 7 in self.cam_list:
            self.channel_6 = 6

            self.udp_port_7 = self.udp_ports_list[self.cam_list.index(7)]
        else:
            self.channel_6 = None
        
        self.streamtype_1 = 0

        if 8 in self.cam_list:
            self.channel_7 = 7

            self.udp_port_8 = self.udp_ports_list[self.cam_list.index(8)]
        else:
            self.channel_7 = None
        self.streamtype_1 = 0
        if 9 in self.cam_list:
            self.channel_8 = 8

            self.udp_port_9 = self.udp_ports_list[self.cam_list.index(9)]
        else:
            self.channel_8 = None
        self.streamtype_1 = 0
        if 10 in self.cam_list:

            self.channel_9 = 9

            self.udp_port_10 = self.udp_ports_list[self.cam_list.index(10)]
        else:
            self.channel_9 = None
        self.streamtype_1 = 0

        if 11 in self.cam_list:
            self.channel_10 = 10

            self.udp_port_11 = self.udp_ports_list[self.cam_list.index(11)]
        else:
            self.channel_10 = None

        self.streamtype_1 = 0


        if 12 in self.cam_list:

            self.channel_11 = 11

            self.udp_port_12 = self.udp_ports_list[self.cam_list.index(12)]
        else:
            self.channel_11 = None

        self.streamtype_1 = 0

        if 13 in self.cam_list:
            
            self.channel_12 = 12

            self.udp_port_13 = self.udp_ports_list[self.cam_list.index(13)]
        else:
            self.channel_12 = None
        self.streamtype_1 = 0

        if 14 in self.cam_list:
            self.channel_13 = 13

            self.udp_port_14 = self.udp_ports_list[self.cam_list.index(14)]
        else:
            self.channel_13 = None
        
        self.streamtype_1 = 0

        if 15 in self.cam_list:
            self.channel_14 = 14

            self.udp_port_15 = self.udp_ports_list[self.cam_list.index(15)]
        else:
            self.channel_14 = None

        self.streamtype_1 = 0

        if 16 in self.cam_list:
            self.channel_15 = 15

            self.udp_port_16 = self.udp_ports_list[self.cam_list.index(16)]
        else:
            self.channel_15 = None

        self.streamtype_1 = 0



        


        self.sock_1 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

        self.sock_1.setblocking(0)

        self.sock_1#("/tmp/cam_1.s")

        self.sock_2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_2.setblocking(0)
        self.sock_2#("/tmp/cam_2.s")

        self.sock_3 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_3.setblocking(0)
        self.sock_3#("/tmp/cam_3.s")

        self.sock_4 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_4.setblocking(0)
        self.sock_4#("/tmp/cam_4.s")

        self.sock_5 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_5.setblocking(0)
        self.sock_5#("/tmp/cam_5.s")

        self.sock_6 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_6.setblocking(0)
        self.sock_6#("/tmp/cam_6.s")

        self.sock_7 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_7.setblocking(0)
        self.sock_7#("/tmp/cam_7.s")

        self.sock_8 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_8.setblocking(0)
        self.sock_8#("/tmp/cam_8.s")

        self.sock_9 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_9.setblocking(0)
        self.sock_9#("/tmp/cam_9.s")

        self.sock_10 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_10.setblocking(0)
        self.sock_10#("/tmp/cam_10.s")

        self.sock_11 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_11.setblocking(0)
        self.sock_11#("/tmp/cam_11.s")

        self.sock_12 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_12.setblocking(0)
        self.sock_12#("/tmp/cam_12.s")

        self.sock_13 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_13.setblocking(0)
        self.sock_13#("/tmp/cam_13.s")

        self.sock_14 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_14.setblocking(0)
        self.sock_14#("/tmp/cam_14.s")

        self.sock_15 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_15.setblocking(0)
        self.sock_15#("/tmp/cam_15.s")

        self.sock_16 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_16.setblocking(0)
        self.sock_16#("/tmp/cam_16.s")



    def get_login_info(self):
        print("请输入登录信息(Please input login info)")
        print("")
        # self.ip = input('地址(IP address):')
        # self.port = int(input('端口(port):'))
        # self.username = input('用户名(username):')
        # self.password = input('密码(password):')

        #self.ip = "2406:b400:d4:6752:2a18:fdff:fe02:ecfb"
        # self.ip  = "2406:b400:d4:5048:2a18:fdff:fe02:ecfb"
        # "2406:B400:D4:7DCD:28:18:fd:07:73:16"
        # "2406:B400:D4:7DCD:2a18:fdff:fe07:7316"
        # "2406:B400:D4:7DCD:2a18:fdff:fe02:ecfb"
        self.ip = self.static_ip
        self.port = self.port_
        self.username = self.user_name
        self.password = self.password_

    def login(self):
        if not self.loginID:
            stuInParam = NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
            stuInParam.dwSize = sizeof(NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY)
            stuInParam.szIP = self.ip.encode()
            stuInParam.nPort = self.port
            stuInParam.szUserName = self.username.encode()
            stuInParam.szPassword = self.password.encode()
            stuInParam.emSpecCap = EM_LOGIN_SPAC_CAP_TYPE.TCP
            # stuInParam.emSpecCap = EM_LOGIN_SPAC_CAP_TYPE.P2P
            # stuInParam.emSpecCap = 19
            
            # stuInParam.pCapParam = "CP7H08C2FPAZ01990"

            stuOutParam = NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
            stuOutParam.dwSize = sizeof(NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)
            print(stuInParam)
            self.loginID, device_info, error_msg = self.sdk.LoginWithHighLevelSecurity(stuInParam, stuOutParam)
            if self.loginID != 0:
                print("WAIT !",device_info)
                print("登录成功(Login succeed). 通道数量(Channel num):" + str(device_info.nChanNum))
                return True
            else:
                print("登录失败(Login failed). " + error_msg)
                return False

    def logout(self):
        if self.loginID:
            if self.playID:
                self.sdk.StopRealPlayEx(self.playID)
                self.playID = 0

            self.sdk.Logout(self.loginID)
            self.loginID = 0
        print("登出成功(Logout succeed)")

    def get_realplay_info(self):
        print("")
        print("请输入实时监视信息(Please input realplay info)")

    def realplay(self):
        if not self.playID:
            if self.streamtype == 0:

                #stream_type = SDK_RealPlayType.Realplay_1

                stream_type = SDK_RealPlayType.Realplay_1
            else:
                stream_type = SDK_RealPlayType.Realplay_1
            print(stream_type,"stream type")
            if self.channel is not None:

                self.playID = self.sdk.RealPlayEx(self.loginID, self.channel, 0, stream_type)
            if self.channel_1 is not None:
                self.playID_1 = self.sdk.RealPlayEx(self.loginID, self.channel_1, 0, stream_type)
            if self.channel_2 is not None:
                self.playID_2 = self.sdk.RealPlayEx(self.loginID, self.channel_2, 0, stream_type)
            if self.channel_3 is not None:
                self.playID_3 = self.sdk.RealPlayEx(self.loginID, self.channel_3, 0, stream_type)
            if self.channel_4 is not None:
                self.playID_4 = self.sdk.RealPlayEx(self.loginID, self.channel_4, 0, stream_type)
            if self.channel_5 is not None:
                self.playID_5 = self.sdk.RealPlayEx(self.loginID, self.channel_5, 0, stream_type)
            if self.channel_6 is not None:
                self.playID_6 = self.sdk.RealPlayEx(self.loginID, self.channel_6, 0, stream_type)
            if self.channel_7 is not None:
                self.playID_7 = self.sdk.RealPlayEx(self.loginID, self.channel_7, 0, stream_type)
            if self.channel_8 is not None:
                self.playID_8 = self.sdk.RealPlayEx(self.loginID, self.channel_8, 0, stream_type)
            if self.channel_9 is not None:
                self.playID_9 = self.sdk.RealPlayEx(self.loginID, self.channel_9, 0, stream_type)
            if self.channel_10 is not None:
                self.playID_10 = self.sdk.RealPlayEx(self.loginID, self.channel_10, 0, stream_type)
            if self.channel_11 is not None:
                self.playID_11 = self.sdk.RealPlayEx(self.loginID, self.channel_11, 0, stream_type)
            if self.channel_12 is not None:
                self.playID_12 = self.sdk.RealPlayEx(self.loginID, self.channel_12, 0, stream_type)
            if self.channel_13 is not None:
                self.playID_13 = self.sdk.RealPlayEx(self.loginID, self.channel_13, 0, stream_type)
            if self.channel_14 is not None:
                self.playID_14 = self.sdk.RealPlayEx(self.loginID, self.channel_14, 0, stream_type)
            if self.channel_15 is not None:
                self.playID_15 = self.sdk.RealPlayEx(self.loginID, self.channel_15, 0, stream_type)


            if self.channel is not None and  self.playID!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID, self.m_RealDataCallBack, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_1 is not None and  self.playID_1!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_1, self.m_RealDataCallBack_1, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_2 is not None and  self.playID_2!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_2, self.m_RealDataCallBack_2, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_3 is not None and  self.playID_3!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_3, self.m_RealDataCallBack_3, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_4 is not None and  self.playID_4!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_4, self.m_RealDataCallBack_4, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_5 is not None and  self.playID_5!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_5, self.m_RealDataCallBack_5, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_6 is not None and  self.playID_6!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_6, self.m_RealDataCallBack_6, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_7 is not None and  self.playID_7!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_7, self.m_RealDataCallBack_7, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_8 is not None and  self.playID_8!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_8, self.m_RealDataCallBack_8, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_9 is not None and  self.playID_9!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_9, self.m_RealDataCallBack_9, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_10 is not None and  self.playID_10!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_10, self.m_RealDataCallBack_10, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_11 is not None and  self.playID_11!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_11, self.m_RealDataCallBack_11, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_12 is not None and  self.playID_12!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_12, self.m_RealDataCallBack_12, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_13 is not None and  self.playID_13!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_13, self.m_RealDataCallBack_13, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_14 is not None and  self.playID_14!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_14, self.m_RealDataCallBack_14, None, EM_REALDATA_FLAG.RAW_DATA  )
            if self.channel_15 is not None and  self.playID_15!=0 :
                self.sdk.SetRealDataCallBackEx2(self.playID_15, self.m_RealDataCallBack_15, None, EM_REALDATA_FLAG.RAW_DATA  )

            verification_dict = {1:self.playID,2:self.playID_1,3:self.playID_2,4:self.playID_3,5:self.playID_4,6:self.playID_5,7:self.playID_6,8:self.playID_7,9:self.playID_8,10:self.playID_9,11:self.playID_10,12:self.playID_11,13:self.playID_12,14:self.playID_13,15:self.playID_14,16:self.playID_15}
            for temp_cam in self.cam_list:
                if verification_dict[temp_cam]==0:
                    print("实时监视失败(RealPlay fail). "+ self.sdk.GetLastErrorMessage())
                    return False
            print("实时监视成功(RealPlay succeed).")
            return True
                

    def stop_realplay(self):
        if self.playID:
            self.sdk.StopRealPlayEx(self.playID)
            self.playID = 0
        print("停止实时监视成功(Stop RealPlay succeed).")

    # 实现断线回调函数功能
    def DisConnectCallBack(self, lLoginID, pchDVRIP, nDVRPort, dwUser):
        print("实时监视(RealPlay)-离线(OffLine)")
        print("starting to shut down .....")
        #sys.exit(1)
        # raise Exception("system went offline")

    # 实现断线重连回调函数功能
    def ReConnectCallBack(self, lLoginID, pchDVRIP, nDVRPort, dwUser):
        print("实时监视(RealPlay)-在线(OnLine)")
        print("starting to shutdown ... in reconnect callback..")
        #sys.exit(1)
        # raise Exception("need to reconnect again to get all cameras back online")

    # 拉流回调函数功能
    def RealDataCallBack(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(1)
        if lRealHandle == self.playID:
            if dwDataType == 0:
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                # # print("IS YUV ",dwDataType,param)
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                # if dwBufSize > 10000:
                # buffer_2 = io.BytesIO()
                # buffer_2.write(bytes(data_buffer))
                # buffer_2.seek(0)
                # try :
                #     container = av.open(buffer_2, mode='r')
                #     amount  = self.sock_1.sendto(data_buffer, ("localhost",10000))
                #     print(1,amount,dwBufSize,"<-------","sent")
                
                # except Exception as err1:
                #     pass
                #     # print(err1,1,dwBufSize, "did not sent")

                amount  = self.sock_1.sendto(data_buffer, ("localhost",self.udp_port_1))
                print(1,amount,dwBufSize,"<-------","sent")
                print("what is param ",param)
                # with open('./data.dav', 'ab+') as data_file:
                    # data_file.write(data_buffer)
                # amount  = self.sock_1.sendto(data_buffer, ("127.0.0.1",10000))
                

    
    def RealDataCallBack_1(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(lRealHandle,dwDataType,param,dwUser,"debug")
        if lRealHandle == self.playID_1:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)

                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                # if dwBufSize >10000:
                    # print("tiktok")
                amount = self.sock_2.sendto(data_buffer, ("localhost",self.udp_port_2))
                print(2,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_2(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        if lRealHandle == self.playID_2:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                # if dwBufSize >10000:

                amount  = self.sock_3.sendto(data_buffer, ("localhost",self.udp_port_3))
                print(3,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_3(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        if lRealHandle == self.playID_3:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount  = self.sock_4.sendto(data_buffer, ("localhost",self.udp_port_4))
                print(4,amount,dwBufSize,"<-------")
                print("what is param ",param)
    
    def RealDataCallBack_4(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(3)
        if lRealHandle == self.playID_4:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount  = self.sock_5.sendto(data_buffer, ("localhost",self.udp_port_5))
                print(5,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_5(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(4)
        if lRealHandle == self.playID_5:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount = self.sock_6.sendto(data_buffer, ("localhost",self.udp_port_6))
                print(6,amount,dwBufSize,"<-------")
                print("what is param ",param)


    def RealDataCallBack_6(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(6)
        if lRealHandle == self.playID_6:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount = self.sock_7.sendto(data_buffer, ("localhost",self.udp_port_7))
                print(7,amount,dwBufSize,"<-------")
                print("what is param ",param)


    def RealDataCallBack_7(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(7)
        if lRealHandle == self.playID_7:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount  = self.sock_8.sendto(data_buffer, ("localhost",self.udp_port_8))
                print(8,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_8(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(8)
        if lRealHandle == self.playID_8:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount=self.sock_9.sendto(data_buffer, ("localhost",self.udp_port_9))
                print(9,amount,dwBufSize,"<-------")
                print("what is param ",param)
    
    def RealDataCallBack_9(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(9)
        if lRealHandle == self.playID_9:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount  = self.sock_10.sendto(data_buffer, ("localhost",self.udp_port_10))
                print(10,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_10(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(10)
        if lRealHandle == self.playID_10:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount  = self.sock_11.sendto(data_buffer,("localhost",self.udp_port_11))
                print(11,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_11(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(11)
        if lRealHandle == self.playID_11:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount  = self.sock_12.sendto(data_buffer, ("localhost",self.udp_port_12))
                print(12,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_12(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(12)
        if lRealHandle == self.playID_12:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount = self.sock_13.sendto(data_buffer, ("localhost",self.udp_port_13))
                print(13,amount,dwBufSize,"<-------")
                print("what is param ",param)

    def RealDataCallBack_13(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(13)
        if lRealHandle == self.playID_13:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount = self.sock_14.sendto(data_buffer, ("localhost",self.udp_port_14))
                print(14,amount,dwBufSize,"<-------")
                print("what is param ",param)

    
    def RealDataCallBack_14(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(14)
        if lRealHandle == self.playID_14:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount = self.sock_15.sendto(data_buffer, ("localhost",self.udp_port_15))
                print(15,amount,dwBufSize,"<-------")
                print("what is param ",param)
    def RealDataCallBack_15(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
        # print(15)
        if lRealHandle == self.playID_15:
            if dwDataType == 0:
                # print("IS YUV ",dwDataType,param)
                # print("码流大小(Stream size):" + str(dwBufSize) + ". 码流类型:原始未加密码流(Stream type:original unencrypted stream)")
                data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
                amount = self.sock_16.sendto(data_buffer,("localhost",self.udp_port_16))
                print(16,amount,dwBufSize,"<-------")
                print("what is param ",param)





    # 关闭主窗口时清理资源
    def quit_demo(self):
        if  self.loginID:
            self.sdk.Logout(self.loginID)
        self.sdk.Cleanup()
        print("程序结束(Demo finish)")

if __name__ == '__main__':
    try:

        my_demo = RealPlayDemo()
        my_demo.get_login_info()
        result = my_demo.login()
        print(result)
        if not result:
            my_demo.quit_demo()
        else:
            my_demo.get_realplay_info()
            result = my_demo.realplay()
            
            # for packet in container.demux():
            #     print(packet.size)
            #     if packet.size == 0:
            #         continue
            #     cur_pos += packet.size
            #     for frame in packet.decode():
            #         print(frame.shape)
                    # self.frames.append(frame)
            if not result:
                my_demo.quit_demo()
            else:
                while 1:
                    pass
                # temp = input('输入任意键停止实时监视(Enter any key to stop realplay):')
    except Exception as err:
        my_demo.stop_realplay()
        my_demo.logout()
        my_demo.quit_demo()
        print(err)
        raise Exception("regualar exception")
    except KeyboardInterrupt:
        my_demo.stop_realplay()
        my_demo.logout()
        my_demo.quit_demo()


