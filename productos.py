import data
import funciones as f

descripcion_columnas = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO", "STATUS"]
productos = data.productos

def menu_productos():

    producto = 0
    titulo_sistema = " Gestión de Productos "
    screen = f'|{titulo_sistema:-^160}|'
    funciones = " 1: Ver | 2: Buscar | 3: Agregar | 4: Modificar | 5: Eliminar | 6: Volver "
    texto_opcion = "Opción:"
    texto_error = "Opción inválida. Intente nuevamente."
    color_inicio = '\033[37;44m'
    terminar_color = '\033[0m'
    negrita = '\033[1m'
    color_error = '\033[37;41m'
    ordenar = ""
    while True:
        print(f"{negrita}{color_inicio}{screen}{terminar_color}")
        print(f'{color_inicio}|{funciones:^160}|')
        opcion = input(f'|{texto_opcion:<160}|{terminar_color}\n')

        if opcion == "1":
            ver_inactivos = input("Desea ver los productos inactivos? (s/n): ")
            if ver_inactivos.lower() == "s":
                ver_inactivos = True
                f.mostrar_tabla(productos, descripcion_columnas, producto, ver_inactivos)
            else:
                ver_inactivos = False
                f.mostrar_tabla(productos, descripcion_columnas, producto, ver_inactivos)
            while ordenar != "4":
                ordenar = input("Desea ordenar la tabla por alguna columna? 1-Nombre de producto | 2-Precio | 3-Stock | 4-No: ")
                if ordenar == "1":
                    productos.sort(key=lambda x: x["nombre"])
                    f.mostrar_tabla(productos, descripcion_columnas, producto)
                elif ordenar == "2":
                    orden = ""
                    while orden != "1" and orden != "2":
                        orden = input("De menor a mayor (1) o mayor a menor (2): ")
                        if orden == "1":
                            producto_precio_menor = sorted(productos, key=lambda x: x["precio"])
                            f.mostrar_tabla(producto_precio_menor, descripcion_columnas, producto)
                        elif orden == "2":
                            productos_precio_mayor = sorted(productos, key=lambda x: x["precio"], reverse=True)
                            f.mostrar_tabla(productos_precio_mayor, descripcion_columnas, producto)
                        else:
                            print("Opción inválida. Intente nuevamente.")
                elif ordenar == "3":
                    orden = input("De menor a mayor (1) o mayor a menor (2): ")
                    if orden == "1":
                        productos.sort(key=lambda x: x["stock"])
                    elif orden == "2":
                        productos.sort(key=lambda x: x["stock"], reverse=True)
                    f.mostrar_tabla(productos, descripcion_columnas, producto)
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
            f.modificar_registro(productos, descripcion_columnas, producto)
        elif opcion == "5":
            id_eliminar = int(input("Ingrese ID: "))
            f.desactivar_registro(productos, id_eliminar)
        elif opcion == "6":
            break
        else:
            print(f'{color_error}{texto_error:<160}{terminar_color}')
