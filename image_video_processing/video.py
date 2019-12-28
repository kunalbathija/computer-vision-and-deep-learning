import cv2
import numpy as np
import matplotlib.pyplot as plt

vid = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts frames to gray

    output.write(frame)
    cv2.imshow('colour',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
output.release()
cv2.destroyAllWindows()
