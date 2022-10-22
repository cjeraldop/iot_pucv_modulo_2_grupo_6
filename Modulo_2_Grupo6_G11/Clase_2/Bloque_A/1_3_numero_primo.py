'''
Escriba un programa que determine si un número es primo o
compuesto (no primo).
'''
numero= int(input('Ingrese un número: '))

es_primo=True
for i in range(2,numero): #Si se encuentra algún otro divisor entre 2 y numero - 1, entonces no es primo
  if (numero%i) == 0:
    es_primo=False
 
print("El número es", "primo" if es_primo else "compuesto")
