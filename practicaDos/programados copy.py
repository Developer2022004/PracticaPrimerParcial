import cv2
img = cv2.imread("practicaUno/imgdos.jpg")
img_copia = img.copy()
img_HSV = cv2.cvtColor(img_copia,cv2.COLOR_BGR2HSV)

#Obtencion de canales de la imagen
R,G,B = cv2.split(img)
H,S,V = cv2.split(img_HSV)

#En formato RGB
cv2.namedWindow("R",cv2.WINDOW_NORMAL)
cv2.imshow("R",R)

cv2.namedWindow("G",cv2.WINDOW_NORMAL)
cv2.imshow("G",G)

cv2.namedWindow("C",cv2.WINDOW_NORMAL)
cv2.imshow("B",B)
cv2.imwrite("practicaDos/copiaR.jpg",R)
cv2.imwrite("practicaDos/copiaG.jpg",G)
cv2.imwrite("practicaDos/copiaB.jpg",B)

#En formato HSV

cv2.namedWindow("H",cv2.WINDOW_NORMAL)
cv2.imshow("H",H)

cv2.namedWindow("S",cv2.WINDOW_NORMAL)
cv2.imshow("S",S)

cv2.namedWindow("V",cv2.WINDOW_NORMAL)
cv2.imshow("V",V)

cv2.imwrite("practicaDos/copiaH.jpg",H)
cv2.imwrite("practicaDos/copiaS.jpg",S)
cv2.imwrite("practicaDos/copiaV.jpg",V)

cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
cv2.imshow("Imagen",img)

cv2.waitKey(0)
cv2.destroyAllWindows()