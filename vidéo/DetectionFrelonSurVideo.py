# -*- coding: cp1252 -*-
'''
Exemple de programme de d�tection de frelon dans une vid�o

Plus d'information : https://beeornottobee.wordpress.com
Contact            : beeornottobee37@gmail.com
Auteur             : lp
'''

'''
Fonctionne raspbian strech avec python 3.5 et opencv 3.4.4
Fonctionne un python 3.6, un open CV 4.1.1 en utilisant Spyder dans un environnement anaconda.
'''

print ("Exemple de d�tection de frelons sur images vid�o")
from cv2 import __version__
print ("version opencv : ",__version__)
import cv2
  
face_cascade = cv2.CascadeClassifier('cascadefrelon.xml')
cap = cv2.VideoCapture('filmfrelonasiatique.mp4')
if cap.isOpened():
  print ("vid�o charg�e")
else:
  print ("vid�o NON charg�e")
  
while True:
  try:
    ret, img = cap.read()
    cv2.imshow('Exemple detection',img)
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
    print ("fin")
    break
