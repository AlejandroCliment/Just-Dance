import cv2
import os
cam=cv2.VideoCapture("/home/erika/Escritorio/Vision/just dance refachero/rasputin.mp4")

current=0
while (True):
    ret,frame=cam.read()
    if not ret:
        quit()
    name ='/home/erika/Escritorio/Vision/just dance refachero/frames_mediapipe/frame' + str(current) +'video8'+'.jpg'
    print('Creating...'+name)
    if(current%150==0):
        cv2.imwrite(name,frame)
    current+=1

cam.release()
cv2.destroyAllWindows()