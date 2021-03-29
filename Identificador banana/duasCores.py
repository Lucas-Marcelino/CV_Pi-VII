import cv2
import numpy as np

ESC_KEY = 27

cap = cv2.VideoCapture(0)

def Videotracking(frame, hue, sat, val, verde = True):
    
    #transforma a imagem de RGB para HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #definir os intervalos de cores que vão aparecer na imagem final
    lowerColor = np.array([hue['min'], sat["min"], val["min"]])
    upperColor = np.array([hue['max'], sat["max"], val["max"]])
    
    #marcador pra saber se o pixel pertence ao intervalo ou não
    mask = cv2.inRange(hsvImage, lowerColor, upperColor)
    
    #aplica máscara que "deixa passar" pixels pertencentes ao intervalo, como filtro
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    #aplica limiarização
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    #encontra pontos que circundam regiões conexas (contour)
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    #se existir contornos    
    if contours:
        #retornando a área do primeiro grupo de pixels brancos
        maxArea = cv2.contourArea(contours[0])
        contourMaxAreaId = 0
        i = 0
        
        #para cada grupo de pixels branco
        for cnt in contours:
            #procura o grupo com a maior área
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                contourMaxAreaId = i
            i += 1
            
        #achei o contorno com maior área em pixels
        cntMaxArea = contours[contourMaxAreaId]
        
        #retorna um retângulo que envolve o contorno em questão
        xRect, yRect, wRect, hRect = cv2.boundingRect(cntMaxArea)
        
        #desenha caixa envolvente com espessura 3
        if verde:
            cv2.rectangle(frame, (xRect, yRect), (xRect + wRect, yRect + hRect), (140, 230, 140), 2)
        else:
            cv2.rectangle(frame, (xRect, yRect), (xRect + wRect, yRect + hRect), (0, 255, 255), 2)
    
    return frame, gray

hue_verde = {'min':30, 'max':100}
sat_verde = {'min':70, 'max':190}
val_verde = {'min':80, 'max':165}

hue_amarelo = {'min':15, 'max':50}
sat_amarelo = {'min':150, 'max':210}
val_amarelo = {'min':145, 'max':230}


while True:
    success, frame = cap.read()
    
    frame, gray_verde = Videotracking(frame, hue_verde, sat_verde, val_verde)
    frame, gray_amarelo = Videotracking(frame, hue_amarelo, sat_amarelo, val_amarelo, verde=False)
    
    cv2.imshow("mascara", gray_verde)
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or 0xFF == ESC_KEY:
        break
        
cap.release()
cv2.destroyAllWindows()
