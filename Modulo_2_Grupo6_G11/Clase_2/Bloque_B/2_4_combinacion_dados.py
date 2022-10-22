#Un jugador debe lanzar dos dados numerados del 1 al 6, y su puntaje es la suma de
#los valores obtenidos.

#Un puntaje dado, puede ser obtenido con varias combinaciones posibles. Por
#ejemplo, el puntaje 4 se logra con 3 combinaciones;1+3, 2+2, 3+1

#Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado
#la cantidad de combinaciones con las que se puede obtener dicho puntaje.

puntaje = int(input("Ingrese el puntaje deseado:"))
dado1=1
contador_combinaciones=0
while dado1 <= 6:
  dado2=1
  while dado2 <= 6:
    if dado1+dado2 == puntaje:
      contador_combinaciones+=1
    dado2 += 1
  dado1 += 1
print("El puntaje:", puntaje, " se puede alcanzar con:", contador_combinaciones," combinaciones")