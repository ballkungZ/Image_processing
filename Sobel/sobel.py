import numpy as np
import cv2 as cv
img = cv.imread('Sobel/01.jpg',cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img,cv.CV_64F)
sobel_x = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobel_y = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

print('[input] type',img.dtype)
print('[Laplacian] type',laplacian.dtype)
print('[Sobel_X] type',sobel_x.dtype)
print('[Sobel_Y] type',sobel_y.dtype)

filter_h = 3
filter_w = 3
filter = np.zeros([filter_h,filter_w],dtype = np.float32)
filter[0,0] = 1;    filter[0,1] = 0;    filter[0,2] = -1;
filter[1,0] = 2;    filter[1,1] = 0;    filter[1,2] = -2;
filter[2,0] = 1;    filter[2,1] = 0;    filter[2,2] = -1;


laplacian = cv.normalize(laplacian,None,0,255,cv.NORM_MINMAX,cv.CV_8U)
sobel_x = cv.normalize(sobel_x,None,0,255,cv.NORM_MINMAX,cv.CV_8U)
sobel_y = cv.normalize(sobel_y,None,0,255,cv.NORM_MINMAX,cv.CV_8U)
cv.imwrite('laplacian.png',laplacian)
cv.imwrite('sobel_x.png',sobel_x)
cv.imwrite('sobel_y.png',sobel_y)
cv.imwrite('Filter_sobel.png',filter)
