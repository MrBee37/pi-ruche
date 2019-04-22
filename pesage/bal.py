# -*- coding: utf-8 -*-
import RPi.GPIO as gpio

'''
Utilisation de l'amplificateur hx711 :
https://beeornottobee.files.wordpress.com/2017/04/hx711-avia.pdf

Utilisation avec un capteur de pesage et un µ-ordinateur raspberry pi :

Plus d'information : https://beeornottobee.wordpress.com
Contact            : beeornottobee37@gmail.com
Auteur             : lp
'''

#utilisation de la numérotation BcM des broches du connecteur GPIO de la RPI
gpio.setmode(gpio.BCM)

DT =27 #n° pin RPI en mode BCM
SCK=17 #n° pin RPI en mode BCM

#configuration pour que la RPI puisse envoyer des données sur l'entrée SCK (clock) du HX711
gpio.setup(SCK, gpio.OUT)

def readCount():
  i=0
  Count=0
  #reset 
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)

  #attente prêt
  while gpio.input(DT) == 1:
    # tant que le HX711 n'est pas prêt à déliver ses données
    # La sortie DT est à 1. la transition a 0 indiquera que
    # la transmission peut débuter
    pass

  #lecture des données
  #a chaque impulsion (1) sur l'entrée SCK
  #les 24 bits sont envoyés 1 à 1 dans l'ordre en
  #débutant par le bit de rang le plus élevé
  #(le "complément à 2" est utilisé pour les nombres négatifs
  #(inversion bit à bit puis ajout de 1))
  #les valeurs sont comprises entre 0x800000(MIN) et 0x7FFFFF(MAX) (-8388607 et +8388607)
  for i in range(24):
    gpio.output(SCK,1)
    #décalage du bit vers la gauche (correspond à x2)
    #ainsi le premier bit reçu sera muliplié par 2, 23 fois
    Count=Count<<1 
    gpio.output(SCK,0)
    if gpio.input(DT): 
      Count=Count+1
    else:
      Count=Count+0 #facultatif (équilibrage des temps d'exécution)

  gpio.output(SCK,1)    
  #25 ième impulsion de configuration (voie de mesure A, gain de 128)
  #(une 26 ième et une 27 ième impulsion pourrait être utilisée
  # pour changer de voie de mesure et de gain)      
  gpio.output(SCK,0)

  #conversion des nombres codés en "complément à 2" en nombres négatif
  if Count >> 23:
    Count = Count-0x1000000
  else:
    Count = Count
  return Count


import time
#while 1:
for i in range(100):
  count= readCount()
  print str(1000+i)[1:],count
  time.sleep(0.5)

gpio.cleanup() #reset gpio RPI
