#programa de transformación de tiempos en suma y cambio de formato
continuar = True
suma = 0
while continuar == True:
    tiempo = int(input('Ingrese duracion tramo en minutos: '))
    if tiempo == 0:
        continuar = False
    else:
        suma = suma + tiempo
horas = suma // 60
minutos = suma % 60
print('El tiempo total de viaje es:', str(horas) + ':' + str(minutos), 'horas')