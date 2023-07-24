import numpy as np
import cv2 as cv

img1 = cv.imread('Sobel/01.jpg')
img2 = cv.imread('Sobel/output_Fourier_sobel_x.png')


gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)


dot_product = np.dot(gray1.flatten(), gray2.flatten())


result_image = np.zeros_like(img1)
result_image[:,:,0] = dot_product / (img1.shape[0] * img1.shape[1])
result_image[:,:,1] = dot_product / (img1.shape[0] * img1.shape[1])
result_image[:,:,2] = dot_product / (img1.shape[0] * img1.shape[1])


cv.imshow('Result Image', result_image)
cv.waitKey(0)
cv.destroyAllWindows()