import data
import funciones as f

descripcion_columnas = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO", "ACTIVO"]
productos = data.productos

def menu_productos():

    producto = 0
    while True:
        print("\n--- Gestión de Productos ---")
        opcion = input("1: Ver | 2: Buscar | 3: Agregar | 4: Desactivar | 5: Salir\nOpción: ")

        if opcion == "1":
            f.mostrar_tabla(productos, descripcion_columnas)
        elif opcion == "2":
            print("Desea hacer una busqueda de un solo producto por ID o una busqueda parcial?")
            opcion_busqueda = int(input("Ingrese 1 para busqueda por ID o 2 para busqueda parcial: "))
            if opcion_busqueda == 1:
                id_buscar = int(input("Ingrese ID: "))
                print(f.buscar_id(productos, id_buscar))
            elif opcion_busqueda == 2:
                print(f.busqueda_productos_parcial())
        elif opcion == "3":
            f.agregar_registro(productos, descripcion_columnas, producto)
        elif opcion == "4":
            id_eliminar = int(input("Ingrese ID: "))
            f.desactivar_registro(productos, id_eliminar)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
