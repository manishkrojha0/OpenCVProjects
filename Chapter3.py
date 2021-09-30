import cv2
import numpy as np
#######  this chapter is all about image size and dimensions and numpy###
img = cv2.imread("Resources/manish.jpeg")
## image show
print(img.shape)
## resize of image
imgResize = cv2.resize(img,(300,200)) ##  width first and then the height
## crop image
imgCropped = img[0:500, 200:500]     ## heigth first and then the width
cv2.imshow("image",img)
cv2.imshow("Resize image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)