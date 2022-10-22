#Escriba un programa que genere aleatoriamente el lanzamiento de una moneda y muestre por pantalla su resultado (CARA o SELLO).
#Lanzarmoneda= input('Lanzar mone
from random import randint
x= randint(0,1)
if x == 0:
  print ("Sello")
else:
  print("Cara")