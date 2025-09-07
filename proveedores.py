import data
import funciones as f

descripcion_columnas = ["ID", "NOMBRE", "VENTA_MINIMA", "PLAZO_ENTREGA", "CUIT", "ACTIVO"]
proveedores = data.proveedores

def menu_proveedores():

    proveedor = 1
    while True:
        print("\n--- Gestión de Proveedores ---")
        opcion = input("1: Ver | 2: Buscar | 3: Agregar | 4: Modificar | 5: Salir\nOpción: ")

        if opcion == "1":
            f.mostrar_tabla(proveedores, descripcion_columnas)
        elif opcion == "2":
            print("Desea hacer una busqueda de un solo proveedor por ID o una busqueda parcial?")
            opcion_busqueda = int(input("Ingrese 1 para busqueda por ID o 2 para busqueda parcial: "))
            if opcion_busqueda == 1:
                id_buscar = int(input("Ingrese ID: "))
                print(f.buscar_id(proveedores, id_buscar))
            elif opcion_busqueda == 2:
                print(f.busqueda_proveedor_parcial())
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