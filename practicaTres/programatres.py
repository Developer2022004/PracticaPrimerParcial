import cv2
img = cv2.imread("practicaTres/imgdos.jpg")
img_copy = img.copy()
img_dos = cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
cv2.imwrite("Gris.jpg",img_dos)

img_dos = cv2.imread("Gris.jpg")
#concatenacion de imagenes. busca como concatenar en horizontal en python.
#cv2.namedWindow("Gris",cv2.WINDOW_NORMAL)
#cv2.imshow("Gris",img_dos)
dos_imagenes = cv2.vconcat([img,img_dos])

cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
cv2.imshow("Imagen",dos_imagenes)
cv2.waitKey(0)
cv2.destroyAllWindows()