#programa que transforma temp de farenheit a Celsius
temp_i = float(input('Ingrese T° En Fahrenheit: '))
temp_f = (temp_i - 32) * (5/9)
print('La', temp_i, ' en grados Celsius son', round(temp_f,2))