'''
Una cadena de ADN es una secuencia de bases nitrogenadas llamadas: (1) adenina, (2) citosina, (3) timina y
(4) guanina. En un programa una cadena se representa como un string de caracteres ‘a’, ‘c’, ‘t’ y ‘g’. Escriba
la función cadena_al_azar(n) que retorne una cadena aleatoria de ADN de largo n.

>>> cadena_al_azar(10)
‘acgtccgcct’
>>> cadena_al_azar(10)
‘tgttcgcatt’
'''


def cadena_al_azar(n):
    from random import choice
    i = 0
    final = ""
    while i < n:
        final += choice("atcg")
        i += 1
    return final


n = int(input("Ingrese el largo de la secuencia de ADN n: "))
print(cadena_al_azar(n))
