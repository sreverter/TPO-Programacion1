import data as data
import funciones as f

#guzmangustavo@outlook.com

data_productos = data.productos
descripcion_columnas = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO"]
que_hacer = ""
while que_hacer != "5":
    que_hacer = input("¿Qué desea hacer?\n(1: Ver productos, 2: Buscar producto, 3: Agregar producto, 4: Eliminar producto, 5: Salir):\n")
    if que_hacer == "1":
        print(descripcion_columnas)
        for fila in data_productos:
            print(fila)
    elif que_hacer == "2":
        id_buscar = int(input("Ingrese el ID del producto a buscar: "))
        producto_encontrado = f.buscar_id(data_productos, id_buscar)
        if producto_encontrado:
            print("Producto encontrado:", producto_encontrado)
        else:
            print("Producto no encontrado.")
    elif que_hacer == "3":
        data_productos = f.agregar_producto(data_productos)
        print("Producto agregado exitosamente.")
        print(descripcion_columnas)
        for fila in data_productos:
            print(fila)
    elif que_hacer == "4":
        id_producto_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
        producto_a_eliminar = f.buscar_id(data_productos, id_producto_eliminar)
        if producto_a_eliminar:
            data_productos.remove(producto_a_eliminar)
            print(f"Producto con ID {id_producto_eliminar} eliminado.")
            print(descripcion_columnas)
            for fila in data_productos:
                print(fila)
    else:
        print("Saliendo del programa.")


