import random
import data as data
import re
import datetime

negrita = '\033[1m'
color_tabla_par = '\033[37;44m'
color_tabla_impar = '\033[34;46m'
terminar_color = '\033[0m'
descripcion_columnas_categorias = ["ID", "CATEGORIA_NOMBRE"]
descripcion_columnas_productos = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO", "STATUS"]
descripcion_columnas_proveedores = ["ID", "Nombre", "Venta mínima", "Plazo de entrega(dias)", "CUIT", "Status"]

def buscar_id(matriz, id_buscar):

    for fila in matriz:
        try:
            if fila["id"] == id_buscar:
                return fila
        except (KeyError, TypeError):
            # Si no tiene clave "id" o hay error de tipo, continuamos
            continue
                
    return None

def mostrar_tabla(matriz, columnas, opcion, inactivos=1): #Esta funcion se utiliza para imprimir todas las tablas del programa
    # if opcion == 0:
    #     tabla_entidad_desactivada = list(filter(lambda x: x["status"] == False, matriz))
    # elif opcion == 1:
    #     tabla_entidad_desactivada = list(filter(lambda x: x[5] == False, matriz)) 
    if (opcion == 0):  # Si es productos
        claves_diccionario = list(matriz[1].keys())
        for i in claves_diccionario:
            print(f"{negrita}{color_tabla_par}|{i:<21}|{terminar_color}", end="")
        print()
        for fila in matriz:
            if inactivos == True:
                if fila["id"] % 2 == 0:
                    for i in fila:
                        if i == "id_categoria" or i == "id_proveedor" or i == "status":
                            id_relacionado = fila[i]
                            if i == "id_categoria":
                                categoria = buscar_id(data.categorias, id_relacionado, 2)
                                print(f"{color_tabla_par}|{categoria[1]:<21}|{terminar_color}", end="")
                            elif i == "id_proveedor":
                                proveedor = buscar_id(data.proveedores, id_relacionado, 1)
                                print(f"{color_tabla_par}|{proveedor[1]:<21}|{terminar_color}", end="")
                            elif i == "status":
                                if fila["status"] == True:
                                    print(f"{color_tabla_par}|{'Activo':<21}|{terminar_color}", end="")
                                else:
                                    print(f"{color_tabla_par}|{'Inactivo':<21}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_par}|{fila[i]:<21}|{terminar_color}", end="")
                else:
                    for i in fila:
                        if i == "id_categoria" or i == "id_proveedor" or i == "status":
                            id_relacionado = fila[i]
                            if i == "id_categoria":
                                categoria = buscar_id(data.categorias, id_relacionado, 2)
                                print(f"{color_tabla_impar}|{categoria[1]:<21}|{terminar_color}", end="")
                            elif i == "id_proveedor":
                                proveedor = buscar_id(data.proveedores, id_relacionado, 1)
                                print(f"{color_tabla_impar}|{proveedor[1]:<21}|{terminar_color}", end="")
                            elif i == "status":
                                if fila["status"] == True:
                                    print(f"{color_tabla_impar}|{'Activo':<21}|{terminar_color}", end="")
                                else:
                                    print(f"{color_tabla_impar}|{'Inactivo':<21}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_impar}|{fila[i]:<21}|{terminar_color}", end="")
                print()
            elif fila["status"] == True:
                if fila["id"] % 2 == 0:
                    for i in fila:
                        if i == "id_categoria" or i == "id_proveedor" or i == "status":
                            id_relacionado = fila[i]
                            if i == "id_categoria":
                                categoria = buscar_id(data.categorias, id_relacionado, 2)
                                print(f"{color_tabla_par}|{categoria[1]:<21}|{terminar_color}", end="")
                            elif i == "id_proveedor":
                                proveedor = buscar_id(data.proveedores, id_relacionado, 1)
                                print(f"{color_tabla_par}|{proveedor[1]:<21}|{terminar_color}", end="")
                            elif i == "status":
                                print(f"{color_tabla_par}|{'Activo':<21}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_par}|{fila[i]:<21}|{terminar_color}", end="")
                else:
                    for i in fila:
                        if i == "id_categoria" or i == "id_proveedor" or i == "status":
                            id_relacionado = fila[i]
                            if i == "id_categoria":
                                categoria = buscar_id(data.categorias, id_relacionado, 2)
                                print(f"{color_tabla_impar}|{categoria[1]:<21}|{terminar_color}", end="")
                            elif i == "id_proveedor":
                                proveedor = buscar_id(data.proveedores, id_relacionado, 1)
                                print(f"{color_tabla_impar}|{proveedor[1]:<21}|{terminar_color}", end="")
                            elif i == "status":
                                print(f"{color_tabla_impar}|{'Activo':<21}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_impar}|{fila[i]:<21}|{terminar_color}", end="")
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
                        if i is True:
                            print(f"{color_tabla_par}|{'Activo':<25}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_par}|{i:<25}|{terminar_color}", end="")
                else:
                    for i in fila:
                        if i is True:
                            print(f"{color_tabla_impar}|{'Activo':<25}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_impar}|{i:<25}|{terminar_color}", end="")
                print()
            elif inactivos == True:
                if fila[0] % 2 == 0:
                    for i in fila:
                        if i is False:
                            print(f"{color_tabla_par}|{'Inactivo':<25}|{terminar_color}", end="")
                        elif i is True:
                            print(f"{color_tabla_par}|{'Activo':<25}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_par}|{i:<25}|{terminar_color}", end="")
                else:
                    for i in fila:
                        if i is False:
                            print(f"{color_tabla_impar}|{'Inactivo':<25}|{terminar_color}", end="")
                        elif i is True:
                            print(f"{color_tabla_impar}|{'Activo':<25}|{terminar_color}", end="")
                        else:
                            print(f"{color_tabla_impar}|{i:<25}|{terminar_color}", end="")
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
                    print(f"{color_tabla_impar}|{i:<25}|{terminar_color}", end="")
            print()
        print()


def desactivar_registro(matriz, id_desactivar, opcion): #Esta funcion se utiliza para desactivar un registro
    fila = buscar_id(matriz, id_desactivar, opcion)
    if opcion == 0:  # Si es productos
        if fila:
            fila["status"] = False
            print("Registro desactivado correctamente.")
        else:
            print("No se encontró el registro.")
    elif opcion == 1:  # Si es proveedores
        if fila:
            fila[5] = False
            print("Registro desactivado correctamente.")
        else:
            print("No se encontró el registro.")
    else:
        if fila:
            matriz.remove(fila)
            print("Registro eliminado correctamente.")

def agregar_registro(matriz, columnas, opcion): #Esta funcion se utiliza para agregar un registro y segun si es producto o proveedor/categoria cambia el tipo
    if opcion == 0:  # Si es productos
        nuevo_producto = {}
        nuevo_producto_id = matriz[-1]["id"] + 1 if matriz else 1
        mostrar_tabla(data.categorias, descripcion_columnas_categorias, 2)
        categoria_producto = input(f"{color_tabla_par}ingrese el ID de la categoria de producto es: (Escriba N si no es ninguna de las categorias listadas) ")
        if categoria_producto.upper() == "N":
            print("Debe agregar una categoría antes de agregar un producto.")
            return
        nombre_producto = input("Ingrese el nombre del producto: ")
        mostrar_tabla(data.proveedores, descripcion_columnas_proveedores, 1)
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        proveedor_id = buscar_proveedor(nombre_proveedor)
        if proveedor_id is None:
            print("Proveedor no encontrado.")
            return matriz
        stock = int(input("Ingrese el stock: "))
        precio = float(input("Ingrese el precio: "))
        nuevo_producto = {
            'id' : nuevo_producto_id,
            "id_categoria" : int(categoria_producto),
            "nombre" : nombre_producto,
            "id_proveedor" : proveedor_id,
            "stock" : stock,
            "precio" : precio,
            "status" : True
        }
        print(nuevo_producto)
        matriz.append(nuevo_producto)
        print(nuevo_producto)
        mostrar_tabla(matriz, columnas, opcion)
        print(f"Producto agregado correctamente.{terminar_color}")
    elif opcion == 1:  # Si es proveedores
        nuevo_proveedor = [matriz[-1][0] + 1 if matriz else 1]
        nombre_proveedor = input(f"{color_tabla_par}Ingrese el nombre del proveedor: ")
        nuevo_proveedor.append(nombre_proveedor)
        venta_minima = int(input("Ingrese la venta mínima: "))
        nuevo_proveedor.append(venta_minima)
        plazo_entrega = int(input("Ingrese el plazo de entrega (días): "))
        nuevo_proveedor.append(plazo_entrega)
        cuit_proveedores = sorted([fila[4] for fila in matriz])
        while len(cuit_proveedores) != nuevo_proveedor[0]:
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
        print(f"Proveedor agregado correctamente.{terminar_color}")
    elif opcion == 2:  # Si es categorias
        nueva_categoria = [matriz[-1][0] + 1 if matriz else 1]
        nombres_categorias = []
        for i in data.categorias:
            nombres_categorias.append(i[1])
        conjunto_categorias = set(nombres_categorias)
        nombre_categoria = input(f"{color_tabla_par}Ingrese el nombre de la categoría: ") 
        while nombre_categoria.capitalize() in conjunto_categorias:
            print("La categoría ya existe. Ingrese un nombre único.")
            nombre_categoria = input("Ingrese el nombre de la categoría: ")
        nueva_categoria.append(nombre_categoria.capitalize())
        matriz.append(nueva_categoria)
        mostrar_tabla(matriz, columnas, opcion)
        print(f"Categoría agregada correctamente.{terminar_color}")




def buscar_proveedor(busqueda): #esta funcion busca un proveedor teniendo en cuenta su nombre
    proveedores = data.proveedores
    busqueda = busqueda.upper() #lo pongo en mayuscula asi no hay errores de comparacion

    for fila in proveedores:
        nombre_proveedor = fila[1].upper()
        if nombre_proveedor == busqueda:
            return fila[0]
    return None

def busqueda_proveedor_parcial(): #Esta funcion busca un proveedor por su nombre segun sus primeras letras
    proveedores = data.proveedores
    busqueda = input(f"{color_tabla_par}Escriba la letra o las primeras 3 letras de los proveedores que desea buscar: ")
    patron = re.compile(busqueda, re.IGNORECASE)

    resultados = [fila for fila in proveedores if patron.search(fila[1])]
    if resultados != 0:
        print(f"Estos son los resultados encontrados para su búsqueda: \n{terminar_color}")
        for fila in resultados:
            print(f"{color_tabla_par}-Nombre {fila[1]} - Entrega minima: {fila[2]} unidades - Plazo de entrega: {fila[3]} dias{terminar_color}")
    else:
        print(f"{color_tabla_par}No se encontraron resultados.{terminar_color}")

    # return resultados
    # dejo comentada la ultima linea porque no se si queremos almacenar los resultados de la busqueda parcial. quizas es algo meramente informativo


def busqueda_productos_parcial(): #Esta funcion busca un producto por su nombre segun sus primeras letras
    productos = data.productos
    busqueda = input(f"{color_tabla_par}Escriba la letra o las primeras 3 letras de los productos que desea buscar: ")
    patron = re.compile(busqueda, re.IGNORECASE)

    resultados = [fila for fila in productos if patron.search(fila["nombre"])]
    if resultados != 0:
        print(f"Estos son los resultados encontrados para su búsqueda: \n{terminar_color}")
        for fila in resultados:
            print(f"{color_tabla_par}-Nombre {fila["nombre"]} - Stock: {fila["stock"]} unidades - Precio: {fila["precio"]} pesos{terminar_color}")
    else:
        print(f"{color_tabla_par}No se encontraron resultados.{terminar_color}")

    # return resultados
    # dejo comentada la ultima linea porque no se si queremos almacenar los resultados de la busqueda parcial. quizas es algo meramente informativo

def modificar_registro(matriz, columnas, opcion): #esta funcion permite modificar un registro, tanto de categoria, como de proveedores y producto
    if opcion == 0:  # Si es productos
        mostrar_tabla(matriz, columnas, opcion)
        id_modificar = int(input(f"{color_tabla_par}Ingrese el ID del producto a modificar: {terminar_color}"))
        producto = buscar_id(matriz, id_modificar, opcion)
        if producto:
            print(f"{color_tabla_par}Producto encontrado:{terminar_color}")
            distribuidor = buscar_id(data.proveedores, producto["id_proveedor"], 1)
            print(f"{color_tabla_par}El producto es {producto["nombre"]}, del distribuidor {distribuidor[1]}, tiene un stock de {producto["stock"]} unidades y un precio de {producto["precio"]} pesos{terminar_color}")
            opcion_modificar = int(input(f"{color_tabla_par}Qué desea modificar? 1-Nombre del producto | 2-Nombre del proveedor | 3-Stock | 4-Precio: {terminar_color}"))
            if opcion_modificar == 1:
                nombre_producto = input(f"{color_tabla_par}Ingrese el nuevo nombre del producto: {terminar_color}")
                producto["nombre"] = nombre_producto
            elif opcion_modificar == 2:
                nombre_proveedor = input(f"{color_tabla_par}Ingrese el nuevo nombre del proveedor: {terminar_color}")
                producto["id_proveedor"] = nombre_proveedor
            elif opcion_modificar == 3:
                opcion_stock = input(f"{color_tabla_par}Esta 1-Ingresando stock o 2-Retirando stock?: {terminar_color}")
                if opcion_stock == "1":
                    stock = int(input(f"{color_tabla_par}Ingrese la cantidad a ingresar: {terminar_color}"))
                    producto["stock"] += stock
                    movimiento_stock(0, stock, producto["nombre"])  # Registro de movimiento de ingreso
                    calcular_tiempo = calcular_tiempo_pedido(buscar_id(data.proveedores, producto["id_proveedor"], 1)[3])
                    print(f"{color_tabla_par}El producto se pidio el día {calcular_tiempo}{terminar_color}")
                elif opcion_stock == "2":
                    stock = int(input(f"{color_tabla_par}Ingrese la cantidad a retirar: {terminar_color}"))
                    producto["stock"] -= stock
                    if producto["stock"] < 0:
                        print(f"{color_tabla_par}No hay suficiente stock. El stock actual es {producto["stock"] + stock}.{terminar_color}")
                        producto["stock"] += stock  # Revertir el cambio
                    elif producto["stock"] <= 30:
                        print(f"{color_tabla_par} El stock actual esta por debajo del minimo requerido (30 unidades). El stock actual es {producto["stock"]}.{terminar_color}")
                        recordar_tiempo_envio = calcular_tiempo_entrega(buscar_id(data.proveedores, producto["id_proveedor"], 1)[3])
                        print(f"{color_tabla_par}Recuerde que pidiendo hoy para re abastecer el stock los productos llegaran recien el dia: {recordar_tiempo_envio}{terminar_color}") 
                        movimiento_stock(1, stock, producto["nombre"]) 
                    else:
                        movimiento_stock(1, stock, producto["nombre"])  
            elif opcion_modificar == 4:
                precio = float(input(f"{color_tabla_par}Ingrese el nuevo precio: {terminar_color}"))
                producto["precio"] = precio
            mostrar_tabla(matriz, columnas, opcion)
            print(f"{color_tabla_par}Producto modificado correctamente.{terminar_color}")
        else:
            print(f"{color_tabla_par}Producto no encontrado.{terminar_color}")
    elif opcion == 1:  # Si es proveedores
        id_modificar = int(input(f"{color_tabla_par}Ingrese el ID del proveedor a modificar: {terminar_color}"))
        proveedor = buscar_id(matriz, id_modificar, opcion)
        if proveedor:
            print(f"{color_tabla_par}Proveedor encontrado: {proveedor[1]}, con venta minima de {proveedor[2]} y entrega de {proveedor[3]} dias.{terminar_color}")
            opcion_modificar = input(f"{color_tabla_par}Qué desea modificar? 1-Nombre del proveedor | 2-Venta minima | 3-Tiempo estimado de entrega | 4-CUIL:{terminar_color}")
            if opcion_modificar == "1":
                nombre_proveedor = input(f"{color_tabla_par}Ingrese el nuevo nombre del proveedor: {terminar_color}")
                proveedor[1] = nombre_proveedor
            elif opcion_modificar == "2":
                venta_minima = int(input(f"{color_tabla_par}Ingrese la nueva venta mínima: {terminar_color}"))
                proveedor[2] = venta_minima
            elif opcion_modificar == "3":
                plazo_entrega = int(input(f"{color_tabla_par}Ingrese el nuevo plazo de entrega (días): {terminar_color}"))
                proveedor[3] = plazo_entrega
            elif opcion_modificar == "4":
                cambio = 0
                cuit_proveedores = sorted([fila[4] for fila in matriz])
                while cambio == 0:
                    cuit = input(f"{color_tabla_par}Ingrese el CUIT: {terminar_color}")
                    patron = re.compile('\d{2}-\d{8}-\d')  
                    if patron.match(cuit):
                        if cuit in cuit_proveedores:
                            print(f"{color_tabla_par}El CUIT ya existe. Ingrese un CUIT único.{terminar_color}")
                        else:
                            cuit_proveedores.append(cuit)
                            proveedor[4] = cuit
                            print(f"{color_tabla_par}Proveedor modificado correctamente.{terminar_color}")
                            cambio =+ 1
                    else:
                        print(f"{color_tabla_par}El formato de CUIT es incorrecto. Debe ser XX-XXXXXXXX-X.{terminar_color}")
                mostrar_tabla(matriz, columnas, opcion)
        else:
            print(f"{color_tabla_par}Proveedor no encontrado.{terminar_color}")
    return matriz

