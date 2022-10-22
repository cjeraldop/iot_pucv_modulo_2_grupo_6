#programa que devuelve los divisores de un numero

n= int(input('Ingrese un número: '))

#condiciones
if n <=0:
    print('Error, debe ingresar un numero mayor que 0')
else:
    i=1
    while i <=n:
        if n%i==0:
            print(i)
            i += 1
        else:
            i += 1


