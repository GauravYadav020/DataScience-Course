# M22 Lesson 1 – Getting started with OpenCV
# Short Description: Introduction to OpenCV library, installation, and basic image loading and display.

# Activity 1
# Goal: Install OpenCV and load an image using cv2.imread()
# Summary: Students will write code to read and display their first image using OpenCV.
# read the image
image = cv2.imread("color.jpg")
# displaying image
cv2.imshow(image)
# print dimensions of the image
# 3 indicates - 3 channels of image - rgb
print(image.shape)

# converting color image to grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow(gray_image)

print(gray_image.shape)

# converting colored to HSV (Hue Saturation and Variance) image
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow(hsv_image)
print(hsv_image.shape)

# canny image is edge detected image
# it takes gray image as an argument
canny_image = cv2.Canny(gray_image, 150, 200) # 150 and 200 are the size of filter
# cv2.imshow(canny_image)

# Erosion (use to reduce noise of the image)
kernel = np.ones((1, 1), np.uint8) # small window or matrix
erode_image = cv2.erode(canny_image, kernel, iterations = 1)
# cv2.imshow(erode_image)

# Dilation
kernel1 = np.ones((5, 5), np.uint8)
dilate_image = cv2.dilate(canny_image, kernel1, iterations=1)
# cv2_imshow(dilate_image)

# displaying all three images in one row
hori_display = np.concatenate((canny_image, erode_image, dilate_image), axis=1)
cv2_imshow(hori_display)

# reading noisy image
image = cv2.imread("lion.jpg")
# cv2_imshow(image)

# denoising image
denoise_image = cv2.fastNlMeansDenoisingColored(image, None, 20, 20, 7, 15)
# cv2_imshow(denoise_image)

hori_display = np.concatenate((image, denoise_image), axis=1)
cv2_imshow(hori_display)