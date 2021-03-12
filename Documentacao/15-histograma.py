import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('tobi.jpg',0)
# cv2.imshow("a", img)

frame = cv2.imread('banana.jpg')
frame1 = cv2.imread('tobi.jpg')

kernel = np.ones((5,5),np.uint8)

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

hsv = cv2.medianBlur(hsv,7)
hsv1 = cv2.medianBlur(hsv1,7)

# define range of yellow color in HSV
lower_yellow = np.array([25,50,50])
upper_yellow = np.array([32,255,255])

# Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask1 = cv2.inRange(hsv1, lower_yellow, upper_yellow)

img = cv2.dilate(mask,kernel,iterations = 1)
img1 = cv2.dilate(mask1,kernel,iterations = 1)

cv2.imshow("nanana", img)
cv2.imshow("tobi", img1)
plt.hist(img.ravel(),256,[150,256])
plt.hist(img1.ravel(),256,[150,256]); plt.show()

