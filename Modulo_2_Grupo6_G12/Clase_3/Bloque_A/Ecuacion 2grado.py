def discriminante(a,b,c):
    return b**2-4*a*c

a = float(input('Ingrese el valor a: '))
b = float(input('Ingrese el valor b: '))
c = float(input('Ingrese el valor c: '))

r = discriminante(a, b, c)

if r < 0:
    print('No tiene solucion real')
elif r == 0:
    solucion = round(-b / (2*a), 3)
    print('Tiene solucion unica = ', solucion)
else:
    solucion = round((-b - (r**0.5))/(2*a),3)
    solucion2 = round((-b + (r**0.5))/(2*a),3)
    print('Tiene 2 soluciones:')
    print('solucion 1 = ', solucion)
    print('solucion 2 = ', solucion2)
