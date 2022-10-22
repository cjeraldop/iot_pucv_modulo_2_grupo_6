temp = {
	'Vina del mar': (9, 26),
	'Valparaiso': (10, 24),
	'Quilpue': (7, 30),
	'Quintero': (4, 22)
}

def crear_reporte(temp):
  import os
  # Replit necesita la ruta base completa
  ruta_actual = os.path.dirname(os.path.abspath(__file__))

  archivo = open(ruta_actual+'/reporte.txt', 'w')
  #No entiendo porque no corre. Lanza un error de indexación con el for pero no veo el motivo
  for ciudad, tupla in temp.items() :
    maxima = tupla[1]
    minima = tupla[0]
    linea = '{}: T° max {}, T° min {}\n'.format(ciudad, maxima, minima)
    archivo.write(linea)
  archivo.close()


crear_reporte(temp)
