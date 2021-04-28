import cv2
import numpy as np

width = 0
height = 0

def TestaInterseccao(y, CoordenadaYLinha):
    DiferencaAbsoluta = abs(y - CoordenadaYLinha)	

    if (DiferencaAbsoluta <= 7):
        return True
    else:
        return False

def Videotracking(frame, hsv, tictoc, contador, verde = True):
    tictoc.setTic()

    height = np.size(frame,0)
    width = np.size(frame,1)
    
    #transforma a imagem de RGB para HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #definir os intervalos de cores que vão aparecer na imagem final
    lowerColor = hsv.getMin()
    upperColor = hsv.getMax()
    
    #marcador pra saber se o pixel pertence ao intervalo ou não
    mask = cv2.inRange(hsvImage, lowerColor, upperColor)
    
    #aplica máscara que "deixa passar" pixels pertencentes ao intervalo, como filtro
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    #aplica limiarização
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    #encontra pontos que circundam regiões conexas (contour)
    contours, _ = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
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
        CoordenadaXCentroContorno = round((xRect+xRect+wRect)/2)
        CoordenadaYCentroContorno = round((yRect+yRect+hRect)/2)
        PontoCentralContorno = (CoordenadaXCentroContorno,CoordenadaYCentroContorno)

        #desenha linhas de referencia 
        CoordenadaYLinha = round(height / 2)
        cv2.line(frame, (0,CoordenadaYLinha), (width,CoordenadaYLinha), (0, 0, 0), 3)

        
        #desenha caixa envolvente com espessura 3
        if verde:
            cv2.rectangle(frame, (xRect, yRect), (xRect + wRect, yRect + hRect), (140, 230, 140), 2)
            cv2.circle(frame, PontoCentralContorno, 1, (140, 230, 140), 5)

            if (TestaInterseccao(CoordenadaYCentroContorno,CoordenadaYLinha)):
                if tictoc.canScore(): 
                    contador.addCount()
                    tictoc.setToc()

        else:
            cv2.rectangle(frame, (xRect, yRect), (xRect + wRect, yRect + hRect), (0, 255, 255), 2)
            cv2.circle(frame, PontoCentralContorno, 1, (0, 255, 255), 5)

            if (TestaInterseccao(CoordenadaYCentroContorno,CoordenadaYLinha)):
                if tictoc.canScore():
                    contador.addCount()
                    tictoc.setToc()
    
    return frame, gray, contador