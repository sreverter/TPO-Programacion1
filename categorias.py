import data
import funciones as scripts
# creo la entidad y la dejo vacia por si la llegamos a necesitar en un futuro

descripcion_columnas = ["ID", "CATEGORIA_NOMBRE"]
categorias = data.categorias

def menu_categorias():

    categoria = 2
    titulo_sistema = " Gestión de Categorias"
    screen = f'|{titulo_sistema:-^160}|'
    funciones = " 1: Ver | 2: Buscar | 3: Agregar | 4: Eliminar | 5: Volver "
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
            scripts.mostrar_tabla(categorias, descripcion_columnas, categoria)
        elif opcion == "2":
                scripts.mostrar_tabla(categorias, descripcion_columnas, categoria)
                id_buscar = int(input(f"{color_inicio}Ingrese ID: {terminar_color}"))
                resultado_busqueda_id = scripts.buscar_id(categorias, id_buscar, categoria)
                print(f"{color_inicio}La categoria que usted busco es: {resultado_busqueda_id[1]}")
        elif opcion == "3":
            scripts.agregar_registro(categorias, descripcion_columnas, categoria)
        elif opcion == "4":
            id_eliminar = int(input(f"{color_inicio}Ingrese ID: {terminar_color}"))
            scripts.desactivar_registro(categorias, id_eliminar, categoria)
        elif opcion == "5":
            break
        else:
            print(f'{color_error}{texto_error:<160}{terminar_color}')
