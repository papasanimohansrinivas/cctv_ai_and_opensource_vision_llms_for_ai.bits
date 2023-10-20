from flask import Flask, request, jsonify,render_template

import dbus
from dbus import Interface
import time
import datetime
import pymysql
import subprocess
import traceback

from threading import Thread

app = Flask(__name__,template_folder='/root/backup_xeon_decoding_server_sep_21_2022')

# db = pymysql.connect("127.0.0.1", "root", "cctv@ai#SOFTWARE0007", "cctv_ai_usecase_products")
def alert_mechanism(cam_no,mp4_payload,server_public_ip_address,password,is_infinite_loop,number_of_times_to_call):

    try:

        from twilio.rest import Client
        account_sid = "AC5e2ed48db288bffb446cf1a75ea55194"
        auth_token = "c751c1bd5e4e489d087ad3d69eb842af"
        client = Client(account_sid, auth_token)

        def send_whatsapp_video_clip_twilio(from_phone_no,to_phone_no,mp4_payload,client,server_public_ip_address):
            message = client.messages.create(
                            from_=from_phone_no,
                            media_url=["http://{}:5000/fire/{}".format(server_public_ip_address,mp4_payload)],
                            #body='Hi Shekhar, were we able to solve the issue that you were facing?',
                            to=to_phone_no
                        )
            return message.sid

        
        def make_a_call(phone_no,cam_no,cam_description,client,twilio_phone_number):
            if cam_description!="":

                say = '<Response><Say>fire detected at camera number {}  fire detected at camera number {}  fire detected at camera number  {}  fire detected at camera number  {}   fire detected at    {} fire detected at   {}  fire detected at  {}</Say></Response>'.format(int(cam_no),int(cam_no),int(cam_no),int(cam_no),cam_description,cam_description,cam_description)
            else:
                say = '<Response><Say>fire detected at camera number {}  fire detected at camera number {}  fire detected at camera number  {}  fire detected at camera number  {}   fire detected at    {} fire detected at   {}  fire detected at  {}</Say></Response>'.format(int(cam_no),int(cam_no),int(cam_no),int(cam_no),int(cam_no),int(cam_no),int(cam_no))
        
            call = client.calls.create(
                twiml=say,
                to=phone_no,
                from_=twilio_phone_number
                )
            return call.sid
        
        def fetch_call_status(client,call_sid):
            call = client.calls(call_sid).fetch()
            return call.status
        
        alert_db_connection = pymysql.connect(host='127.0.0.1',user='root',password=password,database="cctv_ai_usecase_products",charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        
        #client_1_49_206_199_97_25001_cam_11

        do_call  = False
        do_whatsapp = False

        temp = cam_no.split("_")

        temp_cam_number  = temp[-1]

        temp_client_no = "_".join([temp[0],temp[1]])

        temp_client_static_ip = ".".join([temp[2],temp[3],temp[4],temp[5]])

        temp_client_port = temp[6]


        alert_cursor = alert_db_connection.cursor()
        sql = """SELECT * FROM `customer_deployment_table` where client_id_in_system = \"{}\" and dvr_static_ip = \"{}\" and dvr_port = \"{}\" """.format(temp_client_no,temp_client_static_ip,temp_client_port)
        alert_cursor.execute(sql)
        temp_result = alert_cursor.fetchall()


        # for now only this validation necessary where one row per client per dvr etc remove when neceasry 
        assert len(temp_result)==1

        cams_with_call_service_per_usecase_list   = temp_result[0]["cams_with_call_service_per_usecase"].split(",") 

        cams_with_whatsapp_service_per_usecase_list = temp_result[0]["cams_with_whatsapp_service_per_usecase"].split(",")

        subscribed_phone_numbers_for_whatsapp_list = temp_result[0]["subscribed_phone_numbers_for_whatsapp"].split(",")

        subscribed_phone_numbers_for_call_list = temp_result[0]["subscribed_phone_numbers_for_call"].split(",")

        cam_description_list_list = temp_result[0]["cam_description_list"].split("#")

        cam_number_list_list = temp_result[0]["cam_number_list"].split(",")

        set_cam_description_empty = False

        if len(cam_description_list_list)!=len(cam_number_list_list):
            tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
            tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
            alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"number of cam numbers and dscriptions not match for now setting camera description in call service "])
            alert_db_connection.commit()
            set_cam_description_empty = True
        

            ### write to database about the issue 
        if set_cam_description_empty:
            temp_cam_description = ""
        else:
            try:

                cam_number_list_list.index(temp_cam_number)
            except ValueError:
                tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"some how camera number missed in customer_deployment_table entry for now sending camera description empty {}  {} ".format(",".join(cam_number_list_list),temp_cam_number)])
                alert_db_connection.commit()
                set_cam_description_empty = True
                ### log to database done

            if set_cam_description_empty:
                temp_cam_description= ""
            else:
                temp_cam_description = cam_description_list_list[cam_number_list_list.index(temp_cam_number)]



        


        if (temp_cam_number not in cams_with_call_service_per_usecase_list) and (temp_cam_number not in cams_with_whatsapp_service_per_usecase_list):
            
            ### log to database anamoly done 
            ### send a alert mail to admin to do 
            pass

        elif (temp_cam_number in cams_with_call_service_per_usecase_list ) and (temp_cam_number not in cams_with_whatsapp_service_per_usecase_list):
            do_whatsapp=False
            do_call = True

        elif (temp_cam_number in cams_with_call_service_per_usecase_list ) and (temp_cam_number  in cams_with_whatsapp_service_per_usecase_list):
            do_call = True
            do_whatsapp = True

        elif (temp_cam_number not in cams_with_call_service_per_usecase_list ) and (temp_cam_number  in cams_with_whatsapp_service_per_usecase_list):
            do_call = False
            do_whatsapp = True

        if not  do_whatsapp and not do_call:
            tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
            tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
            alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"camera number not present in bot call service or whatsapp service check customer deployment table for now doing both call and service as temporary resolution"])
            alert_db_connection.commit()
            do_whatsapp = True
            do_call = True
            ### log the anamoly

        alert_cursor.execute("""select twilio_whatsapp_number,twilio_call_number from `current_usecases_table` where use_case = \"fire_detection\" """)
        alert_number_results = alert_cursor.fetchall()

        from_whatsapp_no  = alert_number_results[0]["twilio_whatsapp_number"]

        from_twilio_phone_no = alert_number_results[0]["twilio_call_number"]

        if do_whatsapp:

            # assume this is for india numbers only for now , for us we have to change and adapt the code
            whatsapp_dict_from = {"whatsapp:{}".format(from_whatsapp_no):[]}
            whatsapp_dict_to = {}
            for num1 in subscribed_phone_numbers_for_whatsapp_list:
                whatsapp_dict_to["whatsapp:+91{}".format(num1)]=[]

            for send_from_whatsapp_no in whatsapp_dict_from:

                for send_to_whatsapp_no in whatsapp_dict_to:
                    
                    whatsapp_sid = send_whatsapp_video_clip_twilio(send_from_whatsapp_no,send_to_whatsapp_no,mp4_payload,client,server_public_ip_address)
                    tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                    tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                    alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, mp4_payload,"whatsapp video sent to {} with sid :- {}".format(send_to_whatsapp_no,str(whatsapp_sid))])
                    alert_db_connection.commit()
        do_call = False
        if do_call:
            
            phone_dict = {
                    # '+916300910323':{},
                    #'+918770768741':{},
                    #  '+916300910323':{},
        #               '+917093054982':{},
                        # '+919493242570':{}
                    # '+919441057705':{},
                '+919030044059':{}
                    }
            phone_dict = {}
            for num2 in subscribed_phone_numbers_for_call_list:
                phone_dict["+91{}".format(num2)]={}


            ### have to implement design architecture to verify whatsapp video delivery status that doesn't block or interefer with call intimation etc ######
            ### make sure phone numbers are correct and valid numbers 
            ### to do log the calls and whatsapp in database 
            #### change for loop to while infinite loop if reuirement asks for it adapt it 
            ### cam description list inclusion 

            phone_no_list  = list(phone_dict.keys())
            current_lifted_number_list = []
            all_lifted = 0
            if is_infinite_loop:
                i=1
                while True:
                    print("no of times trying :-",i)

                    for phn_no in phone_no_list:
                        is_call_lifted = False
                        for call_sid in phone_dict[phn_no]:
                            if phone_dict[phn_no][call_sid]==1:
                                print("phone no :-",phn_no," lifted after n th time",i)
                                is_call_lifted = True
                                if phn_no not in current_lifted_number_list:
                                    current_lifted_number_list.append(phn_no)
                                break

                        if is_call_lifted==False:
                            print("nth time trying :-",i," for phone no not lifted :-",phn_no)
                            while 1:

                                try:

                                    temp_call_sid  =  make_a_call(phn_no,temp_cam_number,temp_cam_description,client,from_twilio_phone_no)
                                    break
                                except Exception as call_error:
                                    tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                                    tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                                    alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"{} for phone no {}".format(str(call_error),str(phn_no))])
                                    alert_db_connection.commit()
                                    time.sleep(3)
                                
                            phone_dict[phn_no][temp_call_sid]=0
                            tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                            tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                            alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"nth time trying :- {} for phone no not lifted :- {}".format(str(i),phn_no)])
                            alert_db_connection.commit()
                            print("sleep for 30 sec")
                            time.sleep(6)
                            print("after 30 sec")

                    for phn_no2 in phone_no_list:
                        for call_sid2 in  list(phone_dict[phn_no2].keys()):
                            time.sleep(10)
                            if fetch_call_status(client,call_sid2)=='completed':
                                print("phone no lifted ",phn_no2)
                                phone_dict[phn_no2][call_sid2]=1
                    count = 0            
                    for verify_phone_num in phone_no_list:
                        if verify_phone_num in current_lifted_number_list:
                            count+=1
                    
                    if count==len(phone_no_list):
                        all_lifted=True
                    if all_lifted:
                        break
                    i+=1
            else:

                for i in range(number_of_times_to_call):
                    print("no of times trying :-",i)

                    for phn_no in phone_no_list:
                        is_call_lifted = False
                        for call_sid in phone_dict[phn_no]:
                            if phone_dict[phn_no][call_sid]==1:
                                print("phone no :-",phn_no," lifted after n th time",i)
                                tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                                tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                                alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"phone no :- {} lifted after n th time {}".format(str(phn_no),str(i))])
                                alert_db_connection.commit()
                                is_call_lifted = True
                                if phn_no not in current_lifted_number_list:
                                    current_lifted_number_list.append(phn_no)
                                break

                        if is_call_lifted==False:
                            print("nth time trying :-",i," for phone no not lifted :-",phn_no)
                            while 1:

                                try:

                                    temp_call_sid  =  make_a_call(phn_no,temp_cam_number,temp_cam_description,client,from_twilio_phone_no)
                                    break
                                except Exception as call_error:
                                    tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                                    tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                                    alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"{} for phone no {}".format(str(call_error),str(phn_no))])
                                    alert_db_connection.commit()
                                    time.sleep(3)
                            phone_dict[phn_no][temp_call_sid]=0
                            tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                            tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                            alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"nth time trying :- {} for phone no not lifted :- {}".format(str(i),str(phn_no))])
                            alert_db_connection.commit()
                            
                            print("sleep for 30 sec")
                            time.sleep(6)
                            print("after 30 sec")

                    for phn_no2 in phone_no_list:
                        for call_sid2 in  list(phone_dict[phn_no2].keys()):
                            time.sleep(10)
                            if fetch_call_status(client,call_sid2)=='completed':
                                print("phone no lifted ",phn_no2)
                                
                                phone_dict[phn_no2][call_sid2]=1
                                tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
                                tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
                                alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"phone no lifted {}".format(str(phn_no2))])
                                alert_db_connection.commit()
                    # count = 0            
                    # for verify_phone_num in phone_no_list:
                    #     if verify_phone_num in current_lifted_number_list:
                    #         count+=1
                    
                    # if count==len(phone_no_list):
                    #     all_lifted=True
        alert_cursor.close()
        alert_db_connection.close()
    except Exception as error:
        print(error)
        error = traceback.format_exception(error.__class__, error, error.__traceback__)
        print(error)
        alert_db_connection = pymysql.connect(host='127.0.0.1',user='root',password=password,database="cctv_ai_usecase_products",charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        alert_cursor = alert_db_connection.cursor()
        tmp_batch_id = int(alert_cursor.execute('select last_insert_id() from call_and_whatsapp_service_log_table'))
        tmp_STATEMENT = """insert into `call_and_whatsapp_service_log_table` values ("""+",".join(["%s"]*3)+""")"""
        alert_cursor.execute(tmp_STATEMENT,[tmp_batch_id+1, cam_no,"error occured {}".format(error)])
        alert_db_connection.commit()
        alert_cursor.close()
        alert_db_connection.close()
    
    

default_path_1= "/root/backup_xeon_decoding_server_sep_21_2022"

default_path_2 = "/etc/systemd/system"

dvr_connection_systemd_service_ini_file = """[client_details]
client_name = {}
static_ip   = {}
username    = {}
password    = {}
port        = {}
cam_list    = {}
udp_ports   = {}"""


dvr_connection_systemd_service_file = """[Unit]
Description={}

[Service]
WorkingDirectory=/root/backup_xeon_decoding_server_sep_21_2022
ExecStart=/usr/bin/python3 dvr_to_cloud_ipv6_3.py {}

[Install]
WantedBy=multi-user.target"""

stream_decoding_shell_file=  """source  /opt/intel/dlstreamer/setupvars.sh
export GST_DEBUG=3
/opt/intel/dlstreamer/gstreamer/bin/gst-launch-1.0 -mvvv {}
"""
stream_decoding_shell_file_command = """udpsrc  name={} mtu=7000000 timeout=30000000000 port={}   !   queue  !    h264parse  ! video/x-h264,stream-format=byte-stream,alignment=nal ! vaapih264dec   !   vaapipostproc    ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate    ! video/x-raw,width={},height={} ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python_3.py class=custom_accumulator function=process_frame arg={{\\\\\\"cam_no\\\\\\":\\\\\\"{}\\\\\\"\,\\\\\\"accumulate_frames_no\\\\\\":\\\\\\"{}\\\\\\"\,\\\\\\"rabbitmq_queue_name\\\\\\":\\\\\\"{}\\\\\\"}} ! fakesink async=false"""

stream_decoding_systemd_service_file  = """[Unit]
Description={}
After=network.target
StartLimitIntervalSec=0

[Service]
Restart=always
WorkingDirectory=/root/backup_xeon_decoding_server_sep_21_2022
ExecStart=/bin/bash {}
StandardError=append:/var/log/{}.log
Restart=on-failure

[Install]
WantedBy=multi-user.target

"""

fluentbit_systemd_service_config_file = """[SERVICE]
    Flush 1
    Daemon Off
    Log_Level info

[INPUT]
    Name systemd
    Tag *
    Systemd_Filter _SYSTEMD_UNIT={}
    Read_From_Tail true


[FILTER]
    Name grep
    Match *
    regex MESSAGE GstUDPSrcTimeout


[OUTPUT]
    Name http
    Match *
    Host 127.0.0.1
    Port 60000
    Format json
    URI   /restart_dvr_connection
"""

fluentbit_systemd_service_file = """[Unit]
Description={}
Requires=network.target
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/backup_xeon_decoding_server_sep_21_2022
ExecStart=/opt/fluent-bit/bin/fluent-bit -c {}

[Install]
WantedBy=multi-user.target
"""


def write_file_to_directory(file_name,file_path,data):
    try:

        with open(file_path+"/"+file_name,"w")as file_:
            file_.write(data)
    except Exception as e:
        return e
    return True

def restart_service(systemd_service_name):
    sysbus = dbus.SystemBus()
    systemd1 = sysbus.get_object('org.freedesktop.systemd1',     '/org/freedesktop/systemd1')
    manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
    job = manager.RestartUnit(systemd_service_name, 'fail')

    return job


db = pymysql.connect(host='127.0.0.1',user='root',password="cctv@ai#SOFTWARE007",database="cctv_ai_usecase_products",charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
@app.route('/pipeline_management_admin', methods=['GET'])
def pipeline_management_home_page():
    
    return render_template('index.html')


@app.route('/add_new_static_ip_with_port', methods=['GET','POST'])
def pipeline_management_1():
    if request.method == 'GET':
        return render_template('new_static_ip_port_pipeline.html',template_var1="")
    else:
        important_dict = request.form.to_dict(flat=False)
        print(request.form.to_dict(flat=False))
        if important_dict['username'][0]=='root' and important_dict['pwd'][0]=='cctv@ai#SOFTWARE007':
            dvr_static_ip = important_dict['dvr_static_ip'][0]
            dvr_port = important_dict['dvr_port'][0]
            dvr_user_name = important_dict['dvr_user_name'][0]
            dvr_password = important_dict['dvr_password'][0]
            dvr_port = important_dict['dvr_port'][0]

            if dvr_static_ip == "" or dvr_port=="" or len(dvr_static_ip.split("."))!=4:
                return render_template('new_static_ip_port_pipeline.html',template_var1="Un supported values entered for port and ip") 
            if dvr_user_name=='' or dvr_password == '' or dvr_port == '':
                return render_template('new_static_ip_port_pipeline.html',template_var1="dvr password or dvr username or dvr port  is empty ")
            cursor = db.cursor()
            sql = "SELECT * FROM `customer_deployment_table`"
            cursor.execute(sql)
            results = cursor.fetchall()
            sanity_check_1 = len(results)
            allow = True
            ports_per_static_ip ={dvr_static_ip:0}
            for dct in results:
                if dct['dvr_static_ip'] == dvr_static_ip:
                    ports_per_static_ip[dvr_static_ip]+=1
                if (dct['dvr_static_ip']== dvr_static_ip) and (dct['dvr_port']==dvr_port):
                    allow =False
            if allow== False:
                return render_template('new_static_ip_port_pipeline.html',template_var1="static ip with port already exists") 
            else:
                if ports_per_static_ip[dvr_static_ip]>=3:
                    return render_template('new_static_ip_port_pipeline.html',template_var1="ports per static ip exceeded limit 3") 
                else:
                    unique_client_id_per_static_ip_verification = []
                    for dct_2 in results:
                        if dct_2['dvr_static_ip']==dvr_static_ip:
                            unique_client_id_per_static_ip_verification.append(dct_2['client_id_in_system'])
                    assignment_for_client_id_in_system = None
                    allocated_udp_range_per_static_ip_plus_port_per_client = None

                    if len(list(set(unique_client_id_per_static_ip_verification))) > 1:
                        return render_template('new_static_ip_port_pipeline.html',template_var1="two different client id s have same static ip, immediately check database") 
                    
                    
                    elif len(list(set(unique_client_id_per_static_ip_verification)))==0:
                        cursor = db.cursor()
                        sql = "SELECT * FROM `customer_deployment_table`"
                        cursor.execute(sql)
                        temp_results = cursor.fetchall()
                        sanity_check_2 = len(temp_results)
                        if sanity_check_2 != sanity_check_1:
                            return render_template('new_static_ip_port_pipeline.html',template_var1="database changed in between validations and computations ! hence cant proceed ! make sure only one admin use the db at one time")

                        client_id_in_system_list = []
                        for dct_3 in temp_results:
                            client_id_in_system_list.append(dct_3['client_id_in_system'])
                        if client_id_in_system_list==[]:
                            assignment_for_client_id_in_system  = 'client_1'
                        else:
                            assignment_for_client_id_in_system  = "client_"+str(int(sorted(client_id_in_system_list)[-1].split("_")[1])+1)
                        if assignment_for_client_id_in_system=='client_1':
                            allocated_udp_range_per_static_ip_plus_port_per_client = "11000-11015"
                        else:
                            cursor = db.cursor()
                            sql = "SELECT * FROM `customer_deployment_table`"
                            cursor.execute(sql)
                            temp_results_2 = cursor.fetchall()
                            sanity_check_3  = len(temp_results_2)
                            if sanity_check_3!=sanity_check_2:
                                return render_template('new_static_ip_port_pipeline.html',template_var1="database changed in between validations and computations ! hence cant proceed ! make sure only one admin use the db at one time")
                            udp_range_per_static_ip_plus_port_per_client_list = []
                            for dct_4 in temp_results_2:
                                port_1,port_2 = dct_4['allocated_udp_range_per_static_ip_plus_port_per_client'].split("-")
                                port_1 = int(port_1)
                                port_2 = int(port_2)
                                udp_range_per_static_ip_plus_port_per_client_list.append(port_1)
                                udp_range_per_static_ip_plus_port_per_client_list.append(port_2)
                            
                            highest_used_port = sorted(udp_range_per_static_ip_plus_port_per_client_list)[-1]
                            
                            allocated_udp_range_per_static_ip_plus_port_per_client = str(highest_used_port+1)+"-"+str(highest_used_port+1+15)


                    elif len(list(set(unique_client_id_per_static_ip_verification)))==1:
                        assignment_for_client_id_in_system = unique_client_id_per_static_ip_verification[0]
                        cursor = db.cursor()
                        sql = "SELECT * FROM `customer_deployment_table`"
                        cursor.execute(sql)
                        temp_results_3 = cursor.fetchall()
                        sanity_check_4  = len(temp_results_3)
                        if sanity_check_4!=sanity_check_1:
                            return render_template('new_static_ip_port_pipeline.html',template_var1="database changed in between validations and computations ! hence cant proceed ! make sure only one admin use the db at one time")
                        udp_range_per_static_ip_plus_port_per_client_list = []
                        for dct_5 in temp_results_3:
                            port_1_1,port_2_1 = dct_5['allocated_udp_range_per_static_ip_plus_port_per_client'].split("-")
                            port_1_1 = int(port_1_1)
                            port_2_1 = int(port_2_1)
                            udp_range_per_static_ip_plus_port_per_client_list.append(port_1_1)
                            udp_range_per_static_ip_plus_port_per_client_list.append(port_2_1)
                        
                        highest_used_port = sorted(udp_range_per_static_ip_plus_port_per_client_list)[-1]
                        
                        allocated_udp_range_per_static_ip_plus_port_per_client = str(highest_used_port+1)+"-"+str(highest_used_port+1+15)
                    
                    if allocated_udp_range_per_static_ip_plus_port_per_client is None or assignment_for_client_id_in_system is None:
                        return render_template('new_static_ip_port_pipeline.html',template_var1="edge case for calucating udp range and client id allocation,contact developer ")
                    print(allocated_udp_range_per_static_ip_plus_port_per_client,assignment_for_client_id_in_system)
                    if len(important_dict['subscribed_usecases']) == 1:
                        if important_dict['subscribed_usecases'][0]=='':
                            return render_template('new_static_ip_port_pipeline.html',template_var1="empty use case name")
                        # if important_dict['subscribed_usecases'][0]!="fire_detection"
                        if important_dict['cam_number_list'][0]=='':
                            return render_template('new_static_ip_port_pipeline.html',template_var1="empty cam_number_list")
                        if important_dict['image_width_per_usecase'][0]=='' or important_dict['image_height_per_usecase']=='':
                            return render_template('new_static_ip_port_pipeline.html',template_var1="empty image height or width")
                        if important_dict['frame_aggregration_per_usecase'][0]=='':
                            return render_template('new_static_ip_port_pipeline.html',template_var1="frame_aggregration_per_usecase")

                        else:
                            if important_dict['subscribed_usecases'][0]=="fire_detection":
                                dvr_connection_systemd_service_name = "_".join([assignment_for_client_id_in_system,"_".join(dvr_static_ip.split(".")),dvr_port,"dvr_connection.service"])
                                stream_decoding_systemd_service_name = "_".join([assignment_for_client_id_in_system,"_".join(dvr_static_ip.split(".")),dvr_port,"stream_decoding.service"])
                                fluentbit_systemd_service_name = "_".join([assignment_for_client_id_in_system,"_".join(dvr_static_ip.split(".")),dvr_port,"fluentbit.service"])
                                cam_number_list = important_dict['cam_number_list'][0]
                                frame_aggregration_per_usecase = important_dict['frame_aggregration_per_usecase'][0]
                                image_width_per_usecase = important_dict['image_width_per_usecase'][0]
                                image_height_per_usecase = important_dict['image_height_per_usecase'][0]
                                temp_port_1,temp_port_2 = allocated_udp_range_per_static_ip_plus_port_per_client.split("-")
                                temp_port_1,temp_port_2 = int(temp_port_1),int(temp_port_2)
                                temp_port_list  = [port_number for port_number in range(temp_port_1,temp_port_2+1)]
                                cam_number_to_udp_port_mapping_list = ",".join(str(temp_port_list[int(temp_cam_number)-1]) for temp_cam_number in cam_number_list.split(","))
                                dvr_connection_systemd_service_ini_data =  dvr_connection_systemd_service_ini_file.format(assignment_for_client_id_in_system,dvr_static_ip,dvr_user_name,dvr_password,dvr_port,cam_number_list,cam_number_to_udp_port_mapping_list)
                                dvr_connection_systemd_service_ini_file_name =  dvr_connection_systemd_service_name.replace("service","ini")

                                cam_description_list = important_dict["cam_description_list"][0]

                                cams_with_call_service_per_usecase = important_dict["cams_with_call_service_per_usecase"][0]

                                cams_with_whatsapp_service_per_usecase = important_dict["cams_with_whatsapp_service_per_usecase"][0]

                                cams_with_whatsapp_service_per_usecase_list = cams_with_whatsapp_service_per_usecase.split(",")

                                cams_with_call_service_per_usecase_list = cams_with_call_service_per_usecase.split(",")

                                deafault_entries = []

                                for tmp_cam_no in cam_number_list.split(","):
                                    if (tmp_cam_no not in cams_with_call_service_per_usecase_list) and (tmp_cam_no not in cams_with_whatsapp_service_per_usecase_list):
                                        deafault_entries.append(tmp_cam_no)

                                if (deafault_entries!=[]) or (len(deafault_entries)!=0):
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="some cameras were not in both call or whatsapp serices {}".format(deafault_entries))


                                if len(cam_description_list.split("#"))!=len(cam_number_list.split(",")):
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="cam description length and cam number length not matching !")

                                state = write_file_to_directory(dvr_connection_systemd_service_ini_file_name,default_path_1,dvr_connection_systemd_service_ini_data)
                                if state == True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")
                                
                                # state_2 = write_file_to_directory(dvr_connection_systemd_service_ini_file_name,default_path_2,dvr_connection_systemd_service_ini_data)

                                # if state_2 == True:
                                #     pass
                                # else:
                                #     return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")

                                dvr_connection_systemd_service_file_data = dvr_connection_systemd_service_file.format(dvr_connection_systemd_service_name,dvr_connection_systemd_service_ini_file_name)

                                state_2 = write_file_to_directory(dvr_connection_systemd_service_name,default_path_1,dvr_connection_systemd_service_file_data)
                                if state_2 == True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")

                                state_3 = write_file_to_directory(dvr_connection_systemd_service_name,default_path_2,dvr_connection_systemd_service_file_data)

                                if state_3 == True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")
                                stream_decoding_shell_file_command_list = []

                                for current_cam in cam_number_list.split(","):

                                    cam_name =  "_".join([assignment_for_client_id_in_system,"_".join(dvr_static_ip.split(".")),dvr_port,"cam",current_cam])

                                    temp_port_list 
                                    current_stream_decoding_shell_file_command =  stream_decoding_shell_file_command.format(cam_name,temp_port_list[int(current_cam)-1],image_width_per_usecase,image_height_per_usecase,cam_name,frame_aggregration_per_usecase,important_dict['subscribed_usecases'][0])

                                    stream_decoding_shell_file_command_list.append(current_stream_decoding_shell_file_command)
                                
                                stream_decoding_shell_file_data =  stream_decoding_shell_file.format("    ".join(stream_decoding_shell_file_command_list))

                                stream_decoding_shell_file_name = stream_decoding_systemd_service_name.replace("service","sh")

                                state_4 = write_file_to_directory(stream_decoding_shell_file_name,default_path_1,stream_decoding_shell_file_data)

                                if state_4==True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")

                                stream_decoding_systemd_service_file_data = stream_decoding_systemd_service_file.format(stream_decoding_systemd_service_name,stream_decoding_shell_file_name,stream_decoding_systemd_service_name.replace(".service",""))

                                state_5  = write_file_to_directory(stream_decoding_systemd_service_name,default_path_1,stream_decoding_systemd_service_file_data)

                                if state_5==True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")

                                state_6  = write_file_to_directory(stream_decoding_systemd_service_name,default_path_2,stream_decoding_systemd_service_file_data)

                                if state_6==True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")

                                fluentbit_systemd_service_config_file_data = fluentbit_systemd_service_config_file.format(stream_decoding_systemd_service_name)

                                fluentbit_systemd_service_config_file_name = fluentbit_systemd_service_name.replace("service","conf")

                                state_7 = write_file_to_directory(fluentbit_systemd_service_config_file_name,default_path_1,fluentbit_systemd_service_config_file_data)

                                if state_7 == True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")
                                
                                fluentbit_systemd_service_file_data = fluentbit_systemd_service_file.format(fluentbit_systemd_service_name,fluentbit_systemd_service_config_file_name)

                                state_8 = write_file_to_directory(fluentbit_systemd_service_name,default_path_1,fluentbit_systemd_service_file_data)

                                if state_8 == True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")
                                
                                state_9 = write_file_to_directory(fluentbit_systemd_service_name,default_path_2,fluentbit_systemd_service_file_data)

                                if state_9 == True:
                                    pass
                                else:
                                    return render_template('new_static_ip_port_pipeline.html',template_var1="folder permission issue and unable to write file to folder ")
                                
                                
                                print(dvr_connection_systemd_service_file_data)
                                print(fluentbit_systemd_service_config_file_data,fluentbit_systemd_service_config_file_name)
                                print(fluentbit_systemd_service_file_data)
                                print(stream_decoding_systemd_service_file_data)
                                completed_process = subprocess.run(["sudo", "systemctl","daemon-reload"])
                                print(completed_process.check_returncode())

                                completed_process_2 = subprocess.run(["sudo","chmod","777",default_path_1+"/"+stream_decoding_shell_file_name])

                                print(completed_process_2.check_returncode())

                                job_1 = restart_service(fluentbit_systemd_service_name)
                                print(job_1)

                                job_2 = restart_service(stream_decoding_systemd_service_name)

                                print(job_2)

                                job_3 = restart_service(dvr_connection_systemd_service_name)

                                print(job_3)


                                cursor_final = db.cursor()
                                batch_id = int(cursor_final.execute('select last_insert_id() from customer_deployment_table'))

                                STATEMENT = """insert into `customer_deployment_table` values ("""+",".join(["%s"]*25)+""")"""

                                values = [batch_id+1,"something",assignment_for_client_id_in_system,important_dict['subscribed_usecases'][0],
                                dvr_static_ip,dvr_port,important_dict["dvr_connection_protocol"][0],dvr_user_name,dvr_password,
                                dvr_connection_systemd_service_name,stream_decoding_systemd_service_name,image_width_per_usecase,
                                image_height_per_usecase,frame_aggregration_per_usecase,fluentbit_systemd_service_name,"consumer_inference.service",
                                cam_number_list,cam_number_to_udp_port_mapping_list,important_dict["cam_description_list"][0],
                                allocated_udp_range_per_static_ip_plus_port_per_client,important_dict['subscribed_usecases'][0],
                                important_dict["cams_with_call_service_per_usecase"][0],important_dict["cams_with_whatsapp_service_per_usecase"][0],
                                important_dict["subscribed_phone_numbers_for_call"][0],important_dict["subscribed_phone_numbers_for_whatsapp"][0]
                                ]

                                cursor_final.execute(STATEMENT,values)
                                db.commit()


                                return render_template('new_static_ip_port_pipeline.html',template_var1="launched pipeline ")


                            else:
                                return render_template('new_static_ip_port_pipeline.html',template_var1="will implement multi use case deployment in near future , currently fire_detection is only suported ")
                    else:
                        # Implement for multi use case in near future 
                        return render_template('new_static_ip_port_pipeline.html',template_var1="will implement multi use case deployment in near future ,contact developer for this")






            

            return render_template('new_static_ip_port_pipeline.html',template_var1="yes for now") 

        else:
            return render_template('new_static_ip_port_pipeline.html',template_var1="UN authenitcated user")

@app.route('/restart_dvr_connection', methods=['POST'])
def restart_dahua_sdk():
    content_list = request.json
    
    # print(content['MESSAGE'])
    client_list = []
    for content in content_list:
        required_client_id = None
        for words in content['MESSAGE'].split(" "):
            if "client" in words:
                required_client_id = words.replace("\"","")

        if required_client_id is None:
            raise Exception("Failure in parsing gstreamer service ")
        temp=required_client_id.replace("cam","").split("__")[0]
        client_list.append(temp)
    
    assert len(list(set(client_list)))==1
    sysbus = dbus.SystemBus()
    systemd1 = sysbus.get_object('org.freedesktop.systemd1',     '/org/freedesktop/systemd1')
    manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
    # state = manager.GetUnit("xeon_e2286g_ubuntu_20_vaapi.service")
    # print(state)
    crate_unit = manager.LoadUnit(client_list[0]+"_dvr_connection.service")
    crate_proxy = sysbus.get_object('org.freedesktop.systemd1', str(crate_unit))
    crate = Interface(crate_proxy, dbus_interface='org.freedesktop.systemd1.Unit')
    temp = crate_proxy.Get('org.freedesktop.systemd1.Unit',  # interface that defines the property
                    'ActiveEnterTimestamp',                    # name of the property
                    dbus_interface='org.freedesktop.DBus.Properties') # in
    var = time.time() % 1   
    time1 = datetime.datetime.fromtimestamp(temp/1e6)
    time2 = datetime.datetime.fromtimestamp(time.time())
    time_difference = time2 - time1
    print(time_difference.total_seconds())             
    if (temp == 0) or time_difference.total_seconds()>35:
        job = manager.RestartUnit(client_list[0]+"_dvr_connection.service", 'fail')
        job2 = manager.RestartUnit(client_list[0]+"_stream_decoding.service","fail")
        print(job,job2)
        print(time2,time1,time_difference.total_seconds(),job,job2)
        return "Succeded"
    else:
        return "ignored due to {} {} {}".format(time2,time1,time_difference.total_seconds())




    return "Hello World!"

@app.route('/fire_alert_mechanism',methods=['POST'])
def alert_mechanism_for_fire_detection():
    
    try:

        print(request.json,"here it is request from consumer server")
        alert_json = request.get_json()
        mp4_payload =  alert_json["mp4_payload"]
        cam_no =  alert_json["cam_no"]
        server_public_ip_address = alert_json["server_public_ip_address"]
        password = "cctv@ai#SOFTWARE007" 
        is_infinite_loop = False
        number_of_times_to_call = 6

        temp_thread = Thread(target = alert_mechanism,args=(cam_no,mp4_payload,server_public_ip_address,password,is_infinite_loop,number_of_times_to_call,))
        temp_thread.start()

        return "Started Fire alert"

    except Exception as error_3:
        return str(error_3)
    


@app.route('/restart_gstreamer_service/', methods=['POST'])
def restart_gstreamer():
    content = request.json
    
    print(content['MESSAGE'])

    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)
