import random
import data as data
import re


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

def agregar_registro(matriz_productos, columnas, opcion):
    if opcion == 0:  # Si es productos
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

        mostrar_tabla(matriz_productos, columnas)
        print("Producto agregado correctamente.")
    elif opcion == 1:  # Si es proveedores
        nuevo_proveedor = [matriz_productos[-1][0] + 1 if matriz_productos else 1]
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        nuevo_proveedor.append(nombre_proveedor)
        venta_minima = int(input("Ingrese la venta mínima: "))
        nuevo_proveedor.append(venta_minima)
        plazo_entrega = int(input("Ingrese el plazo de entrega (días): "))
        nuevo_proveedor.append(plazo_entrega)
        cuit = input("Ingrese el CUIT: ")
        nuevo_proveedor.append(cuit)
        nuevo_proveedor.append(True)

        matriz_productos.append(nuevo_proveedor)

        mostrar_tabla(matriz_productos, columnas)
        print("Proveedor agregado correctamente.")




def buscar_proveedor(busqueda):
    proveedores = data.proveedores
    busqueda = busqueda.upper() #lo pongo en mayuscula asi no hay errores de comparacion

    for fila in proveedores:
        nombre_proveedor = fila[1].upper()
        if nombre_proveedor == busqueda:
            return fila[0]
    return None

def busqueda_proveedor_parcial():
    proveedores = data.proveedores
    busqueda = input("Escriba la letra o las primeras 3 letras de los proveedores que desea buscar: ")
    patron = re.compile(busqueda, re.IGNORECASE)

    resultados = [fila for fila in proveedores if patron.search(fila[1])]
    if resultados != 0:
        print("Estos son los resultados encontrados para su búsqueda: \n")
        for fila in resultados:
            print(fila)
    else:
        print("No se encontraron resultados.")

    # return resultados
    # dejo comentada la ultima linea porque no se si queremos almacenar los resultados de la busqueda parcial. quizas es algo meramente informativo


def busqueda_productos_parcial():
    productos = data.productos
    busqueda = input("Escriba la letra o las primeras 3 letras de los productos que desea buscar: ")
    patron = re.compile(busqueda, re.IGNORECASE)

    resultados = [fila for fila in productos if patron.search(fila[2])]
    if resultados != 0:
        print("Estos son los resultados encontrados para su búsqueda: \n")
        for fila in resultados:
            print(fila)
    else:
        print("No se encontraron resultados.")

    # return resultados
    # dejo comentada la ultima linea porque no se si queremos almacenar los resultados de la busqueda parcial. quizas es algo meramente informativo
