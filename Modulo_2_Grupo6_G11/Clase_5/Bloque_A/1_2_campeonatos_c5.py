'''
Los resultados de un campeonato de fútbol se almacenan en un diccionario. Las
llaves son los partidos, y los valores los resultados. Revise el archivo
“campeonato_C5.py”

resultados = {

(‘Honduras’, ‘Chile’): (0, 1),
(‘Espana’, ‘Suiza’): (0, 1),
(‘Suiza’, ‘Chile’): (0, 1),
(‘Espana’, ‘Honduras’): (3, 0),
(‘Suiza’, ‘Honduras’): (0, 0),
(‘Espana’, ‘Chile’): (2, 1)

}

Escriba las siguientes funciones!

>>> obtener_lista_equipos(resultados)
[‘Honduras’, ‘Suiza’, ‘Espana’, ‘Chile’]

>>> calcular_puntos(‘Chile’, resultados)
6

>>> calcular_puntos(‘Suiza’, resultados)
4
'''

resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

def obtener_lista_equipos(resultados):
  paises = list()
  for partido in resultados:
    if partido[0] not in paises:
      paises.append(partido[0])
    if partido[1] not in paises:
      paises.append(partido[1])
  return paises


def _obtener_puntos_por_partido(goles_a_favor, goles_en_contra):
  if goles_a_favor > goles_en_contra:
    return 3
  elif goles_a_favor == goles_en_contra:
    return 1
  else:
    return 0
  


def calcular_puntos(equipo, resultados):
  puntos = 0
  for resultado in resultados:
    #print(resultados[resultado])
    if (equipo in resultado): # El equipo está en la tupla
      # Si el equipo está al lado izquierdo es local, al lado derecho, es visita
      if (resultado[0] == equipo):
          goles_del_local = resultados[resultado][0]
          goles_de_la_visita = resultados[resultado][1]
          puntos+=_obtener_puntos_por_partido(goles_del_local, goles_de_la_visita)
      else:
          goles_del_local = resultados[resultado][1]
          goles_de_la_visita = resultados[resultado][0]        
          puntos+=_obtener_puntos_por_partido(goles_del_local, goles_de_la_visita)        
  return puntos




print("La Lista de equipos es :", obtener_lista_equipos(resultados))
print("Los puntos de Chile son: ", calcular_puntos("Chile", resultados))
print("Los puntos de Suiza son: ", calcular_puntos("Suiza", resultados))
