#Recortar dos imagenes
import cv2
img = cv2.imread("practicaCinco/imgdos.jpg")

#Herramienta de recorte que no depende de la matriz de la imagen, sino del puntero cv2.selectROI("ROI",imagen)
imagen_roi = cv2.selectROI("ROI",img)

#Recorte de la imagen en formato de columnas de la imagen (Es el recorte)
nueva_imagen = img[int(imagen_roi[1]):int(imagen_roi[1]+imagen_roi[3]),
                   int(imagen_roi[0]):int(imagen_roi[0]+imagen_roi[2])]

# Nota: Imagen roi guarda la informacion de los cuatro segmentos del recorte de ROI, 
# es decir cada cuadro dibujado en el recorte
#print(imagen_roi)

alto, ancho, canales = nueva_imagen.shape
nueva_imagen = cv2.resize(nueva_imagen,(ancho,alto))

cv2.imwrite("practicaCinco/recortePracCinco.jpg",nueva_imagen)
imagen_recortada = cv2.imread("practicaCinco/recortePracCinco.jpg")

cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
cv2.imshow('Imagen',img)
cv2.imshow("Imagen Recortada",imagen_recortada)

#Extraemos los canales de colores de la imagen
R,G,B = cv2.split(imagen_recortada)

#Abrimos las imagenes convertidas en diferentes canales de colores acorde a la tecla pulsada
while(True):
    if cv2.waitKey(1) & 0xFF == ord('a'):
        print("Presionaste la letra A")
        cv2.imshow("R",R)
        
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Presionaste la letra S")
        cv2.imshow("B",B)
        
    if cv2.waitKey(1) & 0xFF == ord('d'):
        print("Presionaste la letra D")
        cv2.imshow("G",G)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Salir")
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()