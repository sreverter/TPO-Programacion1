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
    {"id": 1, "id_categoria": 1, "nombre": "Leche entera 1L", "id_proveedor": 1, "stock": 500, "precio": 3000, "status": True},
    {"id": 2, "id_categoria": 2, "nombre": "Pechuga de pollo 1kg", "id_proveedor": 2, "stock": 200, "precio": 4500, "status": True},
    {"id": 3, "id_categoria": 3, "nombre": "Agua mineral 500ml", "id_proveedor": 3, "stock": 1000, "precio": 1500, "status": True},
    {"id": 4, "id_categoria": 4, "nombre": "Papas fritas 100g", "id_proveedor": 4, "stock": 350, "precio": 1500, "status": True},
    {"id": 5, "id_categoria": 5, "nombre": "Manzana roja 1kg", "id_proveedor": 5, "stock": 250, "precio": 2000, "status": True},
    {"id": 6, "id_categoria": 1, "nombre": "Yogur natural 200g", "id_proveedor": 6, "stock": 300, "precio": 1200, "status": True},
    {"id": 7, "id_categoria": 2, "nombre": "Carne vacuna 1kg", "id_proveedor": 7, "stock": 180, "precio": 6000, "status": False},
    {"id": 8, "id_categoria": 3, "nombre": "Jugo de naranja 1L", "id_proveedor": 8, "stock": 400, "precio": 2500, "status": True},
    {"id": 9, "id_categoria": 4, "nombre": "Galletitas saladas", "id_proveedor": 9, "stock": 500, "precio": 1700, "status": False},
    {"id": 10, "id_categoria": 5, "nombre": "Banana 1kg", "id_proveedor": 10, "stock": 220, "precio": 1800, "status": True},
    {"id": 11, "id_categoria": 1, "nombre": "Queso cremoso 500g", "id_proveedor": 1, "stock": 150, "precio": 3500, "status": True},
    {"id": 12, "id_categoria": 2, "nombre": "Chorizo 500g", "id_proveedor": 2, "stock": 100, "precio": 3200, "status": False},
    {"id": 13, "id_categoria": 3, "nombre": "Cerveza rubia 1L", "id_proveedor": 3, "stock": 250, "precio": 3500, "status": True},
    {"id": 14, "id_categoria": 4, "nombre": "Alfajor chocolate", "id_proveedor": 4, "stock": 600, "precio": 800, "status": True},
    {"id": 15, "id_categoria": 5, "nombre": "Tomate 1kg", "id_proveedor": 5, "stock": 300, "precio": 2200, "status": False}
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