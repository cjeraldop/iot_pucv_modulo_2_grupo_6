'''
Un viajero desea saber cuánto tiempo tomó el viaje que realizó. Él tiene la duración
en minutos de cada uno de los tramos del viaje.
Escriba un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado, el tiempo total de viaje en formato horas:minutos .

El programa debe dejar de pedir tiempos cuando se ingrese un 0.

Duración del tramo: 15
Duración del tramo: 30
Duración del tramo: 87
Duración del tramo: 0
Tiempo total de viaje: 2:12 horas
'''

continuar = True
suma = 0
while continuar:
    tiempo = int(input('Duracion tramo: '))
    if tiempo == 0:
        continuar = False
    else:
        suma+= tiempo
horas = suma // 60
minutos = suma % 60
print('Tiempo total de viaje:', str(horas) + ':' + str(minutos), 'horas')