#Programa para mostrar el rango de varios números
n = int(input('Cuantos datos ingresara?: '))
i = 0
menor = float('inf')
mayor = -float('inf')
while i < n:
	num = float(input('Ingrese número '+ str(i+1) +' :'))
	if num < menor:
		menor = num
	if num > mayor:
		mayor = num
	i += 1
print('El rango es', round(mayor - menor, 2))