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


def cantidad_de_artistas(dia):

    return len(artistas_por_dia[dia])

def nombre_primer_artista(dia):

    codigo = artistas_por_dia[dia][0]
    for nombre in artistas:
        if codigo in artistas[nombre]:
            return nombre

def pais_origen_ultimo(dia):

    codigo = artistas_por_dia[dia][-1]
    for nombre in artistas:
        codigo1 = artistas[nombre][0]
        if codigo == codigo1:
            return artistas[nombre][1]

def tiempo_total(dia):
    suma = 0
    codigos = artistas_por_dia[dia]
    for codigo in codigos:
        for nombre in artistas:
            if codigo in artistas[nombre]:
                suma += artistas[nombre][-1]
                return suma



dia = input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
print('El primer artista del dia sera', nombre_primer_artista(dia))
print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
print('Ese dia el concierto completo durara', tiempo_total(dia),'minutos')