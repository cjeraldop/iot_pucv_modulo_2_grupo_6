'''
Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número
ingresado por el usuario.
'''

numero= int(input('Ingrese un número '))
i=1

while (i<=10):
  print(numero,"x",i," =",numero*i)
  i+=1
