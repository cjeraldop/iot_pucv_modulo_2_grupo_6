resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}
'''
Escriba la función calcular_diferencia_de_goles(equipo, resultados) que
entregue la diferencia de goles de un equipo.
>>> calcular_diferencia_de_goles(‘Chile’, resultados)
1
'''

def calcular_diferencia_de_goles(equipo, resultados):
  goles_convertidos = 0
  goles_en_contra = 0
  for resultado in resultados:
    #print(resultados[resultado])
    if (equipo in resultado): # El equipo está en la tupla
       # Si el equipo está al lado izquierdo es local, al lado derecho, es visita
      #print (resultado[0])
      if (resultado[0] == equipo):
          goles_convertidos += resultados[resultado][0]  # goles de local
          goles_en_contra += resultados[resultado][1] # goles en contra de local
      else:
          goles_convertidos += resultados[resultado][1] #goles de visita
          goles_en_contra += resultados[resultado][0] # goles en contra de visita
  return goles_convertidos - goles_en_contra
  
print(calcular_diferencia_de_goles("Honduras", resultados))