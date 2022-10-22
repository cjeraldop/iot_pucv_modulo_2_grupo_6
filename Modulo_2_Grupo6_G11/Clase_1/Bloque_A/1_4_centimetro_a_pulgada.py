#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
medida_en_centimetros = float(input("Ingrese la medida en centímetros, que desea convertir a pulgadas: "))
medida_en_pulgadas = round (medida_en_centimetros / 2.54, 4)
print(medida_en_centimetros, "cm es igual a ", medida_en_pulgadas , "in.")