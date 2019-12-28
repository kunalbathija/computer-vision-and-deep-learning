import numpy as np
import cv2
import matplotlib.pyplot as plt

template = cv2.imread('template.jpg',0)
image = cv2.imread('image.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(template,None)
kp2, des2 = orb.detectAndCompute(image,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(template,kp1,image,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()
