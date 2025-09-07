import data
import funciones as f

descripcion_columnas = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO", "ACTIVO"]
productos = data.productos

def menu_productos():

    producto = 0
    titulo_sistema = " Gestión de Productos "
    screen = f'|{titulo_sistema:-^160}|'
    funciones = " 1: Ver | 2: Buscar | 3: Agregar | 4: Modificar | 5: Salir "
    opcion = "Opción:"
    while True:
        print(f"{screen}")
        print(f'|{funciones:^160}|')
        opcion = input(f'|{opcion:<160}|\n')

        if opcion == "1":
            f.mostrar_tabla(productos, descripcion_columnas)
        elif opcion == "2":
            id_buscar = int(input("Ingrese ID: "))
            print(f.buscar_id(productos, id_buscar))
        elif opcion == "3":
            f.agregar_registro(productos, descripcion_columnas, producto)
        elif opcion == "4":
            id_eliminar = int(input("Ingrese ID: "))
            f.desactivar_registro(productos, id_eliminar)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
