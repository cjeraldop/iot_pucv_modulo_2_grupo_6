'''
Escriba un programa que resuelva una ecuación de segundo grado de la
forma:

Recuerde que primero debe calcular el discriminante (d=b**2–4*a*c)
para determinar si la ecuación, (1) no tiene solución real (d<0), (2) tiene
solución única (d==0) o (3) tiene 2 soluciones (d>0).
'''

from math import sqrt
def Ec_2grado(a,b,c):
    d = b ** 2 - 4 * a * c

    if d <0:
         print("No tiene solicion real")
    elif d==0:
        x=(-b+(sqrt((b**2)-4*a*c)))/2*a
        print(x)
    else:
        y = round((-b + (sqrt((b ** 2) - 4 * a * c))) / 2 * a,2)
        y1 = round((-b - (sqrt((b ** 2) - 4 * a * c))) / 2 * a,2)
        print(y, y1)
    return
a= int(input("Ingrese valor de a :"))
b= int(input("Ingrese valor de b :"))
c= int(input("Ingrese valor de c :"))
Ec_2grado(a,b,c)