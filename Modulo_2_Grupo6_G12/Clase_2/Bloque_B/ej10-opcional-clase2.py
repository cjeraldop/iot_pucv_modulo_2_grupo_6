#programa colecta fundacion
n = int(input('Ingrese la cantidad de posibles benefactores: '))
m = int(input('Ingrese el maxímo monto que buscan cubrir en la colecta'))

mayor = -float('inf')
i=1
contador = 0
gran_benefactor = ''
while i <= n and contador < m:
    persona = str(input('Ingrese nombre de la persona ' + str(i) + ': '))
    monto = int(input('Ingrese monto donado: '))
    if monto > mayor:
        mayor = monto
        gran_benefactor = persona

    contador += monto
    i += 1
print('Se alcanzó el monto o la cantidad de benefactores')
print('El monto máximo donado fue: ', mayor , 'que fue donado por: ', gran_benefactor)


