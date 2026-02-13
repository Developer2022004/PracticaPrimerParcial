#instalar imutils funciona para realizar operaciones con matrices
import cv2
import numpy as np
import imutils
from datatime import datetime

camara = cv2.VideoCapture("practicaTrece/hora.mp4")
#Establecemos tamaño al video
camara.set(cv2.CAP_PROP_FRAME_WIDTH,400)
camara.set(cv2.CAP_PROP_FRAME_HEIGHT,300)

while(True):
    frame_actual,frame = camara.read()
    if frame_actual == False:
        break
    else:
        tiempo = datetime.now()
        
        frame = imutils.resize(frame,width=400)
        #Agregamos la imagen en escala de grises
        framegris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        azul1 = np.array([0,96,250])
        azul2 = np.array([0,55,133])
        kernel = np.ones((7,7),np.uint8)
        
        mascara = cv2.inRange(hsv, azul1, azul2)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
        
        resultado = cv2.bitwise_and(frame, frame, mask=mascara)
        resultado[mascara>0]=(10,155,25)
        
        nuevo = cv2.add(frame,resultado)
        
        framegris = cv2.cvtColor(framegris,cv2.COLOR_GRAY2BGR)
        framegris = cv2.add(framegris,resultado)
        #frame = cv2.add(frame,resultado)
        
        cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
        cv2.imshow("Video",frame)
        cv2.namedWindow("VideoGris",cv2.WINDOW_NORMAL)
        cv2.imshow("VideoGris",framegris)
        cv2.namedWindow("VideoNuevo",cv2.WINDOW_NORMAL)
        cv2.imshow("VideoNuevo",nuevo)
        if key == ord('g'):
            nombre = "archivo" + str(tiempo.second) + ".jpg"
            cv2.imwrite(nombre,frame)
            print("Imagen guardada")
    key = cv2.waitKey(1)
    if key == ord('a'):
        break
    
camara.release()
cv2.destroyAllWindows()