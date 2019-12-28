import cv2
import numpy as np

img = cv2.imread('yolo.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converts to gray
retval, threshold1 = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) #normal threshold
retval, threshold2 = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY) #normal threshold on gray image
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) #adaptive thresholding

cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)
cv2.imshow('threshold1',threshold1)
cv2.imshow('threshold2',threshold2)

cv2.waitKey(0)
cv2.destroyAllWindows()
