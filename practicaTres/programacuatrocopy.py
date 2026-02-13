import cv2
img = cv2.imread("practicaTres/imgdos.jpg")
parte = img[0:20,0:]
print(parte)
cv2.imwrite("parte.jpg",parte)

#para recortar las imagenes.abs
parte = cv2.imread("parte.jpg")
cv2.imshow("Parte",parte)
print(parte)


cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
cv2.imshow("Imagen",img)
cv2.waitKey(0)
cv2.destroyAllWindows()