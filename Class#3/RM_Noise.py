import cv2 as cv
import numpy as np

#Remove Noise
img = cv.imread('Class#3/Output of SP.jpg',cv.IMREAD_GRAYSCALE)

output = cv.medianBlur(img,7)

cv.imwrite('Output_RM_Noise.jpg',output)