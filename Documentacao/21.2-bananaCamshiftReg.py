import cv2
import numpy as np

def nothing(x):
    pass

def select_color(name):

    # Create a black image, a window
    img = np.zeros((300,712,3), np.uint8)
    cv2.namedWindow(name)

    # create trackbars for color change
    cv2.createTrackbar('R',name,0,255,nothing)
    cv2.createTrackbar('G',name,0,255,nothing)
    cv2.createTrackbar('B',name,0,255,nothing)

    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, name,0,1,nothing)

    while(1):
        cv2.imshow(name,img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R',name)
        g = cv2.getTrackbarPos('G',name)
        b = cv2.getTrackbarPos('B',name)
        s = cv2.getTrackbarPos(switch,name)

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,f'R:{r}, G:{g}, B:{b}',(20,275), font, 2,(255,255,255),2,cv2.LINE_AA)
            #print([b,g,r])
    cv2.destroyAllWindows()
    return np.uint8([[[b, g, r]]]) 

def teste_cores(filename, lower_yellow, upper_yellow):
    frame = cv2.imread(filename)

    kernel = np.ones((5,5),np.uint8)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv = cv2.medianBlur(hsv,7)


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

def cores_dnv():
    resp = input('Ficou bom? [S/N]')
    return True if resp == 'S' else False

def video_banana(filename, lower, upper):
    cap = cv2.VideoCapture(filename)

    # take first frame of the video
    ret,frame = cap.read()

    # setup initial location of window
    r,h,c,w = 250,90,400,125  # simply hardcoded the values
    track_window = (c,r,w,h)

    # set up the ROI for tracking
    roi = frame[r:r+h, c:c+w]
    hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, lower, upper)
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
            #print(pts)
            #print('\n')
            img2 = cv2.polylines(frame,[pts],True, 255,5)
            cv2.imshow('img2',img2)

            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break
            else:
                pass
                #cv2.imwrite(chr(k)+".jpg",img2)

        else:
            break

    cv2.destroyAllWindows()
    cap.release()

def escolher_arquivo():
    img1 = 'banana1.jpg'
    img2 = 'banana2.jpg'
    img3 = 'bananaSem.jpg'
    print(f"""Escolha um dos arquivos pelo Numero:
1 - {img1}
2 - {img2}
3 - {img3}
    """)
    resposta = int(input())
    if resposta == 1:
        resp = img1
    elif resposta == 2:
        resp = img2
    else:
        resp = img3
    print(f'Vc escolheu o arquivo {resp}')
    return resp

def testando():
    lower_yellow = select_color('lower_yellow')
    lower_yellow = cv2.cvtColor(lower_yellow, cv2.COLOR_BGR2HSV).ravel()
    upper_yellow = select_color('upper_yellow')
    upper_yellow = cv2.cvtColor(upper_yellow, cv2.COLOR_BGR2HSV).ravel()
    filename = escolher_arquivo()
    teste_cores(filename, lower_yellow, upper_yellow)

    return filename, lower_yellow, upper_yellow

def passarVideos(lower_yellow, upper_yellow):
    filename = 'bananaSem.mp4'
    video_banana(filename, lower_yellow, upper_yellow)
    filename = 'banana1.mp4'
    video_banana(filename, lower_yellow, upper_yellow)
    filename = 'banana2.mp4'
    video_banana(filename, lower_yellow, upper_yellow)

def main():
    filename, lower_yellow, upper_yellow = testando()
    resp = cores_dnv()
    while not resp:
        filename, lower_yellow, upper_yellow = testando()
        resp = cores_dnv()
    passarVideos(lower_yellow, upper_yellow)

main()