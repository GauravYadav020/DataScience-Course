# M22 Lesson 4 – Shape Detection using OpenCV
# Short Description: Detect and identify basic shapes in images using contour detection.

# Activity 1
# Goal: Find contours in a binary image using cv2.findContours().
# Summary: Understand contour hierarchy and approximation methods.

for cnt in contours:
    # function able to identify the points to define our shape.
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    n = len(approx)
    if n==6:
        # this is a hexagon
        print("We have a hexagon here")
        cv2.drawContours(img,[cnt],0,255,10)  # this is for boundary of shape
    elif n==3:
        # this is a triangle
        print("We found a triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),3)
    elif n>9:
        # this is a circle
        print("We found a circle")
        cv2.drawContours(img,[cnt],0,(0,255,255),3)
    elif n==4:
        # this is a Square
        print("We found a square")
        cv2.drawContours(img,[cnt],0,(255,255,0),3)
cv2.imshow(img)