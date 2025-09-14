import random
import data as data
import re
import datetime

negrita = '\033[1m'
color_tabla_par = '\033[37;44m'
color_tabla_inpar = '\033[34;46m'
terminar_color = '\033[0m'
descripcion_columnas_categorias = ["ID", "CATEGORIA_NOMBRE"]
descripcion_columnas_productos = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO", "STATUS"]
descripcion_columnas_proveedores = ["ID", "Nombre", "Venta mínima", "Plazo de entrega(dias)", "CUIT", "Status"]

def buscar_id(matriz, id_buscar, opcion):
    if opcion == 0:  # Si es productos
        for fila in matriz:
            if fila["id"] == id_buscar:
                return fila
    else:  # Si es proveedores o categorias
        for fila in matriz:
            if fila[0] == id_buscar:
                return fila
    return None

def mostrar_tabla(matriz, columnas, opcion, inactivos=1):
    if (opcion == 0):  # Si es productos
        claves_diccionario = list(matriz[1].keys())
        for i in claves_diccionario:
            print(f"{negrita}{color_tabla_par}|{i:<21}|{terminar_color}", end="")
        print()
        for fila in matriz:
            if inactivos == True:
                if fila["id"] % 2 == 0:
                    for i in fila:
                        print(f"{color_tabla_par}|{fila[i]:<21}|{terminar_color}", end="")
                else:
                    for i in fila:
                        print(f"{color_tabla_inpar}|{fila[i]:<21}|{terminar_color}", end="")
                print()
            elif fila[6] == True:
                if fila[0] % 2 == 0:
                    for i in fila:
                        print(f"{color_tabla_par}|{fila[i]:<21}|{terminar_color}", end="")
                else:
                    for i in fila:
                        print(f"{color_tabla_inpar}|{fila[i]:<21}|{terminar_color}", end="")
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
            elif inactivos == True:
                if fila[0] % 2 == 0:
                    for i in fila:
                        print(f"{color_tabla_par}|{i:<25}|{terminar_color}", end="")
                else:
                    for i in fila:
                        print(f"{color_tabla_inpar}|{i:<25}|{terminar_color}", end="")
                print()
        print()
    else:  # Si es stock o categorias
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


def desactivar_registro(matriz, id_desactivar, opcion):
    fila = buscar_id(matriz, id_desactivar, opcion)
    if fila:
        fila["status"] = False
        print("Registro desactivado correctamente.")
    else:
        print("No se encontró el registro.")

def agregar_registro(matriz, columnas, opcion):
    if opcion == 0:  # Si es productos
        nuevo_producto = {}
        nuevo_producto["id"] = matriz[-1]["id"] + 1 if matriz else 1
        mostrar_tabla(data.categorias, descripcion_columnas_categorias, 2)
        categoria_producto = input("ingrese el ID de la categoria de producto es: (Escriba N si no es ninguna de las categorias listadas) ")
        if categoria_producto.upper() == "N":
            print("Debe agregar una categoría antes de agregar un producto.")
            return
        nuevo_producto["id_categoria"]=(int(categoria_producto))
        nombre_producto = input("Ingrese el nombre del producto: ")
        nuevo_producto["nombre"]=(nombre_producto)
        mostrar_tabla(data.proveedores, descripcion_columnas_proveedores, 1)
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        proveedor_id = buscar_proveedor(nombre_proveedor)
        if proveedor_id is None:
            print("Proveedor no encontrado.")
            return matriz
        nuevo_producto["id_proveedor"]=(proveedor_id)
        stock = int(input("Ingrese el stock: "))
        precio = float(input("Ingrese el precio: "))
        nuevo_producto["stock"]=(stock)
        nuevo_producto["precio"]=(precio)
        nuevo_producto["status"]=(True) #asumimos que es esta activo al agregarse, despues podriamos cambiarlo

        matriz.append(nuevo_producto)
        print(nuevo_producto)
        mostrar_tabla(matriz, columnas, opcion)
        print("Producto agregado correctamente.")
    elif opcion == 1:  # Si es proveedores
        nuevo_proveedor = [matriz[-1][0] + 1 if matriz else 1]
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        nuevo_proveedor.append(nombre_proveedor)
        venta_minima = int(input("Ingrese la venta mínima: "))
        nuevo_proveedor.append(venta_minima)
        plazo_entrega = int(input("Ingrese el plazo de entrega (días): "))
        nuevo_proveedor.append(plazo_entrega)
        cuit_proveedores = sorted([fila[4] for fila in matriz])
        while len(cuit_proveedores) != nuevo_proveedor[0]:
            print(len(cuit_proveedores))
            print(nuevo_proveedor[0])
            cuit = input("Ingrese el CUIT: ")
            patron = re.compile('\d{2}-\d{8}-\d')
            if patron.match(cuit):
                if cuit in cuit_proveedores:
                    print("El CUIT ya existe. Ingrese un CUIT único.")
                else:
                    cuit_proveedores.append(cuit)
                    nuevo_proveedor.append(cuit)
            else:
                print("El formato de CUIT es incorrecto. Debe ser XX-XXXXXXXX-X.")
        nuevo_proveedor.append(True)

        matriz.append(nuevo_proveedor)

        mostrar_tabla(matriz, columnas, opcion)
        print("Proveedor agregado correctamente.")
    elif opcion == 2:  # Si es categorias o stock
        nueva_categoria = [matriz[-1][0] + 1 if matriz else 1]
        nombre_categoria = input("Ingrese el nombre de la categoría: ") 
        nueva_categoria.append(nombre_categoria)
        matriz.append(nueva_categoria)
        mostrar_tabla(matriz, columnas, opcion)
        print("Categoría agregada correctamente.")




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
        producto = buscar_id(matriz, id_modificar, opcion)
        if producto:
            print("Producto encontrado:")
            print(producto)
            opcion_modificar = int(input("Qué desea modificar? 1-Nombre del producto | 2-Nombre del proveedor | 3-Stock | 4-Precio: "))
            if opcion_modificar == 1:
                nombre_producto = input("Ingrese el nuevo nombre del producto: ")
                producto["nombre"] = nombre_producto
            elif opcion_modificar == 2:
                nombre_proveedor = input("Ingrese el nuevo nombre del proveedor: ")
                producto["id_proveedor"] = nombre_proveedor
            elif opcion_modificar == 3:
                opcion_stock = input("Esta 1-Ingresando stock o 2-Retirando stock?: ")
                if opcion_stock == "1":
                    stock = int(input("Ingrese la cantidad a ingresar: "))
                    producto["stock"] += stock
                    movimiento_stock(0, stock, producto["nombre"])  # Registro de movimiento de ingreso
                elif opcion_stock == "2":
                    stock = int(input("Ingrese la cantidad a retirar: "))
                    producto["stock"] -= stock
                    movimiento_stock(1, stock, producto[2])  # Registro de movimiento de egreso
            elif opcion_modificar == 4:
                precio = float(input("Ingrese el nuevo precio: "))
                producto["precio"] = precio
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