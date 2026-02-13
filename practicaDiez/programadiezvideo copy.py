import cv2
from moviepy import VideoFileClip
import pygame

videoReal = "video.mp4"
videoR = VideoFileClip(videoReal)#cargar video
audioReal = videoR.audio#extra_audio

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)  # ← cambio clave aquí

audioReal.write_audiofile("temp_audio.wav", codec='pcm_s16le')        # ← agregado codec para compatibilidad
pygame.mixer.music.load("temp_audio.wav")#cargar el archivo de audio temporal
pygame.mixer.music.play()#reproducir el audio

video = cv2.VideoCapture(videoReal)#abrir video
#controlar los frames del videoa
fpd = video.get(cv2.CAP_PROP_FPS)#obtener frames por segundo
if fpd <= 0: fpd = 30  # fallback simple, sin if grande
tiempo = int(1000 / fpd)# ← corregido a 1000 (milisegundos reales)

#leer frames del video
while True:
    ret,frame = video.read()#leer frame
    if ret == True:#si se leyo el frame correctamente
        cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)#crear ventana
        cv2.imshow("Frame",frame)#mostrar frame
        if cv2.waitKey(tiempo) & 0xFF == ord('a'):#esperar a que se presione la tecla 'a'
            print("Presionaste la letra A")#si se presiona la tecla 'a', salir del bucle
            break
    else:
        break

video.release()#liberar el video
cv2.destroyAllWindows()#cerrar todas las ventanas abiertas