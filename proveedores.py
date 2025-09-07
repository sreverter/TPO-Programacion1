import data
import funciones as f

descripcion_columnas = ["ID", "NOMBRE", "VENTA_MINIMA", "PLAZO_ENTREGA(dias)", "CUIT", "ACTIVO"]
proveedores = data.proveedores

def menu_proveedores():

    proveedor = 1
    titulo_sistema = " Gestión de Proveedores "
    screen = f'|{titulo_sistema:-^160}|'
    funciones = " 1: Ver | 2: Buscar | 3: Agregar | 4: Modificar | 5: Salir "
    texto_opcion = "Opción:"
    texto_error = "Opción inválida. Intente nuevamente."
    color_inicio = '\033[37;44m'
    terminar_color = '\033[0m'
    negrita = '\033[1m'
    color_error = '\033[37;41m'
    while True:
        print(f"{negrita}{color_inicio}{screen}{terminar_color}")
        print(f'{color_inicio}|{funciones:^160}|')
        opcion = input(f'|{texto_opcion:<160}|{terminar_color}\n')

        if opcion == "1":
            f.mostrar_tabla(proveedores, descripcion_columnas, proveedor)
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
        else:
            print(f'{color_error}{texto_error:<160}{terminar_color}')