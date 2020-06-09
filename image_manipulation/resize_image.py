import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading the image
image = cv2.imread("../test_images/apple.jpeg", 1)

width = 1100
height = 1000
dim = (width, height)

# normal resize
normal = cv2.resize(image, dim)

# interpolation is additional flag
# having values
# cv2.INTER_AREA: This is used when we need need to shrink an image.
shrink_image = cv2.resize(image, (490, 540), interpolation=cv2.INTER_AREA)

# cv2.INTER_CUBIC: This is slow but more efficient.

# cv2.INTER_LINEAR: This is primarily used when zooming is required.
# This is the default interpolation technique in OpenCV.
linear = cv2.resize(image, (650, 540), interpolation=cv2.INTER_LINEAR)

# cv2.INTER_NEAREST : A nearest-neighbor interpolation
stretch_near = cv2.resize(image, (780, 540), interpolation=cv2.INTER_NEAREST)


Titles = ["Original", "normal resize", "Inter Area", "Inter linear", "Interpolation Nearest"]
images = [image, normal, shrink_image, linear, stretch_near]
count = 5

# for subplot
columns = 3
rows = 2
for i in range(count):
	plt.subplot(rows, columns, i+1)
	plt.title(Titles[i])
	plt.imshow(images[i])

plt.show()
