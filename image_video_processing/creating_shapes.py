import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('yolo.jpg',cv2.IMREAD_COLOR) 

cv2.line (img, (0,0), (150,150), (255,0,0), 15)
cv2.rectangle (img, (40,40), (150,150), (255,255,0), 15)
cv2.circle(img, (100,63), 55, (0,0,255), 1)

vertices = np.array([[10,5],[20,30],[80,70],[90,60]], np.int32)
#vertices = vertices.reshape((-1,1,2))
cv2.polylines(img, [vertices], True, (0,255,234),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'yolo!', (0,130), font, 1, (14,98,56), 5, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


