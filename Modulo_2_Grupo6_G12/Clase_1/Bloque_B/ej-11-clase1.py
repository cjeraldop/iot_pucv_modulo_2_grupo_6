#numero más lejano de 5 numeros
n1 = float(input('Ingrese primer número: '))
n2 = float(input('Ingrese segundo número: '))
n3 = float(input('Ingrese tercer número: '))
n4 = float(input('Ingrese cuarto número: '))
n5 = float(input('Ingrese quinto número: '))

d1= abs(n2-n1)
d2 = abs(n3-n1)
d3 = abs(n4-n1)
d4 = abs(n5-n1)
maxim = max(d1,d2,d3,d4)
if maxim == d1:
    print('El número más lejano al primero es el segundo: ', n2)
elif maxim == d2:
    print('El número más lejano al primero es el tercero: ', n3)
elif maxim == d3:
    print('El número más lejano al primero es el cuarto ', n4)
else:
    print('El número más lejano al primero es el quinto: ', n5)

