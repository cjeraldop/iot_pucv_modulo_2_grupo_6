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
            

print(diferencia_de_goles('Chile', resultados))