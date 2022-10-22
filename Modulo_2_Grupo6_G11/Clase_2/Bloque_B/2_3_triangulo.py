#Escriba un programa que pida al usuario un valor entero n e imprima un patrón triangular de n líneas como el que se muestra a continuación:

cantidad = int(input("Ingrese la cantidad:"))
i=1
while i <= cantidad: 
  imprimir = "+"*i
  print(imprimir, end="") 
  print("") 
  i+=1