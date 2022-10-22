'''
Las temperaturas mínimas y máximas de algunas ciudades están guardadas en un diccionario cuyas llaves son
ciudades, y sus valores son tuplas (mínima, máxima).
temp = {

‘Vina del mar’: (9, 26),
‘Valparaiso’: (10, 24),
‘Quilpue’: (7, 30),
‘Quintero’: (4, 22)

}
Escriba la función crear_reporte(temperaturas), cuyo parámetro es el diccionarios de temperaturas, y que
genere el archivo de texto con el formato del ejemplo.

Ejemplo archivo generado: reporte.txt
'''


import os
# Replit necesita la ruta base completa
ruta_actual = os.path.dirname(os.path.abspath(__file__))

temp = {
	'Vina del mar': (9, 26), 
	'Valparaiso': (10, 24), 
	'Quilpue': (7, 30), 
	'Quintero': (4, 22)
}

def crear_reporte(temperaturas):
	ciudades= list(temperaturas.keys())
	temperatura= list(temperaturas.values())
	i=0
	reporte= open(ruta_actual+"/reporte.txt","w")
	while i < len(ciudades):
		minimo,maximo= (temperatura[i])
		linea=ciudades[i]+": "+"minima "+" "+ str(minimo) +" ,"+" "+"maxima"+" "+ str(maximo) + "\n"

		reporte.write(linea)
		i +=1
	reporte.close()
  
crear_reporte(temp)
