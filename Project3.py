############## Number Plate Detector  ########
import cv2
import numpy as np
##################
imgHeight= 480
imgWidth = 640
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_licence_plate_rus_16stages.xml")
minArea = 200    ### minimum area of covered by plate
color = (255,0,255)
#################
cap = cv2.VideoCapture(0)
cap.set(3,imgWidth)
cap.set(4,imgHeight)
cap.set(10,150)
count=0
while True:
    success, img =cap.read()

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) ###coverting image into gray image
    numberPlates=nPlateCascade.detectMultiScale(imgGray,1.1,10)

    for (x, y, w , h ) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0 , 255),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
            # cv2.imshow("Result",img)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("Resources/Scanned?NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
        break