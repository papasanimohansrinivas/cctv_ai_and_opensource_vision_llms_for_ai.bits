import requests
import json
from hurry.filesize import size

"""lgixljgzyqmdhjvp"""
import time
mail_count=0
last_time  = time.time()
while 1:
    current_time = time.time()
    if current_time - last_time > 6:
        print("elapsed time ",current_time-last_time," making rabbit mq call")

        #time.sleep(6)
        memory_used = None
        try:
            data = {
                'username': 'guest',
                'password': 'guest'
            }
            resp = requests.get("http://localhost:15672/api/nodes",auth=(data["username"],data["password"]))
            try:
                json.loads(resp.text)[0]["mem_used"]
                memory_used = json.loads(resp.text)[0]["mem_used"]
            except Exception as err2:
                print("http response problem",err2,resp)
            if memory_used is not None:
                
            
                #!/usr/bin/env python3
                # -*- coding: utf-8 -*-
                # =============================================================================
                # Created By  : Jeromie Kirchoff
                # Created Date: Mon Aug 02 17:46:00 PDT 2018
                # =============================================================================
                # Imports
                # =============================================================================
                import smtplib

                # =============================================================================
                # SET EMAIL LOGIN REQUIREMENTS
                # =============================================================================
                gmail_user = 'papasani.mohansrinivas@gmail.com'
                gmail_app_password = 'lgixljgzyqmdhjvp'

                # =============================================================================
                # SET THE INFO ABOUT THE SAID EMAIL
                # =============================================================================
                sent_from = gmail_user
                sent_to = ['papasani.mohansrinivas@gmail.com', 'shekharpatel62@gmail.com']
                # sent_to = ['papasani.mohansrinivas@gmail.com']

                sent_subject = "RabbitMq fire_detection queue used up memory !!!"
                sent_body = ("memory used in the rabbit mq is this :- {}".format(size(memory_used)))

                email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

                # =============================================================================
                # SEND EMAIL OR DIE TRYING!!!
                # Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
                # =============================================================================
                if 4294967296 > memory_used:
                    print("not sending mail ","current memeory ",size(memory_used),"water mark ",size(4294967296))
                else:
                    if mail_count<=20:

                        try:
                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                            server.ehlo()
                            server.login(gmail_user, gmail_app_password)
                            server.sendmail(sent_from, sent_to, email_text)
                            server.close()

                            print('Email sent!')
                            mail_count+=1
                        except Exception as exception:
                            print("Error: %s!\n\n" % exception)


        except Exception as err:
            raise Exception("something happened")
        last_time = time.time()
