#pip install moviepy pygame Libreria que permite escuchar el sonido de lo videos

import cv2

from moviepy.editor import VideoFileClip
import pygame

videoReal = "practicaDiez/hora.mp4"
videoR = VideoFileClip(videoReal)
audio = videoR.audio

#Que obtenga cada uno de los canales de audio
pygame.mixer.init()
audio.write_audiofile("practicaDiez/temp_audio.wav")
pygame.mixer.music.load("practicaDiez/temp_audio.wav")
pygame.mixer.music.play()

video = cv2.VideoCapture(videoReal)

#para controlar los frames por segundo
fps = video.get(cv2.CAP_PROP_FPS)
tiempo = int(1000/fps)
print(fps)

while(True):
    #hacer lectura de cada uno de sus pixeles
    frame_existente,frame = video.read()
    if frame_existente == True:
        #Si encuentra el frame, continua reproduciendo y mostrando
        cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(tiempo) & 0xFF == ord('c'):
            pygame.mixer.music.stop()
            break
    else:
        #Si no encuentra el frame, deja de reproducir (termina el video)
        break

video.release()
cv2.destroyAllWindows()