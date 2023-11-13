import time
import traceback
import torch
#from torch.onnx import ONNX_ARCHIVE_MODEL_PROTO_NAME, ExportTypes, OperatorExportTypes, #TrainingMode
from torch.autograd import Variable
import torch.nn.functional as F
# from pytorchvideo.models.x3d import create_x3d
import cv2
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
                                       8882,
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



# torch.cuda._lazy_init()
torch.backends.cudnn.benchmark = True


torch.backends.cudnn.enabled = True

torch.backends.cudnn.deterministic = True


path = "/root/backup_cloud_gpu_2_sep_21_2022/video-transformers/runs/exp12/checkpoint"

#PATH = "./pytorchvideo/x3d_large_model_trial_version_5.pth"
# PATH = "/home/ai/pytorchvideo/x3d_large_model_evidential_dear_version_11.pth"
#PATH = "/home/ai/Downloads/x3d_large_model_trial_version_1.pth"

dict_ = {}
for no in range(1,140):
    dict_["cam_{}".format(str(no))]={"timestamps":[],"is_alarm_triggered":0,"to_trigger":0}

load_a = time.time()
path = "/root/backup_cloud_gpu_2_sep_21_2022/yolov5"
model_path = "/root/backup_cloud_gpu_2_sep_21_2022/yolov5/runs/train/yolov5s_overfit_fire_28/weights/best.pt"
model_fire=torch.hub.load(path,"custom",model_path,source="local",force_reload=True,skip_validation=False,verbose=True)

# print(model)


for name2,param2 in model_fire.named_parameters():
    # print(name2,param2.requires_grad)
    param2.requires_grad=False
model_fire.cuda()
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
                b = time.time()
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

                    model_out = model_fire(input_numpy)
                    infer_b = time.time()
                    log_time_a = time.time()
                    log_time_b = time.time()
                    #if pred.eq(torch.tensor([0]).cuda()):
                    #    create_mp4_file("{}_{}_fire_pred.mp4".format(cam_no,str(cam_time)),input_numpy)
                    is_ok = False
                    for lst_values in model_out.pred[0].cpu().numpy().tolist():
                        if lst_values[-2]> threshold:
                            is_ok = True

                    if "fire" in model_out and is_ok:
                        # create mp4 file of input_numpy in test_results to be picked up by twilio api
                        # create_mp4_file("{}_{}_fire_pred.mp4".format(cam_no,str(cam_time)),input_numpy)
                        cv2.imwrite("./test_results/"+"{}_{}_fire_pred.png".format(cam_no,str(cam_time)),cv2.cvtColor(model_out.ims[0], cv2.COLOR_BGR2RGB))


                        decision_a = time.time()
                        dict_[cam_no]["timestamps"].append(cam_time)
                        if len(dict_[cam_no]["timestamps"])>=1:
                            if "25001_cam_1" in cam_no:
                                 pass
                            else:

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
                            "mp4_payload":"{}_{}_fire_pred.png".format(cam_no,str(cam_time)),
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
                                dict_[cam_no]["is_alarm_triggered"]=0
                            
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
                        analysis_array.append([cam_no,cam_time,"fire",probabilities.cpu().numpy().tolist()[0][0]*100])         
                    else:
                        analysis_array.append([cam_no,cam_time,"nofire",probabilities.cpu().numpy().tolist()[0][1]*100])
#                        with open('./test_results/{}_{}_nofire_pred.npy'.format(cam_no,str(cam_time)), 'wb') as f:
#                            np.save(f,input_numpy)

                    print("inference time !",((infer_b-infer_a)+(log_time_b-log_time_a)),"prediction finally !",pred,probabilities)
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
    

        


