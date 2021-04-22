from timer import TicToc
from cv import Videotracking
from colors import hsv
from counter import counter
import cv2

ContadorVerde = counter()
ContadorAmarelo = counter()

cap = cv2.VideoCapture(0)

verdeHSV = hsv(30, 100, 70, 190, 80, 165)
amareloHSV = hsv(15, 50, 150, 210, 145, 230)

TicTocVerde = TicToc(delay = 4)
TicTocAmarelo = TicToc(delay = 4)

while True:
    _, frame = cap.read()
    
    #fazendo traking dos objetos.
    frame, gray_verde, ContadorVerde = Videotracking(frame, verdeHSV, TicTocVerde, ContadorVerde)
    frame, _, ContadorAmarelo = Videotracking(frame, amareloHSV, TicTocAmarelo, ContadorAmarelo, verde=False)

    #Escreve na imagem o numero de pessoas que entraram ou sairam da area vigiada
    cv2.putText(frame, f"Entradas Verde: {ContadorVerde.getCount()}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (140, 230, 140), 2)
    cv2.putText(frame, f"Entradas Amarelo: {ContadorAmarelo.getCount()}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    
    cv2.imshow("mascara", gray_verde)
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()