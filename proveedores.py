import data
import funciones as f

descripcion_columnas = ["ID", "NOMBRE", "VENTA_MINIMA", "PLAZO_ENTREGA", "CUIT", "ACTIVO"]
proveedores = data.proveedores

def menu_proveedores():

    proveedor = 1
    titulo_sistema = " Gestión de Proveedores "
    screen = f'|{titulo_sistema:-^160}|'
    funciones = " 1: Ver | 2: Buscar | 3: Agregar | 4: Modificar | 5: Salir "
    opcion = "Opción:"
    while True:
        print(f"{screen}")
        print(f'|{funciones:^160}|')
        opcion = input(f'|{opcion:<160}|\n')

        if opcion == "1":
            f.mostrar_tabla(proveedores, descripcion_columnas)
        elif opcion == "2":
            id_buscar = int(input("Ingrese ID: "))
            print(f.buscar_id(proveedores, id_buscar))
        elif opcion == "3":
            f.agregar_registro(proveedores, descripcion_columnas, proveedor)
        elif opcion == "4":
            id_modificar = int(input("Ingrese ID: "))
            fila = f.buscar_id(proveedores, id_modificar)
            if fila:
                for i in range(1, len(descripcion_columnas)):
                    fila[i] = input(f"Nuevo valor para {descripcion_columnas[i]} ({fila[i]}): ") or fila[i]
            else:
                print("Proveedor no encontrado.")
        elif opcion == "5":
            break