'''
Desarrolle una función llamada desviacion_estandar(valores) cuyo parámetro
valores sea una lista de números reales. La función debe retornar la desviación estándar
de los valores:

Donde n es la cantidad de valores, xҧes el promedio, y los xi son cada uno de los
valores. Esto significa que hay que hacerlo siguiendo los siguientes pasos:

1. Calcular el promedio de los valores
2. A cada valor, restarle el promedio, y el resultado elevarlo al cuadrado
3. Sumar todos los valores obtenidos
4. Dividir la suma por la cantidad de valores y sacar la raíz cuadrada del resultado.
'''

def desviacion_estandar(valores):
    suma = 0
    promedio = sum(valores)/len(valores)
    i=0
    while i < len(valores):
        suma += (valores[i]-promedio)**2
        i += 1
    return (suma / (len(valores) - 1)) ** 0.5


print("La desviación estándar de [1.3, 1.3, 1.3] es : ", desviacion_estandar([1.3, 1.3, 1.3]))
print("La desviación estándar de [4.0, 1.0, 11.0, 13.0, 2.0, 7.0] es : ", desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0]))
print("La desviación estándar de [1.5, 9.5] es : ", desviacion_estandar( [1.5, 9.5]))

