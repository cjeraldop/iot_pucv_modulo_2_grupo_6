#Escriba un programa que transforme una temperatura ingresada por usuario de grados Farenheit(F) a Celsius (C), usando al siguiente fórmula: (F - 32) * 5/9

lectura_temp_farenheit = float(input("Ingrese la temperatura en Farenheit (F), que convertirá a Celsius (C): "))

transformacion_a_celsius = round((lectura_temp_farenheit - 32) * 5/9)

print("Los", lectura_temp_farenheit, " F en grados Celsius es igual a ", transformacion_a_celsius , " C.")