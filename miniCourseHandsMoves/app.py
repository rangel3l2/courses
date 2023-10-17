from cvzone.HandTrackingModule import HandDetector
import cv2

camera = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

while(True):

    _,imagem_de_entrada = camera.read()
    lista_maos = detector.findHands(imagem_de_entrada, draw= True)

    cv2.imwrite('saida.jpg', imagem_de_entrada)
    if lista_maos:
         primeira_mao = lista_maos[0]

         if(primeira_mao):
            center1 = primeira_mao[0]['center']
            print(center1)
            fingers = detector.fingersUp(primeira_mao[0])


    cv2.imshow('imagem', imagem_de_entrada)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break

camera.release()
