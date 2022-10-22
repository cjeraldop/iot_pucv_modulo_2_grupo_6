'''
Escriba un programa que entregue todos los divisores de un número
entero ingresado. Su programa deberá validar que el número ingresado
sea positivo (> 0). En caso que cero o negativo, deberá mostrar un
mensaje de error.

>>> Ingrese un numero: -1
Error, debe ingresar un numero mayor a 0

>>> Ingrese un numero: 20
1 2 4 5 10 20
'''

numero= int(input('Ingrese un número '))

if numero<=0:
  print("Error, debe ingresar un numero mayor a 0")
  exit(0)

i=1
salida=''
while (i<=numero):
  if numero%i==0:
    salida += str(i) + " "
  i+=1
print(salida)