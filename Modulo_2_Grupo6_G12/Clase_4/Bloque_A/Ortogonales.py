print('BIENVENIDOS - ¿SON ORTOGONALES?')
def es_ortogonal(a, b):
    suma = 0
    for i in range(len(a)):
        suma+=a[i] * b[i]
    return suma == 0

print("¿Son ORTONALES las listas a=[2, 1] y b=[-3, 6]?", es_ortogonal([2,1],[-3,6]))
