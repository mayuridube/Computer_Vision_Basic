# usage
# press 's' to save image and 'q' to discard

import numpy as np
import cv2
# read image
img = cv2.imread('../test_images/index.jpeg')


# display image
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
# wait for 's' key to save and exit.
elif k == ord('s'):
    # image write
    cv2.imwrite('store_image.jpg', img)
    print("Image write successfully")
    cv2.destroyAllWindows()
