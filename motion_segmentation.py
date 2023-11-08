def motion_detector():
  counter = 0
  import cv2
  import numpy as np
#   from matplotlib import pyplot as plt
  # cap = cv2.VideoCapture('20230311161615-1.mp4')
  # cap = cv2.VideoCapture('20230305095312.mp4')
#   cap = cv2.VideoCapture('20230204141640.mp4')
  name = "output_003"
  cap = cv2.VideoCapture("{}.mp4".format(name))
  print(cap.get(cv2. CAP_PROP_FPS))
  #writer = cv2.VideoWriter("output_test.mp4",cv2.VideoWriter_fourcc(*"mp4v"),cap.get(cv2. CAP_PROP_FPS),(1080, 1920))

  num_ = 1
  frame_count = 0
  previous_frame = None
  print(cap.isOpened())
  cummulutative_list = []
  countours_images = []
  delta_b = None
  while 1:
    # cummulutative_list = []
    print(cap.isOpened())
    frame_count += 1

    # 1. Load image; convert to RGB
    ret,img_brg = cap.read()
    print(ret)
    write_ = False
    
    if not ret:
        c1= 0 
        for image_ in countours_images:
          # cv2.imwrite("test/late_evening_fire_test_trail__gray_image_image_{}_part_{}.png".format(counter,c1), cv2.cvtColor(src=image_, code=cv2.COLOR_BGR2RGB))
        # write_ = True
          c1+=1
        break
    img_rgb = cv2.cvtColor(src=img_brg, code=cv2.COLOR_BGR2RGB)
    img_rgb = cv2.resize(img_rgb,(640,480))

    if ((frame_count % 2) == 0):
        pass

      # 2. Prepare image; grayscale and blur
    prepared_frame = img_rgb.copy()
    # prepared_frame[prepared_frame<200]=0
    # prepared_frame[prepared_frame>200]=255
    # hsv = cv2.cvtColor(prepared_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(prepared_frame, (100,100,100), (255,255,255))
    prepared_frame = cv2.bitwise_and(prepared_frame, prepared_frame, mask = mask)

    prepared_frame = cv2.cvtColor(prepared_frame, cv2.COLOR_BGR2GRAY)
    
    # prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5,5), sigmaX=0)
   # 3. Set previous frame and continue if there is None
    if (previous_frame is None):
    # First frame; there is no previous one yet
        previous_frame = prepared_frame
        # continue
    if counter==1:
        delta_b =  cv2.subtract(src1=previous_frame, src2=prepared_frame)
        # mask_1 = cv2.inRange(delta_b, 0, 255)
        # delta_b = cv2.bitwise_and(delta_b, delta_b, mask = mask_1)
        print(delta_b.dtype)
        # delta_b[delta_b<0]=0
        print(delta_b.dtype)
        cv2.imwrite("test/delta.png",delta_b)
        # calculate difference and update previous frame
    diff_frame_1 = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
    cummulutative_list.append(diff_frame_1)
    previous_frame = prepared_frame.copy()
    result_img  = np.zeros(prepared_frame.shape)
    print(len(cummulutative_list))
    if counter>num_:
      if 1:

        for frame_diff in cummulutative_list:
            result_img +=frame_diff
        if counter>0:
          result_img  += delta_b
      result_img =  result_img.astype(np.uint8)
      print(result_img.dtype)
      # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
      kernel = np.ones((3, 3))
      diff_frame = cv2.erode(result_img, kernel, 3)

      # 5. Only take different areas that are different enough (>20 / 255)
      thresh_frame = cv2.threshold(src=diff_frame, thresh=50, maxval=255, type=cv2.THRESH_BINARY)[1]
      # gray_diff_image = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY)
      gray_diff_image = diff_frame
      cv2.imwrite("test/identify_{}_{}.png".format(name,counter),diff_frame)
      _,contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(image=img_rgb, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    c=0
    print(counter)
    if counter>num_:
      
      for contour in contours:
          # mask = np.ones(gray_diff_image.shape, np.uint8)*255
          # mask = np.zeros_like(img_rgb, dtype=np.uint8)
          mask = np.zeros(img_rgb.shape[0:2], dtype="uint8")
          

          if cv2.contourArea(contour) < 50:
              # too small: skip!
              continue
          # cv2.drawContours(mask, [contour], -1, 0, -1) 
          mask = cv2.drawContours(mask, [contour] ,0, 255, -1) 
          # new_image = img_rgb.copy()
          # new_image[mask < 255] = 0 

          result = cv2.bitwise_and( img_rgb,  img_rgb, mask=mask)
          # new_image[mask < 255, :] = 0
          print(counter,c)
          if 1:
            # pass
            cv2.imwrite("test/late_evening_fire_test_trail__gray_image_image_{}_part_{}.png".format(counter,c), cv2.cvtColor(src=result, code=cv2.COLOR_BGR2RGB))
          # cv2.imwrite("late_evening_fire_test_trail__gray_image_image_{}_part_{}_mask.png".format(counter,c), mask)
          else:
            countours_images.append(result)


          c+=1
          # (x, y, w, h) = cv2.boundingRect(contour)
          # cv2.rectangle(img=img_rgb, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
      # cv2.imshow('Motion detector', img_rgb)
      # plt.imshow(img_rgb)
      # plt.show()
      # plt.pause(0.3)
      # cv2.imwrite("late_evening_fire_test_trail_{}.png".format(counter), cv2.cvtColor(src=img_rgb, code=cv2.COLOR_BGR2RGB))
      # cv2.imwrite("late_evening_fire_test_trail__gray_image_{}.png".format(counter), cv2.cvtColor(src=gray_diff_image, code=cv2.COLOR_GRAY2RGB))
      
      # writer.write(img_rgb)
    counter+=1
    if write_ :
      break
    print(img_rgb.shape)


  cap.release()
#   writer.release()

motion_detector()