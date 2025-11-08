import archivo as data
import funciones as scripts

descripcion_columnas = ["ID", "NOMBRE", "VENTA_MINIMA", "PLAZO_ENTREGA(dias)", "CUIT", "STATUS"]

def menu_proveedores():
    proveedores = data.cargar_proveedores()
    proveedor = 1
    titulo_sistema = " Gestión de Proveedores "
    screen = f'|{titulo_sistema:-^160}|'
    funciones = " 1: Ver | 2: Buscar | 3: Agregar | 4: Modificar | 5:Eliminar | 6: Volver "
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
            ver_inactivos = input(f"{color_inicio}Desea ver los proveedores inactivos? (s/n): {terminar_color}")
            if ver_inactivos.lower() == "s":
                scripts.mostrar_tabla(proveedores, descripcion_columnas, proveedor, True)
            else:
                scripts.mostrar_tabla(proveedores, descripcion_columnas, proveedor, False)
        elif opcion == "2":
            print(f"{color_inicio}Desea hacer una busqueda de un solo proveedor por ID o una busqueda por primeras letras?{terminar_color}")
            opcion_busqueda = input(f"{color_inicio}Ingrese 1 para busqueda por ID o 2 para busqueda por letras: {terminar_color}")
            if opcion_busqueda == "1":
                id_buscar = int(input(f"{color_inicio}Ingrese ID: {terminar_color}"))
                resultado_busqueda_id = scripts.buscar_id(proveedores, id_buscar, proveedor)
                if resultado_busqueda_id:
                    print(f"{color_inicio}El proveedor de ID {id_buscar} es: {resultado_busqueda_id['nombre']}, este tiene una venta mínima de {resultado_busqueda_id['productos_sum']} unidades y un plazo de entrega de {resultado_busqueda_id['tiempo_entrega']} días.{terminar_color}")
                else:
                    print(f"{color_inicio}Proveedor no encontrado.{terminar_color}")
            elif opcion_busqueda == "2":
                scripts.busqueda_proveedor_parcial()
            else:
                print(f"{color_error}Opción inválida. Intente nuevamente.{terminar_color}")
        elif opcion == "3":
            scripts.agregar_registro(proveedores, descripcion_columnas, proveedor)
            data.guardar_proveedores(proveedores)
        elif opcion == "4":
            scripts.modificar_registro(proveedores, descripcion_columnas, proveedor)
            data.guardar_proveedores(proveedores)
        elif opcion == "5":
            id_eliminar = int(input(f"{color_inicio}Ingrese ID: {terminar_color}"))
            scripts.desactivar_registro(proveedores, id_eliminar, proveedor)
            data.guardar_proveedores(proveedores)
        elif opcion == "6":
            break
        else:
            print(f'{color_error}{texto_error:<160}{terminar_color}')