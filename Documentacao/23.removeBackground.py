import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

def MOG(cap):
    fgbg = cv2.createBackgroundSubtractorMOG()

    while(1):
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)

        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        cap.release()
        cv2.destroyAllWindows()

def MOG2(cap):
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while(1):
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)

        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def GMG(cap): 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    fgbg = cv2.createBackgroundSubtractorGMG()

    while(1):
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()



MOG(cap)
MOG2(cap)
GMG(cap)
