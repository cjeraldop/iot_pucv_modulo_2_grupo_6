#escribir un programa para determinar si un numero es primo o no
n = int(input('Ingrese un numero: '))
i = 2
aux = False
while i < n and aux == False:
    if n % i == 0:
        aux = True
    i += 1

if aux == False:
    print('Es compuesto')
else:
    print('Es primo')