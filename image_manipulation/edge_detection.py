#import the required libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# read the image
image = cv2.imread('../test_images/car.png')

# calculate the edges using Canny edge algorithm
edges = cv2.Canny(image, 100, 200)

# plot the edges
plt.imshow(edges)
cv2.imwrite("../output_images/edge_detection_op.jpg",edges)

plt.show()
