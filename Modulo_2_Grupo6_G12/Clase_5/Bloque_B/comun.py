paises = {
	'Juan': {'Chile', 'Argentina'}, 
	'Pedro': {'Francia', 'Suiza', 'Chile'}, 
	'Diego': {'Chile', 'Italia', 'Francia', 'Peru'}, 
}

def cuantos_en_comun(a, b): 
	comunes = 0
	c1 = paises[a]
	c2 = paises[b]
	for c in c1: 
		if c in c2:
			comunes += 1
	return comunes	
print(cuantos_en_comun('Juan', 'Diego'))
