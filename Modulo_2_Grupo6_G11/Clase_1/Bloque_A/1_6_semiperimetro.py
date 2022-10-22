#Escriba un programa que calcule el área de un triángulo a partir de la longitud de sus lados (a, by c), y de su semiperímetro (s) mediante la siguiente fórmula:
print ("Calcular el área del triángulo a partir de la longitud de sus lados")
ladoA = int(input ("Ingrese la longitud del lado A: "))
ladoB = int(input ("Ingrese la longitud del lado B: "))
ladoC = int(input ("Ingrese la longitud del lado C: "))

semiperimetro = (ladoA + ladoB + ladoC) * 1/2
area_triangulo = (semiperimetro * (semiperimetro-ladoA) * (semiperimetro-ladoB) * (semiperimetro - ladoC))**1/2

print("El area del triangulo es:", area_triangulo)