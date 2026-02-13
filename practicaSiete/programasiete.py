
#rangos de colores

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
    
NOTA DURANTE LA PRACTICA SE INSTALA PIP INSTALLA NUMPY

Hue (H) → Representa el color (0-179 en OpenCV)

Saturation (S) → Intensidad del color (0-255)

Value (V) → Brillo (0-255)
'''
import numpy as np
import cv2
img = cv2.imread("practicaSiete/imgcinco.jpg")
cv2.putText(img, "Colores a cambiar",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
#cv2.putText(imagen,Texto,coordenadas(x,y),Fuente,Escala,ColorRGB)

#Extraemos en HSV para procesar los patrones de colores
imagen_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
verde_uno = np.array([25,20,20])
verde_dos = np.array([100,255,255])

#Generacion de matriz para el calculo de valores exactos
kernel = np.ones((7,7),np.uint8)
# en caso de no detectar algunos colores con exactitud se recomienda incrementar el kernel a 9,9

#Creamos una mascara para la comparacion de pixeles de las imagenes
mascara = cv2.inRange(imagen_hsv,verde_uno,verde_dos)
#Tomando en cuenta la morfologia exterior cerrada solo se usa cuando las figuras de la imagen son complejas no sencillas
mascara = cv2.morphologyEx(mascara,cv2.MORPH_CLOSE,kernel)
#Tomando en cuenta la morfologia exterior abierta solo se usa cuando las figuras de la imagen son complejas no sencillas
mascara = cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel)

resultado = cv2.bitwise_and(img,img,mask=mascara)

#Creacion de contornos, que utilice la imagen, manten lo externo y manten lo proximo simple
contorno, hirachy = cv2.findContours(mascara,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#contorno se conforma mediante diversos cuerpos de datos (matrices) razon por la cual es importante iterarlo

for i in contorno:
    #Calcula el área del objeto detectado.
    area = cv2.contourArea(i)
    if area > 500:
        cv2.drawContours(resultado,[i],-1,(255,0,0),1)
        #cv2.drawContours(imagen, contornos, indice, color, grosor) dibuja contornos
        #imagen → Imagen donde se dibujarán los contornos. 
        #contornos → Lista de contornos (arrays de puntos). 
        #indice → Indica qué contorno dibujar. #0 → dibuja solo el primer contorno 1 → el segundo -1 → dibuja todos los contornos en la lista
        #color → Color del contorno (formato BGR).
        #grosor → Espesor de la línea. # 1 → línea delgada 2 o más → línea más gruesa -1 → rellena el contorno completamente
        print(area)
    
        x,y,w,h = cv2.boundingRect(i)
        areas = f"Aread: {int(area)}"
        cv2.putText(resultado,areas,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

cv2.imshow("ImagenHSV",imagen_hsv)
cv2.imshow("Imagen",img)
cv2.imshow("Mascara",mascara)
cv2.imshow("Resultado",resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()