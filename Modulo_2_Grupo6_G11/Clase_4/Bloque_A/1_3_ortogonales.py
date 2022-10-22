'''
Dos listas de números son ortogonales si su producto interno es cero. Escriba
la función son_ortogonales(a, b) que indique si a y b son ortogonales.

>>> son_ortogonales([2, 1], [-3, 6])
True
'''
def son_ortogonales(a, b):
    i = 0
    n = len(a)
    prod = 0
    while i < n:
        c = a[i] * b[i]
        prod = prod + c
        i += 1
    return prod ==0
  
print("¿Los vectores [2,1],[-3,6]) son ortogonales?", son_ortogonales([2,1],[-3,6]))
