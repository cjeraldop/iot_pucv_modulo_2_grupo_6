import os
# Replit necesita la ruta base completa
ruta_actual = os.path.dirname(os.path.abspath(__file__))

archivo= open(ruta_actual+"/quijote.txt")
letras=0
palabras=0
contadorlineas=0
for linea in archivo:
    linea= linea.strip()
    espacios= linea.count(" ")
    #print("caracteres con espacios", len(linea))
    caracteres=len(linea)-espacios
    #print("hay ", caracteres , "letras")
    #print(linea)
    letras=letras+caracteres
    palabras=palabras+espacios+1
    contadorlineas=contadorlineas+1

print("el texto tiene", letras, "letras")
print("el texto tiene", palabras , "palabras")
print("el texto tiene", contadorlineas , "lineas")