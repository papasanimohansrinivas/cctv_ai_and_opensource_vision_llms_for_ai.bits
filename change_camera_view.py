import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# To open matplotlib in interactive mode
# %matplotlib qt5
 
 
# Load the image
img = cv2.imread('/home/mohan/backup_cloud_gpu_2_feb_1_2023/fire_class_per_cam.v6i.yolov5pytorch/train/images/client_1_49_206_199_97_25001_cam_4_1677335363_fire_pred_png.rf.66665ec22ba59fa02bfb2bbce3d57b6a.jpg') 
 
# Create a copy of the image
img_copy = np.copy(img)
 
# Convert to RGB so as to display via matplotlib
# Using Matplotlib we can easily find the coordinates
# of the 4 points that is essential for finding the 
# transformation matrix
# img_copy = cv2.cvtColor(cv2.UMat(img_copy),cv2.COLOR_BGR2RGB)
print(img_copy.shape)
# plt.imshow(img_copy)
# plt.show()
n = 3
var = img_copy.shape[:2]
pt_A = [var[0],var[1]]
pt_B = [0, var[1]//n]
pt_C = [var[0]//n, 0]
pt_D = [var[0]//n,var[1]//n]
print(pt_B,pt_A,pt_C)
width_AD = np.sqrt(((pt_A[0] - pt_D[0]) ** 2) + ((pt_A[1] - pt_D[1]) ** 2))
width_BC = np.sqrt(((pt_B[0] - pt_C[0]) ** 2) + ((pt_B[1] - pt_C[1]) ** 2))
maxWidth = max(int(width_AD), int(width_BC))
 
 
height_AB = np.sqrt(((pt_A[0] - pt_B[0]) ** 2) + ((pt_A[1] - pt_B[1]) ** 2))
height_CD = np.sqrt(((pt_C[0] - pt_D[0]) ** 2) + ((pt_C[1] - pt_D[1]) ** 2))
maxHeight = max(int(height_AB), int(height_CD))
print(maxWidth,maxHeight)

input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
output_pts = np.float32([[0, 0],
                        [0, maxHeight - 1],
                        [maxWidth - 1, maxHeight - 1],
                        [maxWidth - 1, 0]])
M = cv2.getPerspectiveTransform(input_pts,output_pts)
print(M)
out = cv2.warpPerspective(img,M,(maxWidth, maxHeight),flags=cv2.INTER_LINEAR)
plt.imshow(out)
plt.show()