import data
import funciones as scripts

descripcion_columnas = ["ID", "NOMBRE", "VENTA_MINIMA", "PLAZO_ENTREGA(dias)", "CUIT", "STATUS"]
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

        if type(opcion) != str:
            print(f"{color_error}Opción inválida. Intente nuevamente.{terminar_color}")

        if opcion == "1":
            ver_inactivos = input("Desea ver los productos inactivos? (s/n): ")
            if ver_inactivos.lower() == "s":
                ver_inactivos = True
                scripts.mostrar_tabla(proveedores, descripcion_columnas, proveedor, ver_inactivos)
            else:
                ver_inactivos = False
                scripts.mostrar_tabla(proveedores, descripcion_columnas, proveedor, ver_inactivos)
        elif opcion == "2":
            print(f"{color_inicio}Desea hacer una busqueda de un solo proveedor por ID o una busqueda parcial?")
            opcion_busqueda = input(f"Ingrese 1 para busqueda por ID o 2 para busqueda parcial: {terminar_color}")
            if opcion_busqueda.isdigit() == False:
                print(f"{color_error}Opción inválida. Intente nuevamente.{terminar_color}")
            if opcion_busqueda == "1":
                id_buscar = int(input("Ingrese ID: "))
                print(scripts.buscar_id(proveedores, id_buscar, proveedor))
            elif opcion_busqueda == "2":
                print(scripts.busqueda_proveedor_parcial())
        elif opcion == "3":
            scripts.agregar_registro(proveedores, descripcion_columnas, proveedor)
        elif opcion == "4":
            id_modificar = int(input("Ingrese ID: "))
            fila = scripts.buscar_id(proveedores, id_modificar, proveedor)
            if fila:
                for i in range(1, len(descripcion_columnas)):
                    fila[i] = input(f"Nuevo valor para {descripcion_columnas[i]} ({fila[i]}): ") or fila[i]
            else:
                print("Proveedor no encontrado.")
        elif opcion == "5":
            break
        else:
            print(f'{color_error}{texto_error:<160}{terminar_color}')