#Escriba un programa que muestre el área del circulo a partir del radio
from math import pi
r = float(input('Ingrese el radio del circulo: '))
area = round(pi*r**2,2)

print ('El área del circulo es: ', area)

