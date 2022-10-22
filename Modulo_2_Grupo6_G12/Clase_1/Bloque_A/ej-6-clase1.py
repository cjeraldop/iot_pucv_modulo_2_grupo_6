#Programa que calcula el área de un triangulo
from math import sqrt

a = float(input('Ingrese longitud de lado 1: '))
b = float(input('Ingrese longitud de lado 2: '))
c = float(input('Ingrese longitud de lado 3: '))
s = (a+b+c)/2


aux = sqrt((s*(s-a)*(s-b)*(s-c)))

print("El área del triángulo es: ", round(aux, 2))