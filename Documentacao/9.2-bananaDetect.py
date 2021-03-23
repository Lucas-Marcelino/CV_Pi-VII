import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread('banana3.jpg')
frame = img
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv = cv2.medianBlur(hsv,7)

kernel = np.ones((5,5),np.uint8)

cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')


    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        upper_yellow = np.uint8([[[b, g, r]]]) 
        upper_yellow = cv2.cvtColor(upper_yellow, cv2.COLOR_BGR2HSV).ravel()
        lower_yellow = np.array([25,50,50])
        
        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        mask = cv2.dilate(mask,kernel,iterations = 1)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)

        img = res
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,f'R:{r}, G:{g}, B:{b}',(20,4000), font, 2,(255,255,255),2,cv2.LINE_AA)

cv2.destroyAllWindows()