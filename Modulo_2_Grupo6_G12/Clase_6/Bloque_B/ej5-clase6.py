import os
# Replit necesita la ruta base completa
ruta_actual = os.path.dirname(os.path.abspath(__file__))

archivo = open(ruta_actual+'/pacientes.csv')
jovenes = open(ruta_actual+'/jovenes.csv', 'w')
tercera_edad = open(ruta_actual+'/tercera_edad.csv', 'w')

for linea in archivo:
    rut, nombre, edad = linea.strip().split(';')
    if int(edad) < 30:
        jovenes.write(linea)
    if int(edad) > 60:
        tercera_edad.write(linea)

jovenes.close()
tercera_edad.close()
archivo.close()

