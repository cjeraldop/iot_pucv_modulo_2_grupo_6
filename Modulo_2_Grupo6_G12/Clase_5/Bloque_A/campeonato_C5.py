resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

def obtener_lista_equipos(resultados):
	lista = []
	partidos =resultados.keys()

	for llave in partidos:
		for pais in llave:
			if pais not in lista:
				lista.append(pais)
	return lista

def calcular_puntos(pais, resultados):
      puntos = 0
      for llave in resultados:
            eq1, eq2 = llave
            g1, g2 = resultados[llave]
            if pais == eq1:
              if g1 > g2:
                    puntos += 3
              if g1 == g2:
                puntos += 1
            if pais == eq2:
              if g2 > g1:
                    puntos += 3
              if g2 == g1:
                    puntos += 1
      return puntos


		



print(calcular_puntos('Chile', resultados))

