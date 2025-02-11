import numpy as np
import cv2

def det_banana(filename):
    cap = cv2.VideoCapture(filename)

    # take first frame of the video
    ret,frame = cap.read()
    cv2.imwrite(filename+".jpg",frame)

    # setup initial location of window
    r,h,c,w = 250,90,400,125  # simply hardcoded the values
    track_window = (c,r,w,h)

    # set up the ROI for tracking
    roi = frame[r:r+h, c:c+w]
    hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0., 50.,50.)), np.array((32.,255.,255.)))
    roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
    term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

    while(1):
        ret ,frame = cap.read()

        if ret == True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

            # apply meanshift to get the new location
            ret, track_window = cv2.CamShift(dst, track_window, term_crit)

            # Draw it on image
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            print(pts)
            print('\n')
            img2 = cv2.polylines(frame,[pts],True, 255,5)
            cv2.imshow('img2',img2)

            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break
            else:
                cv2.imwrite(chr(k)+".jpg",img2)

        else:
            break

    cv2.destroyAllWindows()
    cap.release()

# filename = 'bananaSem.mp4'
# det_banana(filename)

# filename = 'banana1.mp4'
# det_banana(filename)

# filename = 'banana2.mp4'
# det_banana(filename)

filename = 'banana3.mp4'
det_banana(filename)