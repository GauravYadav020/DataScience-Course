# M22 Lesson 3 – Color Detection using OpenCV
# Short Description: Detect specific colors in images/videos using HSV color space and masking.

# Activity 1
# Goal: Convert BGR image to HSV and create a mask for a specific color range.
# Summary: Detect a single color (e.g., red or blue) using lower and upper bounds.
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# reading image
img = cv2.imread("shapes.png")
cv2_imshow(img)

# converting BGR image to HSV image
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow(hsv_img)

# specifying range of blue color
lower_blue = np.array([65, 0, 0])
upper_blue = np.array([110, 255, 255])

# creating mask for only blue color
mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
cv2.imshow(mask)

# returning result (mask) in blue color except the black one
result = cv2.bitwise_and(img, img, mask = mask)
cv2_imshow(result)