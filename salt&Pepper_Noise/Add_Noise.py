import cv2 as cv
import random

#Add salt&PepperNoise
img = cv.imread('salt&Pepper_Noise/01.jpg',cv.IMREAD_GRAYSCALE)

density_salt = 0.2
density_pepper = 0.2

number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

for i in range(number_of_white_pixel):
    y_coord = random.randint(0,img.shape[0] - 1)
    x_coord = random.randint(0,img.shape[1] - 1)
    img[y_coord][x_coord] = 255
                     
number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

for i in range(number_of_black_pixel):
    y_coord = random.randint(0,img.shape[0] - 1)
    x_coord = random.randint(0,img.shape[1] - 1)
    img[y_coord][x_coord] = 0

cv.imwrite('Output of SP.jpg',img)