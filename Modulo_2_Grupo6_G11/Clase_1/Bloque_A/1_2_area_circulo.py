#Ejercicio 2
#Área del círculo (A = π r²).
from math import pi
radio_circulo = float(input("Ingrese el radio de un circulo en milimetros:"))
area_circulo = pi * radio_circulo**2 
print("El área de la circunferencia es:", round(area_circulo,2) ," en mm2")