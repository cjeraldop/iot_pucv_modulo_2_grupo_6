print('BIENVENIDOS - PRODUCTO INTERNO')
def producto_interno(a, b):
    suma = 0
    for i in range(len(a)):
        suma+=a[i] * b[i]
    return suma

print("El producto interno entre las listas a=[7, 1, 4, 9, 8] y b=range (5) es : ", producto_interno([7, 1, 4, 9, 8], range(5)))
