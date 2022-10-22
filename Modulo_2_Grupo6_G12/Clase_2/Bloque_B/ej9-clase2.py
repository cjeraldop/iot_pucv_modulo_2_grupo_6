#programa que muestra la cantidad de combinaciones de una suma de puntajes en dados
n = int(input('Ingrese el puntaje deseado de los dos dados: '))
i=1
contador = 0
while i<=6:
    j=1
    while j<=6:
        if i+j==n:
            contador += 1
        else:
            contador += 0
        j += 1
    i += 1
print('La suma ', n, 'se puede obtener de', contador, 'combinaciones')
