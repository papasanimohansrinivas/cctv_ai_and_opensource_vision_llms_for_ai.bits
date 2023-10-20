import select
import sys
from systemd import journal
from threading import Thread

def gmail_alert(message):
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

    sent_subject = "video not coming to server !!!"
    sent_body = ("\n".join(message))

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
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)


j = journal.Reader()
j.log_level(journal.LOG_INFO)

j.add_match(_SYSTEMD_UNIT="xeon_e2286g_ubuntu_20_vaapi.service")
j.seek_tail()
j.get_previous()
# j.get_next() # it seems this is not necessary.

p = select.poll()
p.register(j, j.get_events())

message_buffer = []
start = False

while p.poll():
    var = j.process()
    print(var)
    if var == journal.APPEND:
        try:
            print(j,"woooow")
            for entry in j:
                print(entry)
                if entry['MESSAGE'] != "":
                    if "GstUDPSrcTimeout" in entry["MESSAGE"]:
                        if start == False:
                            start = True
                        message_buffer.append(entry["MESSAGE"])
                        
                        print(entry['MESSAGE'])
                    else:
                        print(entry["MESSAGE"],"NOT required")
                else:
                    print("final wait")
            else:
                print("yay",start)
                if start:
                    temp_thread = Thread(target = gmail_alert,args=(message_buffer,))
                    temp_thread.start()
                    start = False
                    message_buffer =[]
                # print("yaay",j)  

        except Exception as e:
            print("what is the execption ",e)
        except KeyboardInterrupt:
            print("..exiting")
            sys.exit(1)
    elif var == journal.INVALIDATE or var== journal.NOP:
        print("i think system waiting ",start)
        
