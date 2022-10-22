#Escribir un programa que invierta un entero de 3 digitos
num = int(input('Escriba un entero de 3 dígitos: '))
d1 = num % 10
num = num //10
d2 = num % 10
num = num //10
d3 = num % 10
invertido = str(d1*100+d2*10+d3)

print ('El número invertido es: ', invertido)
