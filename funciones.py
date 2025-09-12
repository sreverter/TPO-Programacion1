import random
import data as data
import re
import datetime

negrita = '\033[1m'
color_tabla_par = '\033[37;44m'
color_tabla_inpar = '\033[34;46m'
terminar_color = '\033[0m'

def buscar_id(matriz, id_buscar):
    for fila in matriz:
        if fila[0] == id_buscar:
            return fila
    return None

def mostrar_tabla(matriz, columnas, opcion):
    if (opcion == 0):  # Si es productos
        for i in columnas:
            print(f"{negrita}{color_tabla_par}|{i:<21}|{terminar_color}", end="")
        print()
        for fila in matriz:
            if fila[6] == True:
                if fila[0] % 2 == 0:
                    for i in fila:
                        print(f"{color_tabla_par}|{i:<21}|{terminar_color}", end="")
                else:
                    for i in fila:
                        print(f"{color_tabla_inpar}|{i:<21}|{terminar_color}", end="")
                print()
        print()
    elif (opcion == 1):  # Si es proveedores
        for i in columnas:
            print(f"{negrita}{color_tabla_par}|{i:<25}|", end="")
        print()
        for fila in matriz:
            if fila[5] == True:
                if fila[0] % 2 == 0:
                    for i in fila:
                        print(f"{color_tabla_par}|{i:<25}|{terminar_color}", end="")
                else:
                    for i in fila:
                        print(f"{color_tabla_inpar}|{i:<25}|{terminar_color}", end="")
                print()
        print()
    else:  # Si es movimiento de stock
        for i in columnas:
            print(f"{negrita}{color_tabla_par}|{i:<25}|", end="")
        print()
        for fila in matriz:
            if fila[0] % 2 == 0:
                for i in fila:
                    print(f"{color_tabla_par}|{i:<25}|{terminar_color}", end="")
            else:
                for i in fila:
                    print(f"{color_tabla_inpar}|{i:<25}|{terminar_color}", end="")
            print()
        print()


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

        mostrar_tabla(matriz_productos, columnas, opcion)
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

        mostrar_tabla(matriz_productos, columnas, opcion)
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

def modificar_registro(matriz, columnas, opcion):
    if opcion == 0:  # Si es productos
        id_modificar = int(input("Ingrese el ID del producto a modificar: "))
        producto = buscar_id(matriz, id_modificar)
        if producto:
            print("Producto encontrado:")
            print(producto)
            opcion_modificar = int(input("Qué desea modificar? 1-Nombre del producto | 2-Nombre del proveedor | 3-Stock | 4-Precio: "))
            if opcion_modificar == 1:
                nombre_producto = input("Ingrese el nuevo nombre del producto: ")
                producto[2] = nombre_producto
            elif opcion_modificar == 2:
                nombre_proveedor = input("Ingrese el nuevo nombre del proveedor: ")
                producto[3] = nombre_proveedor
            elif opcion_modificar == 3:
                opcion_stock = input("Esta 1-Ingresando stock o 2-Retirando stock?: ")
                if opcion_stock == "1":
                    stock = int(input("Ingrese la cantidad a ingresar: "))
                    producto[4] += stock
                    movimiento_stock(0, stock, producto[2])  # Registro de movimiento de ingreso
                elif opcion_stock == "2":
                    stock = int(input("Ingrese la cantidad a retirar: "))
                    producto[4] -= stock
                    movimiento_stock(1, stock, producto[2])  # Registro de movimiento de egreso
            elif opcion_modificar == 4:
                precio = float(input("Ingrese el nuevo precio: "))
                producto[5] = precio
            mostrar_tabla(matriz, columnas, opcion)
            print("Producto modificado correctamente.")
        else:
            print("Producto no encontrado.")
    elif opcion == 1:  # Si es proveedores
        id_modificar = int(input("Ingrese el ID del proveedor a modificar: "))
        proveedor = buscar_id(matriz, id_modificar)
        if proveedor:
            print("Proveedor encontrado:")
            print(proveedor)
            nombre_proveedor = input("Ingrese el nuevo nombre del proveedor: ")
            proveedor[1] = nombre_proveedor
            venta_minima = int(input("Ingrese la nueva venta mínima: "))
            proveedor[2] = venta_minima
            plazo_entrega = int(input("Ingrese el nuevo plazo de entrega (días): "))
            proveedor[3] = plazo_entrega
            cuit = input("Ingrese el nuevo CUIT: ")
            proveedor[4] = cuit
            mostrar_tabla(matriz, columnas, opcion)
            print("Proveedor modificado correctamente.")
        else:
            print("Proveedor no encontrado.")
    return matriz

def movimiento_stock(opcion, stock, producto):
    descripcion_columnas = ["ID", "Tipo(Ingreso, Egreso)", "Producto", "cantidad", "fecha"]
    movimiento_stock = data.movimiento_stock
    id_movimiento = len(movimiento_stock) + 1
    if opcion == 0:  # Si es ingreso
        tipo_movimiento = "Ingreso"
        cantidad = stock
    elif opcion == 1:  # Si es egreso
        tipo_movimiento = "Egreso"
        cantidad = -stock
    fecha = datetime.date.today().strftime("%d-%m-%y")
    movimiento_stock.append((id_movimiento, tipo_movimiento, producto, cantidad, fecha))
    mostrar_tabla(movimiento_stock, descripcion_columnas, 2) 