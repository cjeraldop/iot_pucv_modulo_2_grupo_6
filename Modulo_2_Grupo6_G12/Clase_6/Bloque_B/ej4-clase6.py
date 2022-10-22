import os
# Replit necesita la ruta base completa
ruta_actual = os.path.dirname(os.path.abspath(__file__))

archivo = open(ruta_actual+'/notas.txt')
reporte = open(ruta_actual+'/reporte.csv', 'w')

for linea in archivo:
    todo= linea.strip().split(':')
    nombre = todo[0]
    notas = list(map(float, todo[1:]))
    promedio = sum(notas) / len (notas)
    if promedio < 4.0:
        reporte.write('El alumno {} está reprobado \n'.format(nombre))
    else:
        reporte.write('El alumno {} está aprobado \n'.format(nombre))
archivo.close()
reporte.close()

