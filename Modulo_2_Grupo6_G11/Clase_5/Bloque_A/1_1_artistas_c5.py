artistas = {
    # nombre: codigo, origen, duracion en minutos de la presentacion)
    'Marco Antonio Solis': (1, 'Estados Unidos', 74),
    'Daddy Yankee': (2, 'Puerto Rico', 70),
    'Myriam Hernandez': (3, 'Chile', 40),
    'Los Charros de Lumaco': (4, 'Chile', 25),
    'Metallica': (5, 'Estados Unidos', 45),
    'U2': (6, 'Irlanda', 80),
    'Justin Bieber': (7, 'Canada', 5),
}

artistas_por_dia = {
    # dia, orden de las presentaciones
    "Lunes": (1, 4, 3, 6, 2, 5),
    "Martes": (2, 5, 1),
    "Miercoles": (3, 6, 2, 4),
    "Jueves": (2, 5),
}

#INICIO FUNCIONES

def cantidad_de_artistas(dia):
  #cuerpo de la función
  return len(artistas_por_dia[dia])

def nombre_primer_artista(dia):
  #cuerpo de la función
  codigo_artista_encontrar = artistas_por_dia[dia][0]
  for artista in artistas.items():
    if (artista[1][0] == codigo_artista_encontrar):
      return artista[0]
  
def pais_origen_ultimo(dia):
  #cuerpo de la función
  codigo_artista_encontrar = artistas_por_dia[dia][-1]
  for artista in artistas.items():
    if (artista[1][0] == codigo_artista_encontrar):
      return artista[1][1]

def tiempo_total(dia):
  #cuerpo de la función
  tiempo_del_dia=0
  tupla_de_artistas = artistas_por_dia[dia]
  for codigo_artista in list(tupla_de_artistas): # convertir la tupla que contiene los codigos de los artistas a una lista iterable
    #print(codigo_artista)
    
    #Traer tiempo del artista por código:
    for artista in artistas.items():         #Recorrer la lista de artistas
      if (artista[1][0] == codigo_artista):   # comparar el codigo del artista del día con la lista de artistas
        tiempo = artista[1][2]               #Traer tiempo del artista
        tiempo_del_dia+=tiempo               #acumular el tiempo parcial del show del artista
  return tiempo_del_dia                       #retornar la duración total
#FIN FUNCIONES

dia = input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
print('El primer artista del dia sera', nombre_primer_artista(dia))
print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
print('Ese dia el concierto completo durara', tiempo_total(dia),'minutos')
