import cv2
import numpy as np

#img = np.ones((512,512,1), np.uint8)
height, width,channel = img.shape
print (width)
img[:,0:512//2] = (255,0,0)


cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows
