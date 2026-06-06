# M22 Lesson 2 – Drawing using OpenCV
# Short Description: Learn to draw shapes, lines, and text on images using OpenCV functions.

# Activity 1
# Goal: Draw basic shapes like line, rectangle, and circle on a blank canvas.
# Summary: Use cv2.line(), cv2.rectangle(), cv2.circle() with different colors and thickness.

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import cv2
import matplotlib.pyplot as plt

emptyImg = np.zeros(shape=(512, 512, 3), dtype=np.int16)

plt.imshow(emptyImg)