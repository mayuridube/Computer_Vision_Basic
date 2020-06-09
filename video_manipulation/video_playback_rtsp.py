import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"

rtsp_link = "rtsp://port:ip/"
cap = cv2.VideoCapture(rtsp_link)
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
    else:
        print("Failed to get frame")

    # press q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
