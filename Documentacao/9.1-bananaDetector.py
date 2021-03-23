import cv2
import numpy as np


frame = cv2.imread('banana3.jpg')

kernel = np.ones((5,5),np.uint8)

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

hsv = cv2.medianBlur(hsv,7)

# define range of yellow color in HSV
lower_yellow = np.array([0,50,50])
upper_yellow = np.array([32,255,255])

# Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

mask = cv2.dilate(mask,kernel,iterations = 1)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0) & 0xFF


cv2.destroyAllWindows()