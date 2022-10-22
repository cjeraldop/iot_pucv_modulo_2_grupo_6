pal1 = input('Ingrese palabra 1: ')
pal2 = input('Ingrese palabra 2: ')
l1 = len(pal1)
l2 = len(pal2)
#condiciones
if l2 > l1:
    print('La palabra 2 es más larga en: ', l2-l1, 'cáracteres')
elif l1 > l2:
    print('La palabra 1 es más larga en: ', l1-l2, 'cáracteres')
else:
    print('Ambas palabras son iguales en cantidad de cáracteres')