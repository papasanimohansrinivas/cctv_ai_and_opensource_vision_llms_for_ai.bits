import random
random.seed(7)
import cv2
from matplotlib import pyplot as plt

import albumentations as A
from albumentations import *
import pybboxes as pbx
import itertools
BOX_COLOR = (255, 0, 0) # Red
TEXT_COLOR = (255, 255, 255) # White

def yolo_to_normal(bbox):
    x_min, y_min, w, h = [640*nm for nm  in bbox]
    W=H=640
    dw = 640
    dh = 640
    # x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)
    l = int((x_min - w / 2))
    r = int((x_min + w / 2))
    t = int((y_min - h / 2))
    b = int((y_min + h / 2) )
    x_min, x_max, y_min, y_max = l ,r,t,b

    return x_min,x_max,y_min,y_max


def visualize_bbox(img, bbox, class_name, color=BOX_COLOR, thickness=2):
    """Visualizes a single bounding box on the image"""
    x_min, y_min, w, h = [640*nm for nm  in bbox]
    W=H=640
    # x_min, y_min, w, h =  pbx.convert_bbox(bbox, from_type="yolo", to_type="coco", image_size=(W, H))
    # print(x_min, y_min, w, h)
    dw = 640
    dh = 640
    # x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)
    l = int((x_min - w / 2))
    r = int((x_min + w / 2))
    t = int((y_min - h / 2))
    b = int((y_min + h / 2) )
    x_min, x_max, y_min, y_max = l ,r,t,b
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)
    
    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)    
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
    cv2.putText(
        img,
        text=class_name,
        org=(x_min, y_min - int(0.3 * text_height)),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.35, 
        color=TEXT_COLOR, 
        lineType=cv2.LINE_AA,
    )
    return img


def visualize(image, bboxes, category_ids, category_id_to_name):
    img = image.copy()
    for bbox, category_id in zip(bboxes, category_ids):
        class_name = category_id_to_name[category_id]
        img = visualize_bbox(img, bbox, class_name)
    plt.figure(figsize=(12, 12))
    plt.axis('off')
    plt.imshow(img)
    plt.show()

base_folder = "/home/mohan/backup_cloud_gpu_2_feb_1_2023/"
base_dir = "fire_class_per_cam.v6i.yolov5pytorch/"
destination_dir = "fire_class_per_cam.v6i.yolov5pytorch_albumentations/"
test = "test/"
train = "train/"
valid = "valid/"

labels = "labels/"
import os 
images = "images/"

