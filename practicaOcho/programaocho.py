'''
Verde:
    verde claro: 25,20,20
    verde oscuro: 100,255,255

Azul:
    azul claro: 100,100,20
    azul oscuro: 125,255,255
    
Rojo:
    rojo claro1: 0,100,20
    rojo oscuro1: 5,255,255
    rojo claro2: 175,100,20
    rojo oscuro2: 179,255,255

Amarillo:
    amarillo claro: 15,100,20
    amarillo oscuro: 45,255,255
    
Blanco:
    blanco claro: 220,220,220
    blanco oscuro: 255,255,255
    
NOTA DURANTE LA PRACTICA SE INSTALA PIP INSTALL NUMPY
'''

import cv2
import numpy as np
img = cv2.imread("practicaSiete/imgcinco.jpg")
cv2.putText(img, "Colores a cambia",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))

#Extraemos en HSV para procesar los patrones de colores
imagen_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

rojo_uno = np.array([0,100,20])
rojo_dos = np.array([5,255,255])
rojo_tres = np.array([175,100,20])
rojo_cuatro = np.array([179,255,255])
kernel = np.ones((7,7),np.uint8)

mascara_uno = cv2.inRange(imagen_hsv,rojo_uno,rojo_dos)
mascara_dos = cv2.inRange(imagen_hsv,rojo_tres,rojo_cuatro)
mascaras = cv2.add(mascara_uno,mascara_dos)
mascaras = cv2.morphologyEx(mascaras,cv2.MORPH_CLOSE,kernel)
mascaras = cv2.morphologyEx(mascaras,cv2.MORPH_OPEN,kernel)

resultado = cv2.bitwise_and(img,img,mask=mascaras)

#Creacion de contornos, que utilice la imagen, manten los externo y manten los proximo simple
contorno, hirachy = cv2.findContours(mascaras,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#contorno se conforma mediante diversos cuerpos de datos (matrices) raxon por la cual es importante iterarlo

for i in contorno:
    area = cv2.contourArea(i)
    if area > 500:
        cv2.drawContours(resultado,[i],-1,(255,0,0),1)
        print(area)
    
        x,y,w,h = cv2.boundingRect(i)
        areas = f"Aread: {int(area)}"
        cv2.putText(resultado,areas,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

cv2.imshow("ImagenHSV",imagen_hsv)
cv2.imshow("Imagen",img)
cv2.imshow("Mascara",mascaras)
cv2.imshow("Resultado",resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()


