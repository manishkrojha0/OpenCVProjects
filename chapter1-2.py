import cv2
import numpy as np
print("package Imported")
# ##########image reading###########
# img = cv2.imread("Resources/sudoko.jpg")
# cv2.imshow("output",img)
# cv2.waitKey(0)
########## video view#############
# cap = cv2.videoCapture("Resources/production ID 4291570.mp4")
# cap = cv2.VideoCapture("Resources/production ID 4291570.mp4")
# while True:
#     success, img =cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

##### webcam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
# while True:
#     success, img =cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

#####    basics functions  ####

img = cv2.imread("Resources/manish.jpeg")
kernel = np.ones((5,5),np.uint8)
## convert img to gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 ##convert into blurred
imgBlur = cv2.GaussianBlur(img,(7,7),0)
  ### convert into canny
imgCanny = cv2.Canny(img,300,300)
## image Dialation
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.waitKey(0)

