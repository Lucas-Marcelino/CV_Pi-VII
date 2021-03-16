import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'tobi.jpg'

def Harris(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

def Shi_Tomasi(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)

    plt.imshow(img),plt.show() 

def SIFT(filename):
    img = cv2.imread(filename)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT()
    kp = sift.detect(gray,None)

    img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('dst',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

def surf(filename):
    img = cv2.imread(filename,0)
    surf = cv2.SURF(400)
    kp, des = surf.detectAndCompute(img,None)
    img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
    plt.imshow(img2),plt.show()

def fast(filename):
    img = cv2.imread(filename,0)

    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector()

    # find and draw the keypoints
    kp = fast.detect(img,None)
    img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))

    # Print all default params
    print ("Threshold: ", fast.getInt('threshold'))
    print ("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
    print ("neighborhood: ", fast.getInt('type'))
    print ("Total Keypoints with nonmaxSuppression: ", len(kp))

    cv2.imshow('fast_true',img2)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

    # Disable nonmaxSuppression
    fast.setBool('nonmaxSuppression',0)
    kp = fast.detect(img,None)

    print ("Total Keypoints without nonmaxSuppression: ", len(kp))

    img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))
    
    cv2.imshow('fast_false',img3)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

def BRIEF_det(filename):
    img = cv2.imread(filename,0)

    # Initiate STAR detector
    star = cv2.FeatureDetector_create("STAR")

    # Initiate BRIEF extractor
    brief = cv2.DescriptorExtractor_create("BRIEF")

    # find the keypoints with STAR
    kp = star.detect(img,None)

    # compute the descriptors with BRIEF
    kp, des = brief.compute(img, kp)

    img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))
    cv2.imshow('BRIEF_CenSurE',img2)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

#Harris(filename)
#Shi_Tomasi(filename)
#SIFT(filename)
#surf(filename)
#fast(filename)
#BRIEF_det(filename)