altura = float(input('Ingrese estatura: '))
peso = float(input('Ingrese peso: '))
edad = int(input('Ingrese edad: '))

imc = peso / (altura ** 2)

if edad < 45:
    if imc < 22.0:
        print('Bajo')
    else:
        print('Medio')
else:
    if imc < 22.0:
        print('Medio')
    else:
        print('Alto')