print('BIENVENIDOS - INVENTARIO SUPERMERCADO')
productos = [
    #(id_producto, nombre, precio, cantidad_bodega)
    (41419, 'Fideos', 450, 210),
    (70717, 'Cuaderno', 900, 119),
    (78714, 'Jabon', 730, 708),
    (30877, 'Desodorante', 2190, 79),
    (47470, 'Yogur', 99, 832),
    (50809, 'Palta', 500, 55),
    (75466, 'Galletas', 235, 0),
    (33692, 'Bebida', 700, 20),
    (89148, 'Arroz', 900, 121),
    (66194, 'Lapiz', 120, 900),
    (15982, 'Vuvuzela', 12990, 40),
    (41235, 'Chocolate', 3099, 48),
]
itemes = [
    (1, 89148, 3),
    (2, 50809, 4),
    (2, 33692, 2),
    (2, 47470, 6),
    (3, 30877, 1),
    (4, 89148, 1),
    (4, 75466, 2),
    (5, 89148, 2),
    (5, 47470, 10),
    (6, 41419, 2),
]

def producto_mas_caro(productos):
    lista=[]
    for cod, nombre, precio, cant in productos:
        lista.append((precio, nombre))
    lista.sort()
    return lista[-1][1]

print("El Producto mas Caro es : ", producto_mas_caro(productos))


def valor_bodega(productos):
    valor = 0
    for cod, nombre, precio, cant in productos:
        valor += precio * cant
    return valor

print("El Valor total en Bodega es de", valor_bodega(productos), 'pesos')


def ingreso_total_ventas(itemes, productos):
    ingreso = 0
    for boleta, codigo, cantidad in itemes:
        for Id_producto, nombre, precio, cantidad_bodega in productos:
            if codigo == Id_producto:
                ingreso += precio * cantidad
    return ingreso

print("El Ingreso Total por ventas es de", ingreso_total_ventas(itemes,productos), 'pesos')
