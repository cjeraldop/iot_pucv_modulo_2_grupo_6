def invertir_digitos(n):
	inverso = ''
	while n > 0:
		d = n % 10
		n = n // 10
		inverso += str(d)
	return int(inverso)
