'''
Cree una función codigo_palabra(codigo) que reciba un código cifrado de sólo letras y entregue el mensaje descifrado. La regla de descifrado es la siguiente: la palabra descifrada se obtiene recorriendo desde el final de la palabra hasta el comienzo, considerando las letras solo en ubicaciones impares. Empezando desde la última letra.

>>> codigo_palabra(‘aczaarltp’)
‘plaza’
>>> codigo_palabra(‘axruatgrrreov’)
‘vergara’
'''

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

codigo= str(input("Ingrese la palabra codificada :"))
print (codigo_palabra(codigo))