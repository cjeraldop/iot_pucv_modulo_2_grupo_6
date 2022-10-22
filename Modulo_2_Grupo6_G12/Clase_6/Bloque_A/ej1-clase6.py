import os
# Replit necesita la ruta base completa
ruta_actual = os.path.dirname(os.path.abspath(__file__))

archivo= open(ruta_actual+"/quijote.txt")
i = 0 # Contador de lineas
letras = '' # String vacio para luego crear un string con todas las letras agrupadas
palabras = '' # String vacio para luego llenar con lineas como si fuera todo el archivo
for linea in archivo:
    letras += linea.strip().replace(' ','') # Aca creamos un string agrupado para contar las letras
    palabras += linea.strip() # Aca creamos un string normal, que luego contaremos las palabras con el metodo split
    i += 1
archivo.close()
print('Hay ', i ,'lineas en el archivo')
print('Hay ', len(letras), ' letras en el archivo')
print('Hay ', len(palabras.split(' ')), 'palabras en el archivo')





