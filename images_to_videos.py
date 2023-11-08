import cv2
import numpy as np

# choose codec according to format needed
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('head_straight_with_2_to_3_head_bobs.mp4', fourcc, 4, (640,480))

for i in range(0,229):
    img = cv2.imread("data_5/data_drawn_image_"+str(i) + '.png')
    video.write(img)

# cv2.destroyAllWindows()
video.release()