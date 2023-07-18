import numpy as np
import cv2

img = cv2.imread("Class#1/01.jpg")

blur_length = 100
angle = 45

angle_rad = np.deg2rad(angle)


kernel_size = int(blur_length)


kernel = np.zeros((kernel_size, kernel_size))

center = kernel_size // 2

for i in range(kernel_size):
    offset = int(round((i - center) * np.tan(angle_rad)))
    kernel[center + offset, i] = 1

kernel /= np.sum(kernel)

blurred_img = cv2.filter2D(img, -1, kernel)

cv2.imwrite("input.jpg",img)
cv2.imwrite("Output.jpg",blurred_img)
cv2.imshow("Original Image", img)
cv2.imshow("Motion Blurred Image", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()