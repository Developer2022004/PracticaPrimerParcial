
import cv2
import numpy as np
img = cv2.imread("PracticaNueve/colores.png")

#Extraemos en HSV para procesar los patrones de colores
imagen_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#NOTA PARA CREAR LA MASCARA DE COLORES, ES NECESARIO TOMAR DOS RANGOS DEL MISMO COLORS (CLARO Y OSCURO) PARA ESTABLECER
#LA MATRIZ DE COLORES
azul_uno = np.array([100,100,20])
azul_dos = np.array([125,255,255])
verde_uno = np.array([25,20,20])
verde_dos = np.array([100,255,255])

rojo_uno = np.array([0,100,20])
rojo_dos = np.array([5,255,255])
rojo_tres = np.array([175,100,20])
rojo_cuatro = np.array([179,255,255])

#Generacion de matriz para el calculo de valores exactos
kernel = np.ones((7,7),np.uint8)

#Creamos una mascara para la comparacion de pixeles de las imagenes
mascara_verde = cv2.inRange(imagen_hsv,verde_uno,verde_dos)

mascara_azul = cv2.inRange(imagen_hsv,azul_uno,azul_dos)

mascara_rojo_uno = cv2.inRange(imagen_hsv,rojo_uno,rojo_dos)
mascara_rojo_dos = cv2.inRange(imagen_hsv,rojo_tres,rojo_cuatro)

#NOTA cv2.add() solo permite el agregar 2 mascaras UMAT al elemento
mascaras = cv2.add(mascara_verde,mascara_azul)
mascaras_rojo = cv2.add(mascara_rojo_uno,mascara_rojo_dos)

mascaras = cv2.add(mascaras,mascaras_rojo)
#Econtrar la morfologia (distingue entre perros, gatos, humanos, ojos, etc...)
mascaras = cv2.morphologyEx(mascaras,cv2.MORPH_CLOSE,kernel)
mascaras = cv2.morphologyEx(mascaras,cv2.MORPH_OPEN,kernel)

resultado = cv2.bitwise_and(img,img,mask=mascaras)

#Significa que si encontro la mascara los elementos dentro de la matriz
resultado[mascaras > 0] = (255,255,255) #En caso de encontrar la matriz, sustituimos el color de la matriz por el color indicado HSV(0,0,0)

#Guardamos la mascara en imagen
cv2.imwrite("PracticaNueve/PracticaNueve.jpg",resultado)

#Fusionamos imagenes
#Valor que representa la influencia de la primera imagen
alpha = 0.9
#Valor que representa la influencia de la segunda imagen
beta = 0.9
#Valor de compensacion de la imagen
gamma = 0

#NOTA: OpenCV distingue el PNG como ausencia de pixeles.
fusion = cv2.addWeighted(resultado,alpha,img,beta,gamma)

cv2.imshow("Mascara",resultado)
#cv2.imshow("Fusion",fusion)
cv2.imshow("Imagen",img)
cv2.waitKey(0)
cv2.destroyAllWindows()