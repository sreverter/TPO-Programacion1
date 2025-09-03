import data
import funciones as f

descripcion_columnas = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO", "ACTIVO"]
productos = data.productos

def menu_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        opcion = input("1: Ver | 2: Buscar | 3: Agregar | 4: Desactivar | 5: Salir\nOpción: ")

        if opcion == "1":
            f.mostrar_tabla(productos, descripcion_columnas)
            orden_por_precio = input("¿Desea ordenar por precio? (s/n): ").lower()
            if orden_por_precio == "s":
                ascendente = input("Quiere que sea de menor a mayor? (s/n)")
                if ascendente == "s":
                    productos.sort(key=lambda x: x[5])
                else:
                    productos.sort(key=lambda x: x[5], reverse=True) 
                f.mostrar_tabla(productos, descripcion_columnas)
        elif opcion == "2":
            id_buscar = int(input("Ingrese ID: "))
            print(f.buscar_id(productos, id_buscar))
        elif opcion == "3":
            f.agregar_registro(productos, descripcion_columnas)
        elif opcion == "4":
            id_eliminar = int(input("Ingrese ID: "))
            f.desactivar_registro(productos, id_eliminar)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
