import funciones as f
import data as data

import productos
import proveedores
#import categorias
#import usuarios

def main():
    while True:
        print("\n--- Sistema de Inventario ---")
        opcion = input("1: Productos | 2: Proveedores | 3: Categorías | 4: Usuarios | 5: Salir\nOpción: ")

        if opcion == "1":
            productos.menu_productos()
        elif opcion == "2":
            proveedores.menu_proveedores()
        elif opcion == "3":
            print("Gestión de categorías aún no implementada.") #aca podriamos agregar una nueva categoria de productos
        elif opcion == "4":
            print("Sistema de usuarios aún no implementado.") #aca podriamos administrar a los usuarios (no se si es necesario, depende como lo implementemos)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()