import cv2
import numpy as np

img = cv2.imread('banana.jpg',0)
cv2.imshow('img-cinza', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),6)

cv2.imshow('img-contornos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


frame = cv2.imread('banana.jpg')
kernel = np.ones((5,5),np.uint8)

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
hsv = cv2.medianBlur(hsv,7)

# define range of yellow color in HSV
lower_yellow = np.array([25,50,50])
upper_yellow = np.array([32,255,255])

# Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask = cv2.dilate(mask,kernel,iterations = 1)

ret,thresh = cv2.threshold(mask,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),6)

cv2.imshow('img-contornos', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()