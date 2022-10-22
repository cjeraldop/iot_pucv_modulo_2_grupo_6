#Escriba un programa que permita determinar el número mayor de n números solicitados al usuario.
cantidad = int(input("Ingrese la cantidad:"))
n=0
mayor = -float("inf")
while n < cantidad:
  numero = int(input("Ingrese un número: "))
  if numero > mayor:
    mayor = numero
  n+=1
print("El número mayor es: ", mayor)