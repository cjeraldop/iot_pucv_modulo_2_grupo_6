'''
A cada cadena le corresponde una cadena complementaria, que se obtiene
intercambiando las adeninas con las timinas, y las citosinas con las guaninas.

cadena = ‘cagcccatgaggcagggtg’
complemento = ‘gtcgggtactccgtcccac’

Escriba la función complementaria(c) que entregue la cadena complementaria
de c.

>>> cadena = ‘cagcccatgaggcagggtg’
>>> complementaria(cadena)
‘gtcgggtactccgtcccac’
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

#Probar