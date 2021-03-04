import cv2
import numpy as np
from matplotlib import pyplot as plt


def showImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)
    return img


def main():
    Img = cv2.imread("imgs/tobi.jpg")
    altura, largura, canais_de_cor = Img.shape
    print("Dimensões da Imagem: " + str(largura) + "x" + str(altura))
    print("Canais de cor: " + str(canais_de_cor))

    for y in range(0, altura):
        for x in range(0, largura):
            #azul, verde, vermelho = Img[y][x]
            #print(f"[{y},{x}] = {Img[y][x]}")

            azul, verde, vermelho = getColor(Img, x, y)
            Img = setColor(Img, x, y, 0, verde, vermelho)

    Img_corte = Img[150 : 300, 100 : 200]
    Img[150 : 300, 205 : 305] = Img_corte
    showImg(Img)
    #showImg(Img)
    #cv2.imwrite("Tobi_modificado.png", Img)

main()