import time
import traceback
import torch
#from torch.onnx import ONNX_ARCHIVE_MODEL_PROTO_NAME, ExportTypes, OperatorExportTypes, #TrainingMode
from torch.autograd import Variable
import torch.nn.functional as F
from pytorchvideo.models.x3d import create_x3d
#import cv2
import numpy as np
import pika
import pickle
import sys
from threading import Thread
import pandas as pd
from torchvision import transforms
from PIL import Image
from moviepy.editor import ImageSequenceClip
#import av
import requests
import pymysql

import sys 
server_public_ip_address =  sys.argv[1]

rabbit_mq_ip = sys.argv[2]

pipeline_management_server_ip = sys.argv[3]

threshold  = float(sys.argv[4])

password = sys.argv[5]


credentials = pika.PlainCredentials('guest', 'guest')
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

    whatsapp_dict_to = {"whatsapp:+919030044059":[]}


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

load_a = time.time()
model = create_x3d(input_channel=3,input_clip_length=16,input_crop_size=312,model_num_class=2,dropout_rate =0.5\
                        ,depth_factor=5.0, head_output_with_global_average=True)
        # create_x3d(input_channel=3,input_clip_length=16,input_crop_size=312,model_num_class=400,dropout_rate =0.5\
        #                 ,depth_factor=5.0, head_output_with_global_average=True)
model.load_state_dict(torch.load(PATH,map_location="cuda"))
model.eval()
model.cuda()
load_b = time.time()
print("model loading took this much time !",load_b-load_a)
analysis_array = []
p = transforms.Compose([transforms.Resize(312)])

with torch.no_grad():

    while (True):
        try :
            time_network_1 = time.time()
            method_frame, header_frame, body = channel.basic_get('fire_detection')
            time_network_2 = time.time()
            # print("network time for message :-  ",time_network_2-time_network_1)
            if method_frame:
                print("network time for message :-  ",time_network_2-time_network_1)
                ack_time_1 = time.time()
                channel.basic_ack(method_frame.delivery_tag)
                ack_time_2 = time.time()
                print("acknowledgemnt time :-",ack_time_2-ack_time_1)
                a = time.time()
                input_numpy = pickle.loads(body)
                print(input_numpy.shape)
                # cou = 1
                # for tm_array in list(input_numpy):
                #     print(tm_array.dtype)
                #     Image.fromarray(tm_array).save("temp_{}.png".format(cou))
                #     cou+=1
                b = time.time()
                torch_tensor = torch.tensor(np.array(input_numpy))
                print(torch_tensor.shape)
                # resized_video = p(torch_tensor.permute(3,0,1,2))
                # permuted_torch  = resized_video
                permuted_torch =  torch_tensor.permute(3,0,1,2)
                temp_tensor = torch.unsqueeze(permuted_torch,0)
                torch_input_tensor = temp_tensor.float().cuda()/255
                c = time.time()
                print("cpu  to gpu loading timee of tensors ",c-a)
                print(header_frame.headers,type(header_frame.headers))
                cam_no = header_frame.headers['camera_no']
                if cam_no in dict_:
                    pass
                else:
                    dict_[cam_no]={"timestamps":[],"is_alarm_triggered":0,"to_trigger":0}
                cam_time = int(float(header_frame.headers['current_time']))
                try:

                    infer_a = time.time()
                    # starter.record()

                    model_out = model(torch_input_tensor)
                    infer_b = time.time()
                    log_time_a = time.time()
                    # output = F.log_softmax(model_out, dim=1)
                    # _, pred = torch.max(output, dim=1)
                    _, pred = torch.max(model_out, dim=1)
                    log_time_b = time.time()
                    if pred.eq(torch.tensor([0]).cuda()) and model_out.cpu().numpy().tolist()[0][0]>threshold:
                        # create mp4 file of input_numpy in test_results to be picked up by twilio api
                        create_mp4_file("{}_{}_fire_pred.mp4".format(cam_no,str(cam_time)),input_numpy)

                        decision_a = time.time()
                        dict_[cam_no]["timestamps"].append(cam_time)
                        if len(dict_[cam_no]["timestamps"])>=1:

                            # time_1,time_2,time_3 = dict_["cam_{}".format(str(cam_no))]["timestamps"][-3:]

                            # time_1 = dict_["cam_{}".format(str(cam_no))]["timestamps"][-1]
                            # if (time_2-time_1)<17 and (time_3-time_2)<17:
                            # if (time_2-time_1)<17:
                            dict_[cam_no]["to_trigger"]=1
                        #print(" cam no current :- ","cam_{}".format(str(cam_no)),dict_["cam_{}".format(str(cam_no))]," <-----condsider")
                        print(" cam no current :- ","{}".format(str(cam_no))," <-----condsider")
                        output_dict = dict_[cam_no]
                        if output_dict["to_trigger"]==1 and output_dict["is_alarm_triggered"]==0:
                            pass
#                           temp_thread = Thread(target = alert_mechanism,args=(cam_no,"{}_{}_fire_pred.mp4".format(cam_no,str(cam_time)),))
#                           temp_thread.start()
                          
                            payload = {'server_public_ip_address':server_public_ip_address,
                            "mp4_payload":"{}_{}_fire_pred.mp4".format(cam_no,str(cam_time)),
                            "cam_no":cam_no
                            }
                            alert_web_request_started = False
                            try:
                                resp=requests.post('http://{}:60000/fire_alert_mechanism'.format(pipeline_management_server_ip), json=payload)
                                if "Started Fire alert" in resp.text:
                                    alert_web_request_started = True
                                else:
                                    raise Exception(str(resp.text))
                                
                            except Exception as error_2:
                                error = traceback.format_exception(error_2.__class__, error_2, error_2.__traceback__)
                                alert_db_connection = pymysql.connect(host=pipeline_management_server_ip,user='root',password=password,database="cctv_ai_usecase_products",charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
                                alert_cursor = alert_db_connection.cursor()
                                tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                                tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                                alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"error occured {}".format(error)])
                                alert_db_connection.commit()
                                alert_cursor.close()
                                alert_db_connection.close()
                            if not alert_web_request_started:
                                dict_[cam_no]["is_alarm_triggered"]=0
                            else:
                                dict_[cam_no]["is_alarm_triggered"]=1
                            
                        elif output_dict["to_trigger"]==0 and output_dict["is_alarm_triggered"]==1:
                            pass
                        elif output_dict["to_trigger"]==1 and output_dict["is_alarm_triggered"]==1:
                            pass
                        elif output_dict["to_trigger"]==0 and output_dict["is_alarm_triggered"]==0:
                            pass
                        decision_b = time.time()
                        print("timestamp evaluation time ",decision_b-decision_a)
                        saving_a = time.time()
                        #with open('./test_results/{}_{}_fire_pred.npy'.format(cam_no,str(cam_time)), 'wb') as f:
                        #    np.save(f,input_numpy)
                        saving_b = time.time()

                    if  pred.eq(torch.tensor([0]).cuda()):
                        analysis_array.append([cam_no,cam_time,"fire",model_out.cpu().numpy().tolist()[0][0]*100])         
                    else:
                        analysis_array.append([cam_no,cam_time,"nofire",model_out.cpu().numpy().tolist()[0][1]*100])
#                        with open('./test_results/{}_{}_nofire_pred.npy'.format(cam_no,str(cam_time)), 'wb') as f:
#                            np.save(f,input_numpy)

                    print("inference time !",((infer_b-infer_a)+(log_time_b-log_time_a)),"prediction finally !",pred,model_out)
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
                temp_df = pd.DataFrame(analysis_array,columns=["cam_no","cam_time","class","confidence"])
                temp_df.to_csv("analysis_results.csv",sep=",")
            except Exception:
                temp_df = pd.DataFrame(analysis_array,columns=["cam_no","cam_time","class","confidence"])
                temp_df.to_csv("analysis_results.csv",sep=",")

            print("bye predictions ..")
            connection.close()
            sys.exit(1)
    

        


