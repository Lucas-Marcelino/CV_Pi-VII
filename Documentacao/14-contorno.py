import cv2
import numpy as np

img = cv2.imread('tobi.jpg',0)
cv2.imshow('img-cinza', img)
cv2.waitKey(0)
img1 = cv2.imread('banana.jpg',0)
cv2.imshow('img-banana', img1)
cv2.waitKey(0)


ret,thresh = cv2.threshold(img1,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    img1 = cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),6)
cnt = contours[0]
cv2.imshow('img-quadrado grande', img1)
cv2.waitKey(0)

x,y,w,h = cv2.boundingRect(cnt)
img1 = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),6)

cv2.imshow('img-quadrado grande', img1)
cv2.waitKey(0)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
imgC = cv2.drawContours(img,[box],0,(0,0,255),6)

cv2.imshow('img-certinho', imgC)
cv2.waitKey(0)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),6)

cv2.imshow('img-circulo', img)
cv2.waitKey(0)
cv2 . destroyAllWindows ()
