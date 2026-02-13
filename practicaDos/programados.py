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
    
    img_copia = img.copy()
    img_HSV = cv2.cvtColor(img_copia,cv2.COLOR_BGR2HSV)

    #Obtencion de canales de la imagen
    R,G,B = cv2.split(img_copia)
    H,S,V = cv2.split(img_HSV)
    
    #B = cv2.resize(B,[200,200],interpolation=cv2.INTER_AREA) Si se desea ajustar el cambio de las dimensiones del canal B de BGR
    #esto con cv2, es necesario indicar la interpolacion (algoritmo de calculo de pixeles) necesaria

    #para conocer el alto y ancho de una imagen (canales = formatos de colores, RGB, RGBA, etc...)
    alto, ancho, canales = img.shape
    #print(alto,ancho)
    
    #En formato RGB
    cv2.namedWindow("R",cv2.WINDOW_NORMAL)
    cv2.imshow("R",R)

    cv2.namedWindow("G",cv2.WINDOW_NORMAL)
    cv2.imshow("G",G)

    cv2.namedWindow("B",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("B",B)
    #Guardamos cada uno de los canales como imagenes independientes
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

    #Guardamos cada uno de los canales como imagenes independientes
    cv2.imwrite("practicaDos/copiaH.jpg",H)
    cv2.imwrite("practicaDos/copiaS.jpg",S)
    cv2.imwrite("practicaDos/copiaV.jpg",V)
    #para adaptar el tamaño de la pantalla
    cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
    cv2.imshow("Imagen",img)
    cv2.imshow("Imagen_Copia",img_copia)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("formato de imagen incorrecto")
    messagebox.showinfo("Error","Imagen incorrecta")
    exit(0)