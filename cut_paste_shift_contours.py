import cv2
import numpy as np


def scale_contour(cnt, scale):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cnt_norm = cnt - [cx, cy]
    cnt_scaled = cnt_norm * scale
    cnt_scaled = cnt_scaled + [cx, cy]
    cnt_scaled = cnt_scaled.astype(np.int32)

    return cnt_scaled

folder_ = "./fire_masks"
# image_name = "getimg_ai_img-7K6j6idbwET4LeBNw8gPDZ-removebg-preview.png"
# image_name = "getimg_ai_img-qEsLNATHaKp9MF33xaAzLz-removebg-preview.png"
image_name = "getimg_ai_img-YT8AjBgtecUMeGCT37EfSz-removebg-preview.png"
import cv2
import numpy as np
from PIL import Image
# import matplotlib.pyplot as plt

# Reading the image
im = cv2.imread(folder_+"/"+image_name)

# Converting image to grayscale
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Thresholding and getting contours from the image
ret, thresh = cv2.threshold(imgray, 0, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
im_copy = im.copy()
im_copy[np.where((im_copy==[0,0,0]).all(axis=2))] = [255,255,255]
print(len(contours),hierarchy)
cnt_scaled_list = []
boxes = []
for contour in contours:
    try:
        coef_x = 20
        coef_y = 20
        # cnt_scaled = scale_contour(contour,0.13)
        # contour[:, :, 0] = contour[:, :, 0] * coef_x
        # contour[:, :, 1] = contour[:, :,  1] * coef_y
        # cnt_scaled_list.append(contour)
        (x, y, w, h) = cv2.boundingRect(contour)
        boxes.append([x,y, x+w,y+h])
    except Exception :
        pass
print(len(cnt_scaled_list))
boxes = np.asarray(boxes)
left, top = np.min(boxes, axis=0)[:2]
right, bottom = np.max(boxes, axis=0)[2:]
h = top-bottom
w = right - left
y = ""
x = ""
# [y:y+h, x:x+w]
# (x,y),(x+w,y+h)
fire_box = im_copy[top:bottom,left:right]

color_converted = cv2.cvtColor(fire_box, cv2.COLOR_BGR2RGB)
pil_image=Image.fromarray(color_converted)
white_img = Image.new("RGB", (640, 640), (255, 255, 255))
print(fire_box.shape)
import os 
try:
    os.mkdir(image_name.replace(".png","")+"-"+"full_mask")
except Exception as e2:
    print(e2.__str__())


for i_h in range(0,640,20):

    for j_h in range(0,640,20):
        try:
            white_img = Image.new("RGB", (640, 640), (255, 255, 255))
            white_img.paste(pil_image,(i_h,j_h))
            final_image = image_name.replace(".png","")+"-"+"full_mask"+"/"+image_name.replace(".png","")+"-"+"full_mask_{}_{}.png".format(i_h,j_h)
            white_img.save(final_image)
            # temp_im = cv2.cvtColor(np.array(white_img), cv2.COLOR_RGB2BGR)
            # temp_imgray = cv2.cvtColor(temp_im, cv2.COLOR_BGR2GRAY)

            # temp_ret, temp_thresh = cv2.threshold(temp_imgray, 0, 255, 0)
            # temp_contours, temp_hierarchy = cv2.findContours(temp_thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            # temp_mask = np.zeros((640,640))
            
            # cv2.drawContours(temp_mask, temp_contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)
            # cv2.imwrite(final_image.replace(".png","-black_mask.png"),temp_thresh)

        except Exception as  e :
            print(e.__str__())

sample=cv2.imread("/home/mohan/backup_cloud_gpu_2_feb_1_2023/getimg_ai_img-7K6j6idbwET4LeBNw8gPDZ-removebg-preview-full_mask"+"/"+"getimg_ai_img-7K6j6idbwET4LeBNw8gPDZ-removebg-preview-full_mask_0_40.png")
# cv2.imshow("da",sample)
# cv2.waitKey(0)
for i_h_k in range(0,640,20):

    for j_h_k in range(0,640,20):
        try:
            final_image_1 = image_name.replace(".png","")+"-"+"full_mask"+"/"+image_name.replace(".png","")+"-"+"full_mask_{}_{}.png".format(i_h_k,j_h_k)
            # white_img.save(final_image)
            temp_im = cv2.imread(final_image_1)
            temp_imgray = cv2.cvtColor(temp_im, cv2.COLOR_BGR2GRAY)

            temp_ret, temp_thresh = cv2.threshold(temp_imgray, 254, 255, cv2.THRESH_BINARY)
            temp_contours, temp_hierarchy = cv2.findContours(temp_thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
            temp_mask = np.zeros((640,640,3))
            
            cv2.drawContours(temp_mask, temp_contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)
            print(temp_mask.shape)
            # cv2.imshow("a",temp_mask)
            cv2.imwrite(final_image_1.replace(".png","-black_mask.png"),255-temp_mask)

        except Exception as  e :
            print(e.__str__())

normal_img = Image.open("/home/mohan/backup_cloud_gpu_2_feb_1_2023/20230204141640"+"/"+"frame_4.jpg")
result_normal_img =  normal_img.resize((640,640),Image.ANTIALIAS)
result_normal_img.save("frame_4_640_640.png")



# cv2.imwrite("fire_1.png",fire_box)
# cv2.rectangle(im_copy, (left,top), (right,bottom), (255, 0, 0), 2)
# img_dark = np.zeros(im.shape)        
# cv2.drawContours(img_dark, cnt_scaled_list, -1, (0,255, 0), 3)
# plt.imshow(im)
# plt.axis("off");
# plt.show()
# cv2.imshow("ds",im_copy)
# cv2.waitKey(0)