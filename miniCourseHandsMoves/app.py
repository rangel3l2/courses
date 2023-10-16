import cv2 
from cvzone.HandTrackingModule import HandDetector

camera = cv2.VideoCapture(0)
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
#camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
detector = HandDetector(maxHands=2)

while(True):
    
    _,imagem_de_entrada = camera.read()
    lista_maos = detector.findHands(imagem_de_entrada, draw= True)

    cv2.imwrite('saida.jpg', imagem_de_entrada)
    # if lista_maos:
    #     primeira_mao = lista_maos[0]
    #     dedinhos = detector.fingersUp(primeira_mao[0])    
    cv2.imshow('imagem', imagem_de_entrada)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
#imagem_de_saida  = cv2.imread('saidajpg')
#imagem_de_saida = imagem_de_saida [0,:,:] + 70
#cv2.imwrite('saida.jpg', imagem_de_saida)
    
camera.release()