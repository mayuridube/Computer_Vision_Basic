'''
usages:
press 's' to select ROI from video feed then press 'enter' to save it
press 'l' to draw line and 'enter to save it'
'''

import numpy as np
import argparse
import imutils
import cv2
imCrop = None
mouse_flag = 0
rectangle_flag = 0
line_flag = 0
crop_x = ""
crop_y = ""
crop_x1 = ""
crop_y1 = ""


# initialize the video stream, pointer to output video file, and
# frame dimensions
vs = cv2.VideoCapture(0)

# image read
# img = cv2.imread('./test_images/index.jpeg')


def line(event, x, y, flags, param):
    global ix, iy, vx, vy, trigger, mouse_down, mouse_flag
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img,(x,y),100,(255,0,0),-1)
        ix, iy = x, y
        # print(ix, iy)
        mouse_down = True
        mouse_flag = 0

    if event == cv2.EVENT_LBUTTONUP and mouse_down:
        vx, vy = x, y
        mouse_down = False
        print(f"line coordinates are:")
        print(f"x:{ix}")
        print(f"y:{iy}")
        print(f"x1:{vx}")
        print(f"y1:{vy}")
        mouse_flag = 2


while True:
    # read the next frame from the file
    (grabbed, frame) = vs.read()

    frame = imutils.resize(frame, width=800)
    # draw roi on first frame only
    # if imCrop is None:
    k = cv2.waitKey(1)
    if k == ord('s'):  # wait for s
        r = cv2.selectROI(frame)
        # print(r)
        imCrop = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        crop_x = int(r[0])
        crop_y = int(r[1])
        crop_x1 = int(r[0] + r[2])
        crop_y1 = int(r[1] + r[3])
        print(f"rectangle coordinates are:")
        print(f"top_x:{crop_x}")
        print(f"top_y:{crop_y}")
        print(f"bottom_x:{crop_x1}")
        print(f"bottom_y:{crop_y1}")
        rectangle_flag = 1
        cv2.destroyAllWindows()

    if k == ord('l'):
        cv2.setMouseCallback('frame', line)
        line_flag = 1
    if k == ord("q"):
        break

    if rectangle_flag == 1:
        cv2.rectangle(frame, (crop_x, crop_y), (crop_x1, crop_y1), (0, 255, 0), 3)
        
    if mouse_flag == 2:
        cv2.line(frame, (ix, iy), (vx, vy), (255, 0, 0), 5)

    cv2.putText(frame, "press 's' to select ROI from video feed",(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(frame,"then press 'enter' to save it",(20,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(frame, "press 'l' to draw line and 'enter to save it",(20,120),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vs.release()
cv2.destroyAllWindows()
