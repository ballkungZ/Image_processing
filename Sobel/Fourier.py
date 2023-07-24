import numpy as np
import cv2 as cv

filter_h = 3
filter_w = 3
filter = np.zeros([filter_h,filter_w],dtype = np.float32)
filter[0,0] = 1;    filter[0,1] = 0;    filter[0,2] = -1;
filter[1,0] = 2;    filter[1,1] = 0;    filter[1,2] = -2;
filter[2,0] = 1;    filter[2,1] = 0;    filter[2,2] = -1;

img = cv.imread('Sobel/sobel_y.png',cv.IMREAD_GRAYSCALE)

img = img.astype(np.float32)

imgF = np.fft.fft2(filter)

imgF = np.fft.fftshift(imgF)

imgReal = np.real(imgF)
imgIma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imgIma**2)
imgPhs = np.arctan2(imgIma,imgReal)



imgMag = np.log(1+imgMag)
imgMag = cv.normalize(imgMag,None,0,255,cv.NORM_MINMAX,cv.CV_8U)


cv.imwrite('output_Fourier_sobel_y.png',imgMag)