'''
Escriba una función que determine si un número es par o no.

>>> es_par(2)
True
'''

def es_par (v):
    return v % 2==0

valor= int(input("Ingresar valor:"))
print(es_par(valor))