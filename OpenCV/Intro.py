import cv2
img = cv2.imread('media/shubhampreview.png',0)

'''
-1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image
0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
1,cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel 
'''
img= cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img= cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('Image',img)
# cv2.imwrite('media/createdpreview.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

