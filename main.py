import funciones as scripts  # ← Corregido el nombre
import archivo as data

import productos
import proveedores
import categorias

def main():
    titulo_sistema = " Sistema de Inventario "
    screen = f'|{titulo_sistema:-^160}|'
    funciones = " 1: Productos | 2: Proveedores | 3: Categorías | 4: Estadisticas Generales | 5: Salir"
    texto_opcion = "Opción:"
    texto_error = "Opción inválida. Intente nuevamente."
    texto_salida = "Saliendo..."
    color_inicio = '\033[37;44m'
    negrita = '\033[1m'
    terminar_color = '\033[0m'
    color_error = '\033[37;41m'
    
    while True:
        print(f'{negrita}{color_inicio}{screen}{terminar_color}')
        print(f'{color_inicio}|{funciones:^160}|')
        opcion = input(f'|{texto_opcion:<160}|{terminar_color}\n')
        
        if opcion == "1":
            productos.menu_productos()
        elif opcion == "2":
            proveedores.menu_proveedores()
        elif opcion == "3":
            categorias.menu_categorias()
        elif opcion == "4":
            scripts.estadisticas()
        elif opcion == "5":
            print(f"{color_inicio}{texto_salida:<160}{terminar_color}")
            break
        else:
            print(f'{color_error}{texto_error:<160}{terminar_color}')

if __name__ == "__main__":
    main()