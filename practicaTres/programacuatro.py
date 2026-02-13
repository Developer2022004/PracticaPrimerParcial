#Recortar dos imagenes
import cv2
img = cv2.imread("practicaTres/imgdos.jpg")
alto, ancho, canal = img.shape

print(f"el alto es: {alto//2}, el ancho es: {ancho//2}")

parte_uno_vertical = img[0:,0:262]
cv2.imwrite("parte_uno_v.jpg",parte_uno_vertical)

parte_dos_vertical = img[0:,262:]
cv2.imwrite("parte_dos_v.jpg",parte_dos_vertical)

#para recortar las imagenes.abs
parte_dos_vertical = cv2.imread("parte_dos_v.jpg")
# cv2.imshow("ParteDos",parte_dos_vertical)
parte_uno_vertical = cv2.imread("parte_uno_v.jpg")
# cv2.imshow("ParteUno",parte_uno_vertical)

cv2.imshow("ParticionUno",parte_uno_vertical)
cv2.imshow("ParticionDos",parte_dos_vertical)

#redimensionamos cada uno de los elementos para lograr cargalos en hconcat()
# imgPUno = cv2.resize(parte_uno_vertical,(ancho,alto))
# imgPDos = cv2.resize(parte_dos_vertical,(ancho,alto))
# dos_imagenes = cv2.hconcat([imgPUno,imgPDos])
dos_imagenes = cv2.hconcat([parte_uno_vertical,parte_dos_vertical])

#NOTA SI DESEAS EVITAR REDIMENSIONAR LOS ELEMENTOS RECORTADOS, ES NECESARIO UTILIZAR DIVISION MATEMATICA CON REDONDEO
#AL ENTERO PROXIMO, PARA ELLO UTILIZA (Dividendo//Divisor)

#NOTA PARA LOGRAR UTILIZAR hconcat/vconcat es necesario que cada uno de los elementos involucrado, deben de tener un tamaño igual.

# cv2.namedWindow("original",cv2.WINDOW_NORMAL)
cv2.imshow("original",dos_imagenes)
cv2.waitKey(0)
cv2.destroyAllWindows()