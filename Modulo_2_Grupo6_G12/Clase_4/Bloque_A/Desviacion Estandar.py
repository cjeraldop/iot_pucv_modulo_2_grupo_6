print('BIENVENIDOS - DESVIACION ESTANDAR')
def desviacion_estandar(valores):
    promedio=sum(valores)/len(valores)
    suma=0
    for v in valores:
        suma += (v - promedio)**2
    return (suma / (len(valores) - 1)) ** 0.5


print("La desviación estándar de [1.3, 1.3, 1.3] es : ", desviacion_estandar([1.3, 1.3, 1.3]))
print("La desviación estándar de [4.0, 1.0, 11.0, 13.0, 2.0, 7.0] es : ", desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0]))
print("La desviación estándar de [1.5, 9.5] es : ", desviacion_estandar( [1.5, 9.5]))
