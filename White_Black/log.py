import cv2 as cv
import numpy as np

img_light = cv.imread('IMG_0572.jpg',cv.IMREAD_GRAYSCALE)
img_dark = cv.imread('IMG_1704.jpg',cv.IMREAD_GRAYSCALE)

#ทำให้ภาพมืด
img_out_to_drak = (img_light / 255)**2
img_out_to_drak = img_out_to_drak * 255

#ทำให้ภาพสว่าง
img_out_to_light = np.log(img_dark)
img_max = np.max(img_out_to_light)
img_out_to_light = img_out_to_light * (255 / img_max)

img_out_to_light = np.array(img_out_to_light, dtype = np.uint8)
img_out_to_drak = np.array(img_out_to_drak, dtype = np.uint8)

cv.imwrite('Pic_input_drak.jpg',img_dark)
cv.imwrite('Pic_output_drak.jpg',img_out_to_light)
cv.imwrite('Pic_input_light.jpg',img_light)
cv.imwrite('Pic_output_light.jpg',img_out_to_drak)