def movimiento_stock(opcion, stock, producto): #funcion que genera una tabla de movimientos de stock que tambien marca que dia ocurrio
    descripcion_columnas = ["ID", "Tipo(Ingreso, Egreso)", "Producto", "cantidad", "fecha"]
    movimiento_stock = data.movimiento_stock
    id_movimiento = len(movimiento_stock) + 1
    if opcion == 0:  # Si es ingreso
        tipo_movimiento = "Ingreso"
        cantidad = stock
    elif opcion == 1:  # Si es egreso
        tipo_movimiento = "Egreso"
        cantidad = stock
    fecha = datetime.date.today().strftime("%d-%m-%y")
    movimiento_stock.append((id_movimiento, tipo_movimiento, producto, cantidad, fecha))
    mostrar_tabla(movimiento_stock, descripcion_columnas, 2) 


def estadisticas(): #funcion estadistica genera que da cantidad de productos, categorias y proveedores, entre otras
    productos = data.productos
    categorias = data.categorias
    proveedores = data.proveedores

    total_productos = len(productos)
    total_categorias = len(categorias)
    total_proveedores = len(proveedores)

    producto_mas_caro = max(productos, key=lambda x: x["precio"])
    producto_mas_barato = min(productos, key=lambda x: x["precio"])
    proveedor_mas_productos = max(proveedores, key=lambda x: sum(1 for prod in productos if prod["id_proveedor"] == x[0]))
    categoria_mas_productos = max(categorias, key=lambda x: sum(1 for prod in productos if prod["id_categoria"] == x[0]))

    print(f"{negrita}{color_tabla_par}Estadísticas del sistema:{terminar_color}")
    print(f"{color_tabla_par}Total de productos: {total_productos}")
    print(f"Total de categorías: {total_categorias}")
    print(f"Total de proveedores: {total_proveedores}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} - Precio: {producto_mas_caro['precio']}")
    print(f"Producto más barato: {producto_mas_barato['nombre']} - Precio: {producto_mas_barato['precio']}")
    print(f"Proveedor con más productos: {proveedor_mas_productos[1]} - Cantidad de productos: {sum(1 for prod in productos if prod['id_proveedor'] == proveedor_mas_productos[0])}")
    print(f"Categoría con más productos: {categoria_mas_productos[1]} - Cantidad de productos: {sum(1 for prod in productos if prod['id_categoria'] == categoria_mas_productos[0])}{terminar_color}")

def calcular_tiempo_pedido(plazo_dias): #Esta funcion calcula que dia se hizo un pedido mediante que dia aumenta el stock teniendo en cuenta el tiempo de entrega del proveedor
    hoy = datetime.date.today()
    fecha_entrega = hoy - datetime.timedelta(days=plazo_dias)
    return fecha_entrega.strftime("%d-%m-%Y")

def calcular_tiempo_entrega(plazo_dias): #esta funcion calcula que dia llegara el producto si se pide ese mismo que se hizo el descenso de stock
    hoy = datetime.date.today()
    fecha_entrega = hoy + datetime.timedelta(days=plazo_dias)
    return fecha_entrega.strftime("%d-%m-%Y")


def top_productos_vendidos():
    movimientos = data.movimiento_stock
    ventas = {}

    # Contamos solo los movimientos, que serian ventas (creo)
    for mov in movimientos:
        if mov[1].lower() == "egreso":
            producto = mov[2]
            cantidad = mov[3]
            ventas[producto] = ventas.get(producto, 0) + cantidad

    if not ventas:
        print(f"{color_tabla_par}No hay registros de ventas aún.{terminar_color}")
        return

    # utilizamos lambda para el ordenamiento de mayor a menor
    top_ventas = sorted(ventas.items(), key=lambda x: x[1], reverse=True)[:3]

    i = 1
    for producto, cantidad in top_ventas:
        print(f"{color_tabla_par}{i}. {producto} - Vendidos: {cantidad}{terminar_color}")
        i += 1
