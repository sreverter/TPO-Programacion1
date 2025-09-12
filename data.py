proveedores = [
    [1, "Distribuidora Sur", 100, 7, "20-12345678-3", True],
    [2, "Comercial Norte", 50, 5, "23-23456789-1", True],
    [3, "Mayorista Express", 200, 10, "27-34567890-4", False],
    [4, "Central Proveeduría", 150, 12, "20-45678901-2", True],
    [5, "Global Import", 80, 15, "23-56789012-7", True],
    [6, "Mercado Federal", 120, 8, "27-67890123-5", True],
    [7, "Alimentos del Centro", 90, 6, "20-78901234-8", True],
    [8, "Distribuidora Andina", 300, 20, "23-89012345-6", True],
    [9, "Proveeduría Pampeana", 110, 9, "27-90123456-1", False],
    [10, "Comercial Atlántico", 70, 4, "20-11223344-0", False]
]


categorias = [
    [1, "Lácteos"],
    [2, "Carnes"],
    [3, "Bebidas"],
    [4, "Snacks"],
    [5, "Frutas y Verduras"]
]

# Referencia de productos
#ID, ID_CATEGORIA, NOMBRE, ID_PROVEEDOR, STOCK, PRECIO, status (activo/inactivo)
productos = [
    [1, 1, "Leche entera 1L", 1, 500, 3000, True],
    [2, 2, "Pechuga de pollo 1kg", 2, 200, 4500, True],
    [3, 3, "Agua mineral 500ml", 3, 1000, 1500, True],
    [4, 4, "Papas fritas 100g", 4, 350, 1500, True],
    [5, 5, "Manzana roja 1kg", 5, 250, 2000, True],
    [6, 1, "Yogur natural 200g", 6, 300, 1200, True],
    [7, 2, "Carne vacuna 1kg", 7, 180, 6000, False],
    [8, 3, "Jugo de naranja 1L", 8, 400, 2500, True],
    [9, 4, "Galletitas saladas 150g", 9, 500, 1700, False],
    [10, 5, "Banana 1kg", 10, 220, 1800, True],
    [11, 1, "Queso cremoso 500g", 1, 150, 3500, True],
    [12, 2, "Chorizo 500g", 2, 100, 3200, False],
    [13, 3, "Cerveza rubia 1L", 3, 250, 3500, True],
    [14, 4, "Alfajor chocolate", 4, 600, 800, True],
    [15, 5, "Tomate 1kg", 5, 300, 2200, False]
]

# usuarios hardcodeados
usuarios = [
    [1, "admin", "1234", "admin"],
    [2, "empleado1", "abcd", "empleado"],
    [3, "empleado2", "5678", "empleado"]
]

# #Agregar tabla de pedidos a proveedores. (Id de proveedor, id de producto, precio, tiempo de entrega, cantidad)
# pedidos_proveedores = [
#     [1, 1, 1.15, 5, 100],
#     [2, 2, 4.40, 7, 50],
#     [3, 3, 0.75, 3, 200],
#     [4, 4, 1.45, 6, 150],
#     [5, 5, 2.10, 8, 80]
# ]

# #tabla de inventario (id de producto, cantidad, punto de pedido)

# inventario = [
#     [1, 500, 100],
#     [2, 200, 50],
#     [3, 1000, 200],
#     [4, 350, 75],
#     [5, 250, 60]
# ]

#movimiento de stock (id, tipo (ingreso, egreso), producto, cantidad, fecha)
movimiento_stock = [
    (1, "ingreso", "Leche entera 1L", 100, "01-01-25"),
    (2, "egreso", "Pechuga de pollo 1kg", 50, "02-01-25"),
    (3, "ingreso", "Agua mineral 500ml", 200, "03-01-25"),
    (4, "egreso", "Papas fritas 100g", 150, "04-01-25"),
    (5, "ingreso", "Manzana roja 1kg", 80, "05-01-25")
]