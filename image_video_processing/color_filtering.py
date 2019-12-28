import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while(1):
    _, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_colour = np.array([30,150,0])
    upper_colour = np.array([180,255,255])
    
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