necessary_combinations = [(PiecewiseAffine(always_apply=True, p=0.5, scale=(0.03, 0.05), nb_rows=(4, 4), nb_cols=(4, 4), interpolation=1, mask_interpolation=0, cval=0, cval_mask=0, mode='constant', absolute_scale=False, keypoints_threshold=0.01), RandomSizedBBoxSafeCrop(always_apply=True, p=1.0, erosion_rate=0.0, height=640, width=640, interpolation=1)), (PiecewiseAffine(always_apply=True, p=0.5, scale=(0.03, 0.05), nb_rows=(4, 4), nb_cols=(4, 4), interpolation=1, mask_interpolation=0, cval=0, cval_mask=0, mode='constant', absolute_scale=False, keypoints_threshold=0.01), Cutout(always_apply=True, p=0.5, num_holes=8, max_h_size=8, max_w_size=16)), (PiecewiseAffine(always_apply=True, p=0.5, scale=(0.03, 0.05), nb_rows=(4, 4), nb_cols=(4, 4), interpolation=1, mask_interpolation=0, cval=0, cval_mask=0, mode='constant', absolute_scale=False, keypoints_threshold=0.01), ShiftScaleRotate(always_apply=True, p=1.0, shift_limit_x=(-0.0625, 0.0625), shift_limit_y=(-0.0625, 0.0625), scale_limit=(-0.09999999999999998, 0.10000000000000009), rotate_limit=(-45, 45), interpolation=1, border_mode=0, value=None, mask_value=None, rotate_method='largest_box')), (PiecewiseAffine(always_apply=True, p=0.5, scale=(0.03, 0.05), nb_rows=(4, 4), nb_cols=(4, 4), interpolation=1, mask_interpolation=0, cval=0, cval_mask=0, mode='constant', absolute_scale=False, keypoints_threshold=0.01), GridDistortion(always_apply=True, p=1.0, num_steps=5, distort_limit=(-0.8, 0.8), interpolation=1, border_mode=1, value=None, mask_value=None, normalized=False)), (RandomSizedBBoxSafeCrop(always_apply=True, p=1.0, erosion_rate=0.0, height=640, width=640, interpolation=1), Cutout(always_apply=True, p=0.5, num_holes=8, max_h_size=8, max_w_size=16)), (RandomSizedBBoxSafeCrop(always_apply=True, p=1.0, erosion_rate=0.0, height=640, width=640, interpolation=1), Perspective(always_apply=True, p=0.5, scale=(0.1, 0.4), keep_size=True, pad_mode=0, pad_val=0, mask_pad_val=0, fit_output=False, interpolation=1)), (RandomSizedBBoxSafeCrop(always_apply=True, p=1.0, erosion_rate=0.0, height=640, width=640, interpolation=1), ShiftScaleRotate(always_apply=True, p=1.0, shift_limit_x=(-0.0625, 0.0625), shift_limit_y=(-0.0625, 0.0625), scale_limit=(-0.09999999999999998, 0.10000000000000009), rotate_limit=(-45, 45), interpolation=1, border_mode=0, value=None, mask_value=None, rotate_method='largest_box')), (RandomSizedBBoxSafeCrop(always_apply=True, p=1.0, erosion_rate=0.0, height=640, width=640, interpolation=1), GridDistortion(always_apply=True, p=1.0, num_steps=5, distort_limit=(-0.8, 0.8), interpolation=1, border_mode=1, value=None, mask_value=None, normalized=False)),  (Cutout(always_apply=True, p=0.5, num_holes=8, max_h_size=8, max_w_size=16), ShiftScaleRotate(always_apply=True, p=1.0, shift_limit_x=(-0.0625, 0.0625), shift_limit_y=(-0.0625, 0.0625), scale_limit=(-0.09999999999999998, 0.10000000000000009), rotate_limit=(-45, 45), interpolation=1, border_mode=0, value=None, mask_value=None, rotate_method='largest_box')), (Cutout(always_apply=True, p=0.5, num_holes=8, max_h_size=8, max_w_size=16), GridDistortion(always_apply=True, p=1.0, num_steps=5, distort_limit=(-0.8, 0.8), interpolation=1, border_mode=1, value=None, mask_value=None, normalized=False)), (Perspective(always_apply=True, p=0.5, scale=(0.1, 0.4), keep_size=True, pad_mode=0, pad_val=0, mask_pad_val=0, fit_output=False, interpolation=1), ShiftScaleRotate(always_apply=True, p=1.0, shift_limit_x=(-0.0625, 0.0625), shift_limit_y=(-0.0625, 0.0625), scale_limit=(-0.09999999999999998, 0.10000000000000009), rotate_limit=(-45, 45), interpolation=1, border_mode=0, value=None, mask_value=None, rotate_method='largest_box')), (Perspective(always_apply=True, p=0.5, scale=(0.1, 0.4), keep_size=True, pad_mode=0, pad_val=0, mask_pad_val=0, fit_output=False, interpolation=1), GridDistortion(always_apply=True, p=1.0, num_steps=5, distort_limit=(-0.8, 0.8), interpolation=1, border_mode=1, value=None, mask_value=None, normalized=False)), (ShiftScaleRotate(always_apply=True, p=1.0, shift_limit_x=(-0.0625, 0.0625), shift_limit_y=(-0.0625, 0.0625), scale_limit=(-0.09999999999999998, 0.10000000000000009), rotate_limit=(-45, 45), interpolation=1, border_mode=0, value=None, mask_value=None, rotate_method='largest_box'), GridDistortion(always_apply=True, p=1.0, num_steps=5, distort_limit=(-0.8, 0.8), interpolation=1, border_mode=1, value=None, mask_value=None, normalized=False))]
category_id_to_name = {0: 'fire'}
for sub_folder in [train,valid,test]:
    images_folder = base_folder+base_dir+sub_folder+images
    labels_folder = base_folder+base_dir+sub_folder+labels
    for image_name  in os.listdir(images_folder):
        read_image_path = images_folder+image_name
        print(read_image_path)
        image = cv2.imread(read_image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        bboxes = []
        category_ids = []
        with open(labels_folder+image_name.replace(".jpg",".txt"))  as fl:
            
            for lines in fl.readlines():
                category_ids.append(int(lines.split(" ")[0]))
                bboxes.append([float(num) for num in lines.split(" ")[1:]])
            print(bboxes,category_ids)
        list_of_transforms = [A.PiecewiseAffine(always_apply=True),A.RandomSizedBBoxSafeCrop(640,640,always_apply=True) ,A.Cutout(always_apply=True,max_h_size=8, max_w_size=16) ,A.Perspective(always_apply=True,scale=(0.1, 0.4)),A.ShiftScaleRotate(always_apply=True,p=1.0,border_mode=0)]
        base_transform = A.Flip(always_apply=True,p=1.0)
        transforms_set_1 = [[base_transform,second_transform] for second_transform in list_of_transforms]
        
        print(list(itertools.combinations(list_of_transforms, 2)),"whats this")
        list_of_list_of_transforms = random.sample(necessary_combinations,7)+transforms_set_1
        print(list_of_list_of_transforms,"debug")
        count_1 = 1
        bbox_augmented_images = []
        cut_box = 1
        extra_images = [image.copy(),image.copy()]
        output_extra_images = [] 
        transform_bbox_3  = A.Compose([A.ShiftScaleRotate(always_apply=True,p=1.0,border_mode=0)])
        transform_bbox_4  = A.Compose([A.Affine(always_apply=True,p=1.0,shear=(-25,25))])    
        list_of_bbox_transforms = [transform_bbox_3,transform_bbox_4]

        for single_transform in list_of_bbox_transforms:

            

            for extra_image in extra_images: 
                
                
                # transform_bbox_1  = A.Compose([A.ShiftScaleRotate(shift_limit=0.325, scale_limit=0.50, rotate_limit=60,always_apply=True,p=1.0)])
                # transform_bbox_2  = A.Compose([A.Flip(always_apply=True,p=1.0)])
                
                
                for bbox_ in bboxes:
                    x_min,x_max,y_min,y_max = yolo_to_normal(bbox_)
                    bounding_box_cut_temp  = extra_image[y_min:y_max,x_min:x_max]
            
                    transformed_bbox_temp  = single_transform(image=bounding_box_cut_temp)

                    extra_image[y_min:y_max,x_min:x_max] = transformed_bbox_temp['image']
            
                    cv2.imwrite("cut_box_{}.png".format(cut_box),cv2.cvtColor(transformed_bbox_temp["image"], cv2.COLOR_BGR2RGB))
                    cut_box+=1
                output_extra_images.append(extra_image)
                        


 

        for trnsfrm_list in list_of_list_of_transforms:
            print(trnsfrm_list)
            transform = A.Compose(trnsfrm_list,bbox_params=A.BboxParams(format='yolo', label_fields=['category_ids']),)
            

            for final_extra_image in output_extra_images:


                transformed = transform(image=final_extra_image, bboxes=bboxes, category_ids=category_ids)
                print(transformed['bboxes'],"-----> transformed boxes")
                # visualize(
                #     transformed['image'],
                #     transformed['bboxes'],
                #     transformed['category_ids'],
                #     category_id_to_name,
                # )
                
                destination_image_path   = base_folder+destination_dir+sub_folder+images+image_name.replace(".jpg","_{}.png".format(count_1))

                destination_image_label_path = base_folder+destination_dir+sub_folder+labels+image_name.replace(".jpg","_{}.txt".format(count_1))


                try:
                    os.mkdir(base_folder+destination_dir+sub_folder)
                except Exception as e1:
                    pass
                try:

                    os.mkdir(base_folder+destination_dir+sub_folder+images)
                except Exception as e2:
                    pass
                
                try:
                    os.mkdir(base_folder+destination_dir+sub_folder+labels)
                except Exception as e3:
                    pass
                
                result = cv2.imwrite(destination_image_path,cv2.cvtColor(transformed["image"], cv2.COLOR_BGR2RGB))
                print("written ",destination_image_path," ",result)

                with open(destination_image_label_path,"w") as fl2:
                    fl2.write("\n".join([ " ".join([str(0)]+[str(jkl) for jkl in list(just_bbox)]) for just_bbox in  transformed["bboxes"]]))
                count_1+=1
            