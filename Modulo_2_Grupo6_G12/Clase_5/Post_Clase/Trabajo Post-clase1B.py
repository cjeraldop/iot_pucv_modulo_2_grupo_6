resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

def diferencia_de_goles(pais, resultados):
    diferencia = 0
    gf = 0
    gc = 0
    for llave in resultados:
        eq1, eq2 = llave
        g1, g2 = resultados[llave]
        if pais == eq1:
            gf += g1
            gc += g2
            diferencia = gf-gc
                    
        if  pais == eq2:
            gf += g2
            gc += g1
            diferencia = gf-gc
    return diferencia

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

def obtener_lista_equipos(resultados):
	lista = []
	partidos =resultados.keys()

	for llave in partidos:
		for pais in llave:
			if pais not in lista:
				lista.append(pais)
	return lista

def goles(pais, resultados):
	suma = 0
	for llave in resultados:
    	eq1, eq2 = llave
		g1, g2 = resultados[llave]
        if pais == eq1:
           suma += g1
        if pais == eq2:
           suma += g2
	return suma

def posicion(resultados):
	lista = []
	equipos = obtener_lista_equipos(resultados)
	for equipo in equipos:
		puntos = calcular_puntos(equipo, resultados)
		d_goles = diferencia_de_goles(equipo, resultados)
		goles = goles(equipo, resultados)
		lista.append((puntos, d_goles, goles, equipo))
		lista.sort()
		lista.reverse()
		final = []
		for pais in lista:
			final.append(pais[-1])
		return final

		



    