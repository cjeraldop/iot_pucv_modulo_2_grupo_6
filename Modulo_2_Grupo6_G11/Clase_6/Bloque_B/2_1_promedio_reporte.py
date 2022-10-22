'''
Las notas de un ramo están almacenadas en el archivo “notas.txt”. Cada línea tiene
el nombre del alumno y sus seis notas, separadas por dos puntos (“:”)

Escriba un programa que cree un nuevo archivo llamado “reporte.txt”, en que
cada línea indique si el alumno está aprobado (promedio >= 4.0) o reprobado
(promedio < 4.0)

Resultado a obtener en archivo reporte.txt

Pepito aprobado
Yayita aprobado
Fulanita aprobado

Moya:5.2:4.7:1.8:3.5:2.7:4.5
'''

import os
# Replit necesita la ruta base completa
ruta_actual = os.path.dirname(os.path.abspath(__file__))

archivo = open(ruta_actual+"/notas.txt")
reporte = open(ruta_actual+"/reporte.txt","w")

def promedio(notas):
  import statistics
  return statistics.mean(notas)

for linea in archivo:  
  linealist = linea.strip().split(":")
  nombre = linealist[0]
  formato = "{}\t{} \n"
  notas = list(map(float,linealist[1:]))

  if (promedio(notas)) > 4.0:
    lineareporte = formato.format(nombre, "aprobado")
  else:
    lineareporte = formato.format(nombre, "reprobado")

  reporte.write(lineareporte)
  
archivo.close()
reporte.close()
