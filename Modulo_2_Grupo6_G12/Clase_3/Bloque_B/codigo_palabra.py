def codigo_palabra (codigo):
	palabra = list(codigo)
	i=0
	n=len(palabra)
	a=""
	while i <n:
		if i%2==0:
			a= palabra[i] +a
		else:
			a = a
		i +=1
	return a

codigo= str(input("Ingrese la palabr codificadda :"))
print (codigo_palabra(codigo))