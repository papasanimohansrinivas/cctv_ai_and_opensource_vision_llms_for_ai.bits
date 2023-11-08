
# folder_name = "/home/mohan/backup_xeon_decoding_server_sep_21_2022/archive_2/dataset_4/train/fire"
folder_name = "/home/mohan/backup_cloud_gpu_2_feb_1_2023/"
# folder_name = "/home/mohan/backup_xeon_decoding_server_sep_21_2022"
# folder_name = "/home/mohan/backup_cloud_gpu_2_feb_1_2023"
# video_name = "client_1_49_206_199_97_25001_cam_15_1669404534_fire_pred.mp4"
# video_name = "smallschool_fire_splash_pool_002.mp4"
# video_name = "client_1_49_206_199_97_25004_cam_4_1669380117_fire_pred.mp4"
# video_name = "client_1_49_206_199_97_25004_cam_3_1669399041_fire_pred.mp4"
# video_name = "client_1_49_206_199_97_25004_cam_1_1669375544_fire_pred.mp4"
# video_name = "client_1_49_206_199_97_25001_cam_16_1669419933_fire_pred.mp4"
# video_name = "VID-20230115-WA0025.mp4"
# video_name = "VID-20230112-WA0016.mp4"
# video_name = "VID-20230112-WA0006.mp4"
# video_name = "20230204141844.mp4"
# video_name = "20230204141640.mp4"
# video_name = "smallschool_fire_gateview_000.mp4"
# video_name = "smallschool_fire_splash_pool_010.mp4"
# video_name = "client_1_49_206_199_97_25001_cam_4_1669443763_fire_pred.mp4"
# video_name = "smallschool_fire_gateview_001.mp4"
# video_name = "smallschool_fire_splash_pool_025.mp4"
# video_name = "20230303143012.mp4"
# video_name = "20230303143343.mp4"
# video_name = "20230303143709.mp4"
# video_name = "20230303144226.mp4"
# video_name = "20230303144421.mp4"
# video_name = "20230303144903.mp4"
# video_name = "20230303151234.mp4" 
# video_name = "20230303151455.mp4"
# video_name = "20230303151716.mp4"
video_name = "20230305095312.mp4"
import cv2 
import os
dest = folder_name+"/"+video_name.replace(".mp4","")
try:
    os.mkdir(dest)
except Exception as e:
    print(e)
vidcap = cv2.VideoCapture(folder_name+"/"+video_name)
success,image = vidcap.read()
count = 0
success = True
while success:
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    if success:
        stretch_near = cv2.resize(image, (640, 640),
               interpolation = cv2.INTER_CUBIC)

        cv2.imwrite(dest+"/" +"frame_%d.jpg" % count,stretch_near)     # save frame as JPEG file
    count += 1

