import cv2
import numpy as np

#Para habilitar la camara (se reconoce con el indice 0 "Camara integrada del equipo")
camara = cv2.VideoCapture(0)
while(camara.isOpened()):
    #Generar el frame y parametro del frame
    frame_actual, frame = camara.read()
    if frame_actual == True:
        #Eliminamos el efecto espejo
        frame = cv2.flip(frame,1) #El metodo flip hace referencia al metodo de rotacion de la camara.
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Nota: np.array([H,S,V]) 
        # H (Hue): 100–130 → rango típico del azul. 
        # S (Saturation): 100–255 → evita detectar colores muy apagados. 
        # V (Value): 20–255 → evita zonas muy oscuras.
        rojo1 = np.array([0,100,20])
        rojo2 = np.array([5,255,255])
        rojo3 = np.array([175,100,20])
        rojo4 = np.array([179,255,255])
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 50])
        kernel = np.ones((7,7),np.uint8)
        mascara_uno = cv2.inRange(hsv,rojo1,rojo2)
        mascara_dos = cv2.inRange(hsv,rojo3,rojo4)
        mascara_tres = cv2.inRange(hsv,lower_black,upper_black)
        mascaras = cv2.add(mascara_uno,mascara_dos)
        mascaras = cv2.add(mascaras,mascara_tres)
        mascaras = cv2.morphologyEx(mascaras, cv2.MORPH_CLOSE, kernel)
        mascaras = cv2.morphologyEx(mascaras, cv2.MORPH_OPEN, kernel)
        resultado = cv2.bitwise_and(frame, frame, mask=mascaras)
        resultado[mascaras > 0] = (100,0,12)
        
        cv2.imshow("Transmision",frame)
        cv2.imshow("Resultado",resultado) 
        key = cv2.waitKey(1)
        if key == ord('a'):
            break
    else:
        break


camara.release()
cv2.destroyAllWindows()