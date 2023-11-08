import time
import traceback
import torch
#from torch.onnx import ONNX_ARCHIVE_MODEL_PROTO_NAME, ExportTypes, OperatorExportTypes, #TrainingMode
from torch.autograd import Variable
import torch.nn.functional as F
# from pytorchvideo.models.x3d import create_x3d
import cv2
import re
import numpy as np
import pika
import pickle
import sys
from threading import Thread
import pandas as pd
from torchvision import transforms
from PIL import Image
#from moviepy.editor import ImageSequenceClip
#import av
import requests
import pymysql
import uuid
import sys 

from huggingface_hub import snapshot_download
from pathlib import Path
import os

# from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
# from llava.conversation import conv_templates, SeparatorStyle
# from llava.model.builder import load_pretrained_model
# from llava.utils import disable_torch_init
# from llava.mm_utils import process_images, tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria

from PIL import Image

import requests
from PIL import Image
from io import BytesIO
# from transformers import TextStreamer



load_a = time.time()

from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import torch
# from modelscope import (
# snapshot_download, AutoModelForCausalLM, AutoTokenizer, GenerationConfig
# )
torch.manual_seed(1234)
# revision = 'v1.0.0'
# model_id = 'qwen/Qwen-VL-Chat-Int4'
# model_dir = snapshot_download(model_id, revision=revision)
# print(model_dir)
# Note: The default behavior now has injection attack prevention off.
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-VL-Chat", trust_remote_code=True)
# if not hasattr(tokenizer, 'model_dir'):
#     tokenizer.model_dir = model_dir
# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat", device_map="cpu", trust_remote_code=True).eval()
# use cuda device
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat",device_map="cuda", trust_remote_code=True,fp16=True).eval()

# Specify hyperparameters for generation
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-VL-Chat", trust_remote_code=True)
# print(model.generation_config)
# 1st dialogue turn
load_b = time.time()
print("model loading took this much time !",load_b-load_a)
# print(model_download_path,"model_download_path")



server_public_ip_address =  sys.argv[1]

rabbit_mq_ip = sys.argv[2]

pipeline_management_server_ip = sys.argv[3]

threshold  = float(sys.argv[4])

password = sys.argv[5]


credentials = pika.PlainCredentials('cctv_ai', 'idmohanceo@ai.bits')
parameters = pika.ConnectionParameters(rabbit_mq_ip,
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)
# connection = pika.BlockingConnection()
channel = connection.channel()


def create_mp4_file(file_name,np_array):
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # video = cv2.VideoWriter("/root/test_results/"+file_name, fourcc, 2, (312, 312))
    # for image in list(np_array):
    #     video.write(image)
    
    # video.release()
    with ImageSequenceClip(list(np_array), fps=2) as clip:
        clip.write_videofile("./test_results/"+file_name,fps=2,logger=None)
    clip.close()

def alert_mechanism(cam_no,mp4_payload):
    phone_dict = {
            # '+916300910323':{},
              #'+918770768741':{},
              #  '+916300910323':{},
#               '+917093054982':{},
                # '+919493242570':{}
               # '+919441057705':{},
		'+919030044059':{}
              }
    
    whatsapp_dict_from = {"whatsapp:+919493750102":[]}

    whatsapp_dict_to = {"whatsapp:+919493750102":[]}


    from twilio.rest import Client
    account_sid = "AC5e2ed48db288bffb446cf1a75ea55194"
    auth_token = "c751c1bd5e4e489d087ad3d69eb842af"
    client = Client(account_sid, auth_token)

    def send_whatsapp_video_clip_twilio(from_phone_no,to_phone_no,mp4_payload,client):
        message = client.messages.create(
                        from_=from_phone_no,
                        media_url=["http://45.77.206.117:5000/fire/{}".format(mp4_payload)],
                        #body='Hi Shekhar, were we able to solve the issue that you were facing?',
                        to=to_phone_no
                    )
        

    
    def make_a_call(phone_no,cam_no,client):
        call = client.calls.create(
            twiml='<Response><Say>fire detected at camera number {}  fire detected at camera number {}  fire detected at camera number  {}  fire detected at camera number  {}   fire detected at camera number  {} fire detected at camera number  {}  fire detected at camera number  {}</Say></Response>'.format(int(cam_no),int(cam_no),int(cam_no),int(cam_no),int(cam_no),int(cam_no),int(cam_no)),
            to=phone_no,
            from_='+16783040899'
            )
        return call.sid
    
    def fetch_call_status(client,call_sid):
        call = client.calls(call_sid).fetch()
        return call.status
    
    #### ------------ send whatsapp video clips before initiating calls ----------- #####

    for send_from_whatsapp_no in whatsapp_dict_from:

        for send_to_whatsapp_no in whatsapp_dict_to:
            
            send_whatsapp_video_clip_twilio(send_from_whatsapp_no,send_to_whatsapp_no,mp4_payload,client)
    
    ### have to implement design architecture to verify whatsapp video delivery status that doesn't block or interefer with call intimation etc ######

    phone_no_list  = list(phone_dict.keys())
    all_lifted = 0
    for i in range(5):
        print("no of times trying :-",i)

        for phn_no in phone_no_list:
            is_call_lifted = False
            for call_sid in phone_dict[phn_no]:
                if phone_dict[phn_no][call_sid]==1:
                    print("phone no :-",phn_no," lifted after n th time",i)
                    is_call_lifted = True
                    break

            if is_call_lifted==False:
                print("nth time trying :-",i," for phone no not lifted :-",phn_no)
                temp_call_sid  =  make_a_call(phn_no,cam_no,client)
                phone_dict[phn_no][temp_call_sid]=0
                print("sleep for 30 sec")
                time.sleep(30)
                print("after 30 sec")

        for phn_no2 in phone_no_list:
            for call_sid2 in  list(phone_dict[phn_no2].keys()):
                time.sleep(10)
                if fetch_call_status(client,call_sid2)=='completed':
                    print("phone no lifted ",phn_no2)
                    phone_dict[phn_no2][call_sid2]=1

def evaluate_timestamps(input_dict,cam_time):
    time_stamps_list = input_dict["timestamps"]
    if len(time_stamps_list)==3:
        time_1,time_2,time_3 = time_stamps_list
        if (time_2-time_1)<14 and (time_3-time_2)<14:
            input_dict["to_trigger"]=1
        elif (time_2-time_1)<14 and (time_3-time_2)>14:
            input_dict["timestamps"]=[time_3]
        elif (time_2-time_1)>14 and (time_3-time_2)<14:
            input_dict["timestamps"] = [time_2,time_3]
        elif (time_2-time_1)>14 and (time_3-time_2)>14:
            input_dict["timestamps"] = [time_3]
    elif len(time_stamps_list)<3:
        time_stamps_list.append(cam_time)
    return input_dict
    


# torch.cuda._lazy_init()
torch.backends.cudnn.benchmark = True


torch.backends.cudnn.enabled = True

torch.backends.cudnn.deterministic = True



PATH = "./pytorchvideo/x3d_large_model_trial_version_5.pth"
# PATH = "/home/ai/pytorchvideo/x3d_large_model_evidential_dear_version_11.pth"
#PATH = "/home/ai/Downloads/x3d_large_model_trial_version_1.pth"

dict_ = {}
for no in range(1,140):
    dict_["cam_{}".format(str(no))]={"timestamps":[],"is_alarm_triggered":0,"to_trigger":0}


gpu_device = torch.device('cuda:0')


# model = create_x3d(input_channel=3,input_clip_length=16,input_crop_size=312,model_num_class=2,dropout_rate =0.5\
#                         ,depth_factor=5.0, head_output_with_global_average=True)
        # create_x3d(input_channel=3,input_clip_length=16,input_crop_size=312,model_num_class=400,dropout_rate =0.5\
        #                 ,depth_factor=5.0, head_output_with_global_average=True)
# model.load_state_dict(torch.load(PATH,map_location="cuda"))
# model.eval()
# model.cuda()

analysis_array = []
p = transforms.Compose([transforms.Resize(312)])







while (True):
    try :
        time_network_1 = time.time()
        list_of_delivery_body= []
        list_of_header_frames= []
        for j in range(6):
            method_frame, header_frame, body = channel.basic_get('fire_detection')
            if not method_frame:
                break
            time_network_2 = time.time()
            print("network time for message :-  ",time_network_2-time_network_1)
            ack_time_1 = time.time()
            channel.basic_ack(method_frame.delivery_tag)
            ack_time_2 = time.time()
            print("acknowledgemnt time :-",ack_time_2-ack_time_1)
            list_of_delivery_body.append(body)
            list_of_header_frames.append(header_frame)
        
        # print("network time for message :-  ",time_network_2-time_network_1)
        if 1:
            a = time.time()
            list_of_images_ = []
            for body_ in list_of_delivery_body:
                input_numpy = pickle.loads(body_)
                input_numpy = np.squeeze(input_numpy, axis=0)
                current_name = str(uuid.uuid4())
                cv2.imwrite("/root/cctv_ai_and_opensource_vision_llms_for_ai.bits/inputs/{}.png".format(current_name),input_numpy)
                list_of_images_.append("/root/cctv_ai_and_opensource_vision_llms_for_ai.bits/inputs/{}.png".format(current_name))
            c = time.time()
            print("cpu  to gpu loading timee of tensors ",c-a)
            list_of_camera_no = []
            list_of_camera_time  = []
            # print(header_frame.headers,type(header_frame.headers))
            for header_frame_ in list_of_header_frames:

                cam_no = header_frame_.headers['camera_no']
                list_of_camera_no.append(cam_no)
                if cam_no in dict_:
                    pass
                else:
                    dict_[cam_no]={"timestamps":[],"is_alarm_triggered":0,"to_trigger":0}
                cam_time = int(float(header_frame_.headers['current_time']))
                list_of_camera_time.append(cam_time)

            try:
                infer_a= time.time()
                input_list = []
                for image_name in list_of_images_:
                    input_list.append({"image":image_name})
                    input_list.append({'text': 'annotate fire'})
                query = tokenizer.from_list_format(input_list)
                # query = "<ref>annotate fire</ref><img>/root/cctv_ai_and_opensource_vision_llms_for_ai.bits/inputs/{}.png'</img>".format(current_name)
                response, history = model.chat(tokenizer, query=query, history=None)
                print(response,list_of_images_,"first turn <<<<<<<<<<<<<<<,-------------")
                pattern = r"<box>(.*?)</box>"
                boxes = re.findall(pattern, response, flags=0)
                # print(boxes,response)
                if len(boxes)==0:
                    pass
                else:
                    # 2nd dialogue turn
    #                 query = tokenizer.from_list_format([
    #                 {'image': '/root/cctv_ai_and_opensource_vision_llms_for_ai.bits/inputs/{}.png'.format(current_name)}, 
    #                     {'text': 'what it is <box>{}</box>'.format(boxes[0])},
    #                 ])
    #                 # query = "<ref>what it is <box>{}</box></ref><img>/root/cctv_ai_and_opensource_vision_llms_for_ai.bits/inputs/{}.png'</img>".format(boxes[0],current_name)
    #                 response, history = model.chat(tokenizer, query, history=None)
    #                 print(response,current_name,"second turn <<<<<<<<<<<<<<<<<,--------------------")
    #                 # # <ref>击掌</ref><box>(536,509),(588,602)</box>
    #                 image = tokenizer.draw_bbox_on_latest_picture(response, None)
    #                 if image:
    #                     image.save("{}_{}_{}_fire_pred.png".format(current_name,cam_no,str(cam_time)),input_numpy)
    #                 else:
    #                     print("no box")
    #                 if ("ceiling" in response ) or (("no" in response) and  ("fire" in response)):
    #                     pass
    #                 elif ("light" in response) and ("ceiling" not in response) or (("no" not in response) and ("fire" in response)):
    #                     cv2.imwrite("./multimodal_llm_pilot_test_outputs/"+"{}_{}_{}_fire_pred.png".format(current_name,cam_no,str(cam_time)),cv2.cvtColor(input_numpy, cv2.COLOR_BGR2RGB))


    #                     decision_a = time.time()
    #                     dict_[cam_no]["timestamps"].append(cam_time)
    #                     if len(dict_[cam_no]["timestamps"])>=1:

    #                         # time_1,time_2,time_3 = dict_["cam_{}".format(str(cam_no))]["timestamps"][-3:]

    #                         # time_1 = dict_["cam_{}".format(str(cam_no))]["timestamps"][-1]
    #                         # if (time_2-time_1)<17 and (time_3-time_2)<17:
    #                         # if (time_2-time_1)<17:
    #                         dict_[cam_no]["to_trigger"]=1
    #                     #print(" cam no current :- ","cam_{}".format(str(cam_no)),dict_["cam_{}".format(str(cam_no))]," <-----condsider")
    #                     print(" cam no current :- ","{}".format(str(cam_no))," <-----condsider")
    #                     output_dict = dict_[cam_no]
    #                     if output_dict["to_trigger"]==1 and output_dict["is_alarm_triggered"]==0:
    #                         pass
    # #                           temp_thread = Thread(target = alert_mechanism,args=(cam_no,"{}_{}_fire_pred.mp4".format(cam_no,str(cam_time)),))
    # #                           temp_thread.start()
                            
    #                         # payload = {'server_public_ip_address':server_public_ip_address,
    #                         # "mp4_payload":"{}_{}_fire_pred.mp4".format(cam_no,str(cam_time)),
    #                         # "cam_no":cam_no
    #                         # }
    #                         payload = {'server_public_ip_address':server_public_ip_address,
    #                         "mp4_payload":"{}_{}_fire_pred.png".format(cam_no,str(cam_time)),
    #                         "cam_no":cam_no
    #                         }
    #                         alert_web_request_started = False
    #                         # try:
    #                         #     resp=requests.post('http://{}:60000/fire_alert_mechanism'.format(pipeline_management_server_ip), json=payload)
    #                         #     if "Started Fire alert" in resp.text:
    #                         #         alert_web_request_started = True
    #                         #     else:
    #                         #         raise Exception(str(resp.text))
                                
    #                         # except Exception as error_2:
    #                         #     error = traceback.format_exception(error_2.__class__, error_2, error_2.__traceback__)
    #                         #     print(error)
    #                             # alert_db_connection = pymysql.connect(host=pipeline_management_server_ip,user='root',password=password,database="cctv_ai_usecase_products",charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    #                             # alert_cursor = alert_db_connection.cursor()
    #                             # tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
    #                             # tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
    #                             # alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"error occured {}".format(error)])
    #                             # alert_db_connection.commit()
    #                             # alert_cursor.close()
    #                             # alert_db_connection.close()
    #                         if not alert_web_request_started:
    #                             dict_[cam_no]["is_alarm_triggered"]=0
    #                         else:
    #                             dict_[cam_no]["is_alarm_triggered"]=0
                            
    #                     elif output_dict["to_trigger"]==0 and output_dict["is_alarm_triggered"]==1:
    #                         pass
    #                     elif output_dict["to_trigger"]==1 and output_dict["is_alarm_triggered"]==1:
    #                         pass
    #                     elif output_dict["to_trigger"]==0 and output_dict["is_alarm_triggered"]==0:
    #                         pass
    #                     decision_b = time.time()
    #                     print("timestamp evaluation time ",decision_b-decision_a)

    #                     # if  pred.eq(torch.tensor([0]).cuda()):
                        analysis_array.append([cam_no,cam_time,"unkown",response])         
                infer_b  =time.time()
                print("inference time !",((infer_b-infer_a)),"prediction finally !",)
                print("--------------------------------eof of inputs ------------------------------------------")
            except Exception as excp:
                if "Connection" in str(excp):
                    connection = pika.BlockingConnection(parameters)
                    channel = connection.channel()
                print("model errored out",excp)
                print(traceback.format_exc())

        else:
            pass
            # print('No message returned')
            # print("network time for message :-  ",time_network_2-time_network_1)
    except KeyboardInterrupt:
        try:
            temp_df = pd.DataFrame(analysis_array,columns=["cam_no","cam_time","class","explanation"])
            temp_df.to_csv("analysis_results.csv",sep=",")
        except Exception:
            temp_df = pd.DataFrame(analysis_array,columns=["cam_no","cam_time","class","explanation"])
            temp_df.to_csv("analysis_results.csv",sep=",")

        print("bye predictions ..")
        connection.close()
        sys.exit(1)


    


