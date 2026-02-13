import cv2
import easygui as ventana
from tkinter import messagebox

#variable para filtrar ciertas imagenes dentro de la ventana
extension = ["*.jpg","*.jpeg","*.png","*.gif"]
imagen = ventana.fileopenbox(msg="Abrir Archivo",title="Buscador de Imagenes",default="", filetypes=extension)
print(imagen[len(imagen) - 4:])
extension_imagen = imagen[len(imagen) - 4:]

if extension_imagen in [".jpg",".png",".gif"]:
    
    # img = cv2.imread("practicaUno/imguno.jpg")
    # print(img)
    img = cv2.imread(imagen)

    #para conocer el alto y ancho de una imagen (canales = formatos de colores, RGB, RGBA, etc...)
    alto, ancho, canales = img.shape
    #print(alto,ancho)

    #Manipulacion de escalabilidad de la imagen
    copia_imagen = img.copy()
    #print(f'Copia de la imagen {copia_imagen}')

    #cv2.resize(copia_imagen,(tamano_x,tamano_y),fx=0.5,fy=0.5) 
    # fx indica la funcion de escala de la imagen en dicho vector
    copia_imagen = cv2.resize(copia_imagen,(0,0),fx=0.5,fy=0.5)

    alto_copia, ancho_copia, canales_copia = copia_imagen.shape
    print(alto_copia,ancho_copia)

    #para guardar la imagen escalada
    cv2.imwrite("practicaUno/copia.jpg",copia_imagen)

    #para adaptar el tamaño de la pantalla
    cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
    cv2.imshow("Imagen",img)
    cv2.imshow("Imagen_Copia",copia_imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("formato de imagen incorrecto")
    messagebox.showinfo("Error","Imagen incorrecta")
    exit(0)