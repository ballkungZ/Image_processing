import cv2 as cv
import numpy as np

#Remove Noise
img = cv.imread('salt&Pepper_Noise/Output of SP.jpg',cv.IMREAD_GRAYSCALE)

output = cv.fastNlMeansDenoising(img,None,h=100)

cv.imwrite('Output_RM_Noise.jpg',output)