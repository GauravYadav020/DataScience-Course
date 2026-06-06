# M22 Lesson 6 – Funny 3D Mirrors
# Short Description: Create fun visual effects like 3D mirrors and distortions using OpenCV.

# Activity 1
# Goal: Implement basic mirror effect by flipping the image.
# Summary: Create horizontal and vertical mirror effects using array slicing.
import cv2
import numpy as np
import math
from vcam import vcam,meshGen

# Create a virtual camera object. Here H,W correspond to height and width of the input image frame.
c1 = vcam(H=H,W=W)

# Create surface object
plane = meshGen(H,W)

# Change the Z coordinate. By default Z is set to 1
# We generate a mirror where for each 3D point, its Z coordinate is defined as
Z = 10*sin(2*pi[x/w]*10)
plane.Z = 10*np.sin((plane.X/plane.W)*2*np.pi*10)

# Get modified 3D points of the surface
pts3d = plane.getPlane()

# Project the 3D points and get corresponding 2D image coordinates using our virtual camera object c1
pts2d = c1.project(pts3d)