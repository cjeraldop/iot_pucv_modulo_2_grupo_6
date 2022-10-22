'''
Una consulta médica mantiene un archivo pacientes.csv con los datos
personales de sus pacientes. Cada línea del archivo tiene el rut, nombre y
edad de un paciente, separados por un símbolo ;

Escriba un programa que construya dos nuevos archivos.

- jovenes.txt, con los datos de los pacientes menores de 30 años.

- mayores.txt, con los datos de todos los pacientes mayores de 60 años.
'''

import os
# Replit necesita la ruta base completa
ruta_actual = os.path.dirname(os.path.abspath(__file__))

archivo = open(ruta_actual+"/pacientes.csv")
jovenes = open(ruta_actual+"/jovenes.txt","a")
mayores = open(ruta_actual+"/mayores.txt","a")

for linea in archivo:
  
  rut, nombreapellido, edad = linea.split(";")
  if(int(edad) < 30):
    #escribir en jovenes.txt 
    jovenes.write(linea)    
  else:
    #escribir en mayores.txt    
    mayores.write(linea)

archivo.close()
jovenes.close()
mayores.close()