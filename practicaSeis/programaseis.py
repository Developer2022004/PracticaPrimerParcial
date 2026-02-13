import cv2
img_uno = cv2.imread("practicaSeis/imguno.jpg")
img_dos = cv2.imread("practicaSeis/imgdos.jpg")

#para fucionar imagenes, es necesario que ambas tengan el mismo tamaño

alto_uno, ancho_uno, canales_uno = img_uno.shape
alto_dos, ancho_dos, canales_dos = img_dos.shape

if(alto_uno + ancho_uno) > (alto_dos + ancho_dos):
    img_uno = cv2.resize(img_uno,(ancho_dos,alto_dos))
else:
    img_dos = cv2.resize(img_dos,(ancho_uno,alto_uno))
    
#Valor que representa la influencia de la primera imagen
alpha = 0.3
#Valor que representa la influencia de la segunda imagen
beta = 0.7
#Valor de compensacion de la imagen
gamma = 0

#NOTA: OpenCV distingue el PNG como ausencia de pixeles.
resultado = cv2.addWeighted(img_uno,alpha,img_dos,beta,gamma)
cv2.imwrite("practicaSeis/resultadofusion.jpg",resultado)
resultado = cv2.imread("practicaSeis/resultadofusion.jpg")

cv2.imshow("Imagen Uno",img_uno)
cv2.imshow("Imagen Dos",img_dos)
cv2.imshow("Resultado",resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
#AQUI SE TERMINA LAS PACTICAS RELACIONADAS A LAS IMAGENES