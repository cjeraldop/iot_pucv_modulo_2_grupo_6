#En estadística descriptiva, se define el rango de un conjunto de datos reales
#como la diferencia entre el mayor y el menor de los datos.

#Por ejemplo, si los datos son [5.96, 6.74, 7.43, 4.99, 7.20, 0.56,
#2.80] entonces el rango será: 7.43 – 0.56 = 6.87

#Escriba un programa que; (1) pregunte al usuario cuántos datos ingresará, (2)
#pida los datos uno por uno y (3) entregue como resultado el rango de los
#datos (suponga que todos los datos que ingrese serán válidos).

cantidad = int(input("Ingrese la cantidad:"))
n=0
mayor = -float("inf")
menor = float("inf")
while n < cantidad:
  numero = float(input("Ingrese un número: "))
  if numero > mayor:
    mayor = numero
  if numero < menor:
    menor = numero
  n+=1

rango = mayor - menor
print("El número mayor es: ", mayor, ", el menor es: ", menor, " el rango es: ", rango)