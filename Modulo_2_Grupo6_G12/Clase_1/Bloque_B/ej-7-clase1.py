#Programa para hacer un cara y sello aleatorio
from random import randint
moneda = randint(0, 1)
if moneda == 0:
    print('Es Cara')
else:
    print('Es Sello')