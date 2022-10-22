'''
Ejercicio de la función para la cadena complementaria
'''
def complementaria(c): 
	reemplazo = ''
	for termino in c: 
		if termino == 'a': 
			reemplazo += 't'
		if termino == 'c': 
			reemplazo += 'g'
		if termino == 't': 
			reemplazo += 'a'
		if termino == 'g': 
			reemplazo += 'c'
	return reemplazo
