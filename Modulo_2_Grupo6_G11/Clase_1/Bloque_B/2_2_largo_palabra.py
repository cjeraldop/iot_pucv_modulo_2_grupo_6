#Escriba un programa que pida al usuario dos palabras, e indique cual de ellas es la más larga, y por cuantas letras lo es.

# Función len() para obtener el largo --> https://www.w3schools.com/python/ref_func_len.asp#:~:text=The%20len()%20function%20returns,of%20characters%20in%20the%20string.

palabra1= input('Ingrese primera palabra: ')
palabra2= input('Ingrese segunda palabra: ')
largopalabra1 =len(palabra1)
largopalabra2 =len(palabra2)
diferencia_de_largo = abs(largopalabra1 - largopalabra2)
if largopalabra1 > largopalabra2:
  print("La primera palabra es la más larga")
elif largopalabra1 < largopalabra2:
  print("La segunda palabra es la más larga")
else:
  print("Las palabras tienen el mismo largo")

#print("La palabras difieren en ", diferencia_de_largo, " letras.")