import cv2
import imagezmq
import mediapipe as mp

# from picamera2.array import PiRGBArray
from picamera2 import Picamera2
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
#mp_drawing = mp.solutions.drawing_utils
denormalize_coordinates = mp_drawing._normalized_to_pixel_coordinates
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('GTK3Agg')
import socket, numpy, pickle   
import subprocess
# For webcam input:
import sys
import ffmpeg
import base64
import time 
import json
video_format = "sdl"
server_url = "SDL output"
eye_idxs = {
            "left": [362, 385, 387, 263, 373, 380],
            "right": [33, 160, 158, 133, 153, 144],
        }
thresholds = {
    "EAR_THRESH": 0.08,
    "WAIT_TIME": 2,
}

RED = (0, 0, 255)  # BGR
GREEN = (0, 255, 0)
frame_w  = 640
frame_h = 480
ALM_txt_pos = (10, int(frame_h // 2 * 1.85))
ALM_txt_pos_altr = (10, int(frame_h // 3 * 1.85))
ALM_txt_pos_altr_altr = (10, int(frame_h // 4 * 1.85))
is_already_closed = False
def plot_text(image, text, origin, 
              color, font=cv2.FONT_HERSHEY_SIMPLEX, 
              fntScale=0.8, thickness=2
              ):
    image = cv2.putText(image, text, origin, font, fntScale, color, thickness)
    return image
def distance(point_1, point_2):
    """Calculate l2-norm between two points"""
    dist = sum([(i - j) ** 2 for i, j in zip(point_1, point_2)]) ** 0.5
    return dist
def get_ear(landmarks, refer_idxs, frame_width, frame_height):
    """
    Calculate Eye Aspect Ratio for one eye.
 
    Args:
        landmarks: (list) Detected landmarks list
        refer_idxs: (list) Index positions of the chosen landmarks
                            in order P1, P2, P3, P4, P5, P6
        frame_width: (int) Width of captured frame
        frame_height: (int) Height of captured frame
 
    Returns:
        ear: (float) Eye aspect ratio
    """
    try:
        # Compute the euclidean distance between the horizontal
        coords_points = []
        for i in refer_idxs:
            lm = landmarks[i]
            coord = denormalize_coordinates(lm.x, lm.y, 
                                             frame_width, frame_height)
            coords_points.append(coord)
 
        # Eye landmark (x, y)-coordinates
        P2_P6 = distance(coords_points[1], coords_points[5])
        P3_P5 = distance(coords_points[2], coords_points[4])
        P1_P4 = distance(coords_points[0], coords_points[3])
 
        # Compute the eye aspect ratio
        ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)
 
    except:
        ear = 0.0
        coords_points = None
 
    return ear, coords_points
def calculate_avg_ear(landmarks, left_eye_idxs, right_eye_idxs, image_w, image_h):
    """Calculate Eye aspect ratio"""
 
    left_ear, left_lm_coordinates = get_ear(
                                      landmarks, 
                                      left_eye_idxs, 
                                      image_w, 
                                      image_h
                                    )
    right_ear, right_lm_coordinates = get_ear(
                                      landmarks, 
                                      right_eye_idxs, 
                                      image_w, 
                                      image_h
                                    )
    Avg_EAR = (left_ear + right_ear) / 2.0
 
    return Avg_EAR, (left_lm_coordinates, right_lm_coordinates),left_ear,right_ear

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '192.168.0.118'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9999
i=0
socket_address = (host_ip,port)
#server_socket.bind(socket_address)
print('Listening at:',socket_address)
#ffmpeg_process = open_ffmpeg_stream_process()
#ffmpeg_process = start_streaming(640,480,9)
#s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  # Gives UDP protocol to follow
#s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10000000) # setSockoptTo open two protocols,SOL_SOCKET: Request applies to socket layer.
#serverip="192.168.0.118"       # Server public IP
#serverport=2323   
#video_out = cv2.VideoWriter("appsrc ! videoconvert ! jpegenc ! rtpjpegpay ! rtpstreampay  ! udpsink host=192.168.0.118 port=5001", cv2.CAP_GSTREAMER, 0, 24, (800,600), True)
#video_out = cv2.VideoWriter("appsrc ! videoconvert ! video/x-raw,format=I420 ! jpegenc ! rtpjpegpay ! rtpstreampay ! udpsink host=192.168.0.118 port=5001", cv2.CAP_GSTREAMER, 0, 24, (800, 600), True)
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
#sender = imagezmq.ImageSender(connect_to='tcp://192.168.0.1:5555')
#rpi_name = socket.gethostname()
cap = cv2.VideoCapture("udp://192.168.0.118:5000")
start = None
with mp_face_mesh.FaceMesh(
    max_num_faces=3,
    refine_landmarks=True,
    min_detection_confidence=0.45,
    min_tracking_confidence=0.12) as face_mesh:
    print(face_mesh,"haha")
    # initialize the camera and grab a reference to the raw camera capture
    # camera = PiCamera2()
    # camera.resolution = (640, 480)
    # camera.framerate = 32
    # rawCapture = PiRGBArray(camera, size=(640, 480))
    # allow the camera to warmup
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration({"size": (640, 480)}))
    picam2.set_controls({'Saturation': 0,'FrameRate': 8})
    # picam2.start_preview(Preview.QTGL)
    picam2.start()
    time.sleep(0.1)
    counter_increment = 0
    # capture frames from the camera
    # for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    while 1:
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image  = picam2.capture_array()
        # show the frame
        # cv2.imshow("Frame", image)
        # key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        # rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        # if key == ord("q"):
            # break
    # while cap.isOpened():
        # success, image = cap.read()
        # print(success)
        if not 1:
            pass
        #cap.release()
        #print("Ignoring empty camera frame.")
        #cap = cv2.VideoCapture("udp://192.168.0.118:5000")      # If loading a video, use 'break' instead of 'continue'.
        #success, image = cap.read()

        #continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        else:
            print("what happened ",image.shape)
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image)

            # Draw the face mesh annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_face_landmarks:
                print("results TRue")
            else:
                print("probably face missing")
            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0].landmark
                face_3d = []
                face_2d = []
                for idx, lm in enumerate(landmarks):
                    if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                        img_h, img_w, img_c = image.shape
                        if idx == 1:
                            nose_2d = (lm.x * img_w, lm.y * img_h)
                            nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)
                        

                        x, y = int(lm.x * img_w), int(lm.y * img_h)

                        # Get the 2D Coordinates
                        face_2d.append([x, y])

                        # Get the 3D Coordinates
                        face_3d.append([x, y, lm.z])       
                
                # Convert it to the NumPy array
                face_2d = np.array(face_2d, dtype=np.float64)

                # Convert it to the NumPy array
                face_3d = np.array(face_3d, dtype=np.float64)

                # The camera matrix
                focal_length = 1 * img_w

                cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                        [0, focal_length, img_w / 2],
                                        [0, 0, 1]])

                # The Distance Matrix
                dist_matrix = np.zeros((4, 1), dtype=np.float64)

                # Solve PnP
                success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                # Get rotational matrix
                rmat, jac = cv2.Rodrigues(rot_vec)

                # Get angles
                angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)
                print("angles",angles[0]*360,angles[1]*360,angles[2]*360)
                angle_x,angle_y,angle_z =  angles[0]*360,angles[1]*360,angles[2]*360

                EAR, coordinates,left_ear,right_ear = calculate_avg_ear(landmarks,
                                                            eye_idxs["left"], 
                                                            eye_idxs["right"], 
                                                            frame_w, 
                                                            frame_h
                                                            )
                cv2.imwrite("data/data_image_{}.png".format(counter_increment),image)
                with open("data/data_ear_rotation_{}.json".format(counter_increment),"w") as fp:
                    fp.write(json.dumps({"ear":EAR,"left_ear":left_ear,"right_ear":right_ear,"angle_x":angle_x,"angle_y":angle_y,"angle_z":angle_z}))
                # print()
                if EAR<thresholds["EAR_THRESH"]:
            #         if is_already_closed :
            #             micro_sleep_time = time.time()-start
            #             if micro_sleep_time >  thresholds["WAIT_TIME"]:
                    #plot_text(image, "ear : {} , left_ear : {} ,  right_ear : {} ".format(str(EAR)[:5],str(left_ear)[:5],str(right_ear)[:5]),
                    #                        ALM_txt_pos_altr, RED)
                    plot_text(image, ", angle_x: {} ".format(str(angle_x)[:5]),
                                            ALM_txt_pos, RED)
                    plot_text(image, ", angle_y: {} ".format(str(angle_y)[:5]),
                                            ALM_txt_pos_altr, RED)
                    plot_text(image, ", angle_z: {} ".format(str(angle_z)[:5]),
                                            ALM_txt_pos_altr_altr, RED)

            #         else:
                        
            #             start = time.time()
            #             is_already_closed = True
            # #         plot_text(image, "EYES CLOSED !",
            # #                              ALM_txt_pos, RED)
                    print("eyes closed ? ",EAR,left_ear,right_ear)
                else:
                    # plot_text(image, "ear : {} , left_ear : {} ,  right_ear : {} ".format(str(EAR)[:5],str(left_ear)[:5],str(right_ear)[:5]),
                                            # ALM_txt_pos_altr, GREEN)
                    # plot_text(image, ", angle_x: {} ,angle_y: {} ,angle_z : {} ".format(str(angle_x)[:5],str(angle_y)[:5],str(angle_z)[:5]),
                                            # ALM_txt_pos, GREEN)
                    plot_text(image, ", angle_x: {} ".format(str(angle_x)[:5]),
                                            ALM_txt_pos, GREEN)
                    plot_text(image, ", angle_y: {} ".format(str(angle_y)[:5]),
                                            ALM_txt_pos_altr, GREEN)
                    plot_text(image, ", angle_z: {} ".format(str(angle_z)[:5]),
                                            ALM_txt_pos_altr_altr, GREEN)

                    print("eyes open ? ",EAR,left_ear,right_ear)
            #         if is_already_closed:
            #             is_already_closed = False

                for face_landmarks in results.multi_face_landmarks:
            #        mp_drawing.draw_landmarks(
            #            image=image,
            #            landmark_list=face_landmarks,
            #            connections=mp_face_mesh.FACEMESH_TESSELATION,
            #            landmark_drawing_spec=None,
            #            connection_drawing_spec=mp_drawing_styles
            #            .get_default_face_mesh_tesselation_style())
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles
                        .get_default_face_mesh_contours_style())
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_IRISES,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles
                        .get_default_face_mesh_iris_connections_style())
            # Flip the image horizontally for a selfie-view display.
        #    print(results.multi_face_landmarks)
        #    ffmpeg_process.stdin.write(image.astype(np.uint8).tobytes())
            print(image.shape)
            #framestring = image.tostring()
        #    sys.stdout.buffer.write(cv2.imencode(".jpg", image)[1].tostring())
        #    sender.send_image(rpi_name, image)

        #    cv2.imwrite("current_image_{}.png".format(i),image)
        #    i+=1
            cv2.imwrite("data/data_drawn_image_{}.png".format(counter_increment),image)
            counter_increment+=1
            encoded,buffer = cv2.imencode('.jpg',image,[cv2.IMWRITE_JPEG_QUALITY,80])
            message = base64.b64encode(buffer)
            server_socket.sendto(message,(host_ip,9999))
        #    res=video_out.write(image)
        #    print("written succeed ? ",res)
            #ret, buffer = cv2.imencode(".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY),30])  # ret will returns whether connected or not, Encode image from image to Buffer code(like [123,123,432....])
            #x_as_bytes = pickle.dumps(buffer)       # Convert normal buffer Code(like [123,123,432....]) to Byte code(like b"\x00lOCI\xf6\xd4...")
            #s.sendto(x_as_bytes,(serverip , serverport)) #
        #   plt.imshow(image)
        #    plt.pause(0.001)
            #cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
        
cap.release()
#video_out.release()
#ffmpeg_process.stdin.close()
#ffmpeg_process.wait()
