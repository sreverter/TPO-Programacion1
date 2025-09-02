import random
import data as data


def buscar_id(matriz, id_buscar):
    for fila in matriz:
        if fila[0] == id_buscar:
            return fila
    return None

def mostrar_tabla(matriz, columnas):
    print(columnas)
    for fila in matriz:
        print(fila)


def desactivar_registro(matriz, id_desactivar):
    fila = buscar_id(matriz, id_desactivar)
    if fila:
        fila[-1] = False
        print("Registro desactivado correctamente.")
        return True
    else:
        print("No se encontró el registro.")
        return False

def agregar_producto(matriz_productos):
    nuevo_producto = [matriz_productos[-1][0] + 1 if matriz_productos else 1]

    nombre_producto = input("Ingrese el nombre del producto: ")
    nuevo_producto.append(nombre_producto)
    nombre_proveedor = input("Ingrese el nombre del proveedor: ")
    proveedor_id = buscar_proveedor(nombre_proveedor)
    if proveedor_id is None:
        print("Proveedor no encontrado.")
        return matriz_productos
    nuevo_producto.append(proveedor_id)
    stock = int(input("Ingrese el stock: "))
    precio = float(input("Ingrese el precio: "))
    nuevo_producto.append(stock)
    nuevo_producto.append(precio)
    nuevo_producto.append(True) #asumimos que es esta activo al agregarse, despues podriamos cambiarlo

    matriz_productos.append(nuevo_producto)
    return matriz_productos


def buscar_proveedor(busqueda):
    proveedores = data.proveedores
    busqueda = busqueda.upper() #lo pongo en mayuscula asi no hay errores de comparacion

    for fila in proveedores:
        nombre_proveedor = fila[1].upper()
        if nombre_proveedor == busqueda:
            return fila[0]
    return None