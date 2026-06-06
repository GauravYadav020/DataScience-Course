# M22 Lesson 5 – Face Detection using OpenCV
# Short Description: Implement face and eye detection using Haar cascades in OpenCV.

# Activity 1
# Goal: Load Haar cascade classifiers and detect faces in a static image.
# Summary: Draw rectangles around detected faces using cv2.detectMultiScale().
pixel values where the face is located

face = face_cascade.detectMultiScale(gray_img, 1.3, 5)
print(face) # prints coordinates where the face exist

[[208  73 161 161]]

Draw a rectangle on the detected face

for(x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3) # green color rectangle with thickness of 3

    cv2_imshow(img)