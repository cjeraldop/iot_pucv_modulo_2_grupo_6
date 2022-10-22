'''
El producto interno de dos listas de números es la suma de los productos de
los términos de ambas. Por ejemplo, si: a = [5, 1, 6] y b = [1, -2, 8]
entonces el producto interno entre a y b es: (5 * 1) + (1 * -2) + (6 * 8)

Escriba la función producto_interno(a, b) que entregue el producto interno
entre a y b.

>>> a = [7, 1, 4, 9, 8]
>>> b = range(5)
>>> producto_interno(a, b)
68
'''

def producto_interno (a,b):
        i=0
        n=len(a)
        prod=0
        while i < n:
                c =a[i]*b[i]
                prod = prod+c
                i +=1
        #print (prod)
        return prod

print (producto_interno ( [7, 1, 4, 9, 8], range(5)))