import numpy as np
import cv2


fourcc = cv2.VideoWriter_fourcc(*'XVID')
# video file name 
out = cv2.VideoWriter('./output.avi', fourcc, 20.0, (640, 480))
    
def capture():
    # '0' is for usb camera
    cap = cv2.VideoCapture(0)
    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            cv2.resize(frame, (640, 480))

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # write the frame
            out.write(frame)


            # press q to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    except:
        print("ERROR")



if __name__ == '__main__':
    capture()
