'''
Cree un módulo llamado “mimodulo.py” y agregue la función
invertir_digitos(n) que reciba un número entero n, y entregue como
resultado el número n, con los dígitos en orden inverso.

Luego desarrolle un programa principal que use la función de dicho
módulo.
'''

from  mi_modulo import invertir_digitos
a = int(input("ingrese n: "))
print("El numero invertido ",invertir_digitos(a))