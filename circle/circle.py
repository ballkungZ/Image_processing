import numpy as np
import cv2

image = np.zeros((400, 400, 3 ), dtype=np.uint8)
position_c1 = (200, 200)
position_c2 = (200, 200)
position_c3 = (200, 200)
size_c1 = 40
size_c2 = 60
size_c3 = 80
color_c1 = (255, 255, 0)
color_c2 = (0, 255, 255)
color_c3 = (0, 255, 0)
thickness = -1
thick = 2
thick2 = 4

cv2.circle(image, position_c1, size_c1, color_c1, thickness)
cv2.circle(image, position_c2, size_c2, color_c2, thick)
cv2.circle(image, position_c3, size_c3, color_c3, thick2)


cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
