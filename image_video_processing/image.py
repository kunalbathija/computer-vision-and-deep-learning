import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('yolo.jpg',cv2.IMREAD_GRAYSCALE) #converts image to grayscale (0)
#IMREAD_COLOR 1
#IMREAD_UNCHANGED -1

#bgr to grayscale by opencv
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('D:\yolo\image processing\grey_yolo.png', img)

'''#bgr to grayscale by matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([50,100], [80,100],'c', linewidth = 5)
plt.show()'''
