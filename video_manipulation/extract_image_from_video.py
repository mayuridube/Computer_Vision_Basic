import cv2
import os

cam = cv2.VideoCapture("video path")

try:
  if not os.path.exists("data"):
    os.makedirs("data")
except:
  print("error in making directory")
  
currentframe = 0
while True:
  ret,frame = cam.read()
  if ret:
    name = './data/frame'+str(currentframe)+'.jpg'
    print('Creating...' +name)
    cv2.imwrite(name,frame)
    currentframe +=1
  else:
    break

cv2.destroyAllWindows()
