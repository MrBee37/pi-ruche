# -*- coding: cp1252 -*-
'''
Exemple de programme de détection de frelon dans une vidéo

Plus d'information : https://beeornottobee.wordpress.com
Contact            : beeornottobee37@gmail.com
Auteur             : lp
'''

'''
Fonctionne sous linux avec python 2.7 et opencv 2.4.13

Fonctionne sous windows(anaconda)
   sur https://www.anaconda.com/distribution/  , prendre didtribution python 2.7
   la lecture de vidéo via open cv nécessite un accès à ffmpeg 
   ( non disposnible via installation conda install -c menpo opencv)
   voir détail sur blog :
   https://randomstufforganized.wordpress.com/2017/08/16/install-opencv-python-with-ffmpeg-to-anaconda/
   sur https://opencv.org/releases/ , charger  OpenCV – 2.4.13.6 pour windows
   copier cv2.pyd de C:\opencv\build\python\2.7\x64 vers  anaconda2\Lib\site-packages
   ajouter la variable d'environnement : OPENCV_DIR valeur : C:\opencv\build\x64\vc14
   ajouter le chemin ;%OPENCV_DIR%\bin
   utiliser spyder pour lancer python  ou une fenêtre Anaconda Prompt

info sur la version opencv:
from cv2 import __version__
print "version opencv : ",__version__
'''

print "Exemple de détection de frelons sur images vidéo"

import cv2
  
face_cascade = cv2.CascadeClassifier('cascadefrelon.xml')
cap = cv2.VideoCapture('filmfrelonasiatique.mp4')
if cap.isOpened():
  print "vidéo chargée"
else:
  print "vidéo NON chargée"
  
while True:
  try:
    ret, img = cap.read()
    #cv2.imshow('Exemple detection',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 12, 0, (90,60), (210,140))
    for (x,y,w,h) in faces:  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    zoomAff = 0.4
    img = cv2.resize(img,None,fx=zoomAff, fy=zoomAff, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('Exemple detection',img)
    cv2.waitKey(1)
  except:
    cv2.destroyAllWindows()
    print "fin"
    break
