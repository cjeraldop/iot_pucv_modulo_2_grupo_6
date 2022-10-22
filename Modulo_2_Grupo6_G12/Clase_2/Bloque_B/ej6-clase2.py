#calcular el mayor y mostrar su pocisión
n = int(input('Ingrese n: '))
i = 1
mayor = -float('inf')
while i <= n:
    numero = int(input('Ingrese número: ' + str(i) + ': '))
    if numero > mayor:
        mayor = numero
        pos = i
    i += 1
print('El mayor es', mayor, 'que corresponde a la posición', pos)