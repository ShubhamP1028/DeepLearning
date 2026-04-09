import cv2
import numpy as np
import random
img = cv2.imread('media/shubhampreview.png',-1)
# shows multi-dimensional array from numpy that is base of openCV
# print(type(img))
# creates a random image of size 400 x 400
# random_imag = np.random.randint(0,255,(400,400,3))
imag = np.zeros((400, 400, 3), dtype=np.uint8)

for i in range(400):
    for j in range(400):
        imag[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('random Image',imag)
cv2.waitKey(0)
cv2.destroyAllWindows()






