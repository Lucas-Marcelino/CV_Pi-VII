import cv2
import numpy as np
import time

ESCAPE_KEY_ASCII = 27

def onChange(value):
    print('valor alterado', value)
    pass

#videoCapture = cv2.VideoCapture('banana3.mp4')

img = cv2.imread('banana3.png')
kernel = np.ones((5,5),np.uint8)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv = cv2.medianBlur(hsv,7)

lower_anterior = np.array([0,50,50])
upper_anterior = np.array([32,255,255])

mask = cv2.inRange(hsv, lower_anterior, upper_anterior)
mask = cv2.dilate(mask,kernel,iterations = 1)
res = cv2.bitwise_and(img, img, mask= mask)


titleWindow = 'ajustando as cores'
cv2.namedWindow(titleWindow)

cv2.createTrackbar('Hue_Lower', titleWindow, 0, 360, onChange)
cv2.createTrackbar('Saturation_Lower', titleWindow, 50, 255, onChange)
cv2.createTrackbar('Value_Lower', titleWindow, 50, 255, onChange)

cv2.createTrackbar('Hue_Upper', titleWindow, 32, 360, onChange)
cv2.createTrackbar('Saturation_Upper', titleWindow, 255, 255, onChange)
cv2.createTrackbar('Value_Upper', titleWindow, 255, 255, onChange)

contar_tempo = 0

Hue_Upper_anterior = 32
atualizar_Hue_Upper = False
Saturation_Upper_anterior = 255
atualizar_Saturation_Upper = False
Value_Upper_anterior = 255
atualizar_Value_Upper = False

Hue_Lower_anterior = 0
atualizar_Hue_Lower = False
Saturation_Lower_anterior = 50
atualizar_Saturation_Lower = False
Value_Lower_anterior = 50
atualizar_Value_Lower = False

while True:

    Hue_Upper_posterior = cv2.getTrackbarPos('Hue_Upper', titleWindow)
    Saturation_Upper_posterior = cv2.getTrackbarPos('Saturation_Upper', titleWindow)
    Value_Upper_posterior = cv2.getTrackbarPos('Value_Upper', titleWindow)

    Hue_Lower_posterior = cv2.getTrackbarPos('Hue_Lower', titleWindow)
    Saturation_Lower_posterior = cv2.getTrackbarPos('Saturation_Lower', titleWindow)
    Value_Lower_posterior = cv2.getTrackbarPos('Value_Lower', titleWindow)

    if Hue_Upper_anterior != Hue_Upper_posterior:
        atualizar_Hue_Upper = True
        contar_tempo = time.time()
        Hue_Upper_anterior = Hue_Upper_posterior
    
    if Saturation_Upper_anterior != Saturation_Upper_posterior:
        atualizar_Saturation_Upper = True
        contar_tempo = time.time()
        Saturation_Upper_anterior = Saturation_Upper_posterior

    if Value_Upper_anterior != Value_Upper_posterior:
        atualizar_Value_Upper = True
        contar_tempo = time.time()
        Value_Upper_anterior = Value_Upper_posterior

    if Hue_Lower_anterior != Hue_Lower_posterior:
        atualizar_Hue_Lower = True
        contar_tempo = time.time()
        Hue_Lower_anterior = Hue_Lower_posterior
    
    if Saturation_Lower_anterior != Saturation_Lower_posterior:
        atualizar_Saturation_Lower = True
        contar_tempo = time.time()
        Saturation_Lower_anterior = Saturation_Lower_posterior

    if Value_Lower_anterior != Value_Lower_posterior:
        atualizar_Value_Lower = True
        contar_tempo = time.time()
        Value_Lower_anterior = Value_Lower_posterior


    if time.time() - contar_tempo > 1:

         if atualizar_Hue_Upper == True or atualizar_Saturation_Upper == True or atualizar_Value_Upper == True or atualizar_Hue_Lower == True or atualizar_Saturation_Lower == True or atualizar_Value_Lower == True:

            lower_anterior = np.array([Hue_Lower_anterior, Saturation_Lower_anterior, Value_Lower_anterior])
            upper_anterior = np.array([Hue_Upper_anterior, Saturation_Upper_anterior, Value_Upper_anterior])
            
            mask = cv2.inRange(hsv, lower_anterior, upper_anterior)
            mask = cv2.dilate(mask,kernel,iterations = 1)
            res = cv2.bitwise_and(img, img, mask= mask)    
            atualizar_Hue_Upper, atualizar_Saturation_Upper, atualizar_Value_Upper= False, False, False
            


    cv2.imshow(titleWindow, res)

    k = cv2.waitKey(1) &0xFF
    if k == ESCAPE_KEY_ASCII:
        break
cv2.destroyAllWindows()
print('Lower: ', lower_anterior)
print('Upper: ', upper_anterior)
