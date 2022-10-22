#Ejercicio 3
#Escriba un programa que invierta un número entero de tres dígitos.
numero_invertir = input("Ingrese un número entero:")
cadena_numero_invertido = numero_invertir[::-1] #Tratar la entrada como texto e invertir la cadena.
int_cadena_invertida = int(cadena_numero_invertido)
print("El número invertido es:", int_cadena_invertida)
