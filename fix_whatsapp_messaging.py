
import requests
pipeline_management_server_ip = "45.63.4.46"
server_public_ip_address = "45.77.156.45"
payload = {'server_public_ip_address':server_public_ip_address,
                            "mp4_payload":"client_1_49_206_199_97_25001_cam_3_1677347536_fire_pred.png",
                            "cam_no":"client_1_49_206_199_97_25001_cam_3_1677347536"
                            }
                            
resp=requests.post('http://{}:60000/fire_alert_mechanism'.format(pipeline_management_server_ip), json=payload)

print(resp.text,resp)

