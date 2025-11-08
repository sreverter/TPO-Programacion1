import random
import archivo as data
import re
import datetime

negrita = '\033[1m'
color_tabla_par = '\033[37;44m'
color_tabla_impar = '\033[34;46m'
terminar_color = '\033[0m'
descripcion_columnas_categorias = ["ID", "CATEGORIA_NOMBRE"]
descripcion_columnas_productos = ["ID", "ID_CATEGORIA", "NOMBRE", "ID_PROVEEDOR", "STOCK", "PRECIO", "STATUS"]
descripcion_columnas_proveedores = ["ID", "Nombre", "Venta mínima", "Plazo de entrega(dias)", "CUIT", "Status"]

def buscar_id(matriz, id_buscar, opcion=None):
    return next(
        filter(lambda fila: isinstance(fila, dict) and fila.get("id") == id_buscar, matriz),
        None
    )

def mostrar_tabla(matriz, columnas, opcion, inactivos=1):
    categorias = data.cargar_categorias()
    proveedores = data.cargar_proveedores()

    def obtener_nombre_categoria(id_cat):
        return next((c["nombre"] for c in categorias if c["id"] == id_cat), "N/A")

    def obtener_nombre_proveedor(id_prov):
        return next((p["nombre"] for p in proveedores if p["id"] == id_prov), "N/A")

    def estado_texto(valor):
        return "Activo" if valor else "Inactivo"

    if not matriz:
        print("No hay datos para mostrar.")
        return

    if opcion == 0:  # Productos
        claves_diccionario = list(matriz[0].keys())
        for clave in claves_diccionario:
            print(f"{negrita}{color_tabla_par}|{clave:<21}|{terminar_color}", end="")
        print()

        for fila in matriz:
            if inactivos or fila.get("status"):
                color = color_tabla_par if fila["id"] % 2 == 0 else color_tabla_impar
                for clave in fila:
                    valor = fila[clave]
                    if clave == "id_categoria":
                        print(f"{color}|{obtener_nombre_categoria(valor):<21}|{terminar_color}", end="")
                    elif clave == "id_proveedor":
                        print(f"{color}|{obtener_nombre_proveedor(valor):<21}|{terminar_color}", end="")
                    elif clave == "status":
                        print(f"{color}|{estado_texto(valor):<21}|{terminar_color}", end="")
                    else:
                        print(f"{color}|{str(valor):<21}|{terminar_color}", end="")
                print()
        print()

    elif opcion == 1:  # Proveedores
        for col in columnas:
            print(f"{negrita}{color_tabla_par}|{col:<25}|", end="")
        print()

        for fila in matriz:
            if fila.get("activo") or inactivos:
                color = color_tabla_par if fila["id"] % 2 == 0 else color_tabla_impar
                for valor in fila.values():
                    texto = "Activo" if valor is True else "Inactivo" if valor is False else str(valor)
                    print(f"{color}|{texto:<25}|{terminar_color}", end="")
                print()
        print()

    else:  # Categorías
        for col in columnas:
            print(f"{negrita}{color_tabla_par}|{col:<25}|", end="")
        print()

        for fila in matriz:
            color = color_tabla_par if fila["id"] % 2 == 0 else color_tabla_impar
            for valor in fila.values():
                print(f"{color}|{str(valor):<25}|{terminar_color}", end="")
            print()
        print()

def desactivar_registro(matriz, id_desactivar, opcion):
    fila = buscar_id(matriz, id_desactivar, opcion)
    if opcion == 0:  # Si es productos
        if fila:
            fila["status"] = False
            print("Registro desactivado correctamente.")
        else:
            print("No se encontró el registro.")
    elif opcion == 1:  # Si es proveedores
        if fila:
            fila["activo"] = False
            print("Registro desactivado correctamente.")
        else:
            print("No se encontró el registro.")
    else:
        if fila:
            matriz.remove(fila)
            print("Registro eliminado correctamente.")

def agregar_registro(matriz, columnas, opcion):
    # Cargar datos actualizados
    categorias = data.cargar_categorias()
    proveedores = data.cargar_proveedores()
    
    if opcion == 0:  # Si es productos
        nuevo_producto_id = matriz[-1]["id"] + 1 if matriz else 1
        mostrar_tabla(categorias, descripcion_columnas_categorias, 2)
        categoria_producto = input(f"{color_tabla_par}Ingrese el ID de la categoria de producto: (Escriba N si no es ninguna de las categorias listadas) {terminar_color}")
        if categoria_producto.upper() == "N":
            print("Debe agregar una categoría antes de agregar un producto.")
            return
        nombre_producto = input("Ingrese el nombre del producto: ")
        mostrar_tabla(proveedores, descripcion_columnas_proveedores, 1)
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        proveedor_id = buscar_proveedor(nombre_proveedor)
        if proveedor_id is None:
            print("Proveedor no encontrado.")
            return matriz
        stock = int(input("Ingrese el stock: "))
        precio = float(input("Ingrese el precio: "))
        nuevo_producto = {
            'id': nuevo_producto_id,
            "id_categoria": int(categoria_producto),
            "nombre": nombre_producto,
            "id_proveedor": proveedor_id,
            "stock": stock,
            "precio": precio,
            "status": True
        }
        matriz.append(nuevo_producto)
        mostrar_tabla([nuevo_producto], columnas, opcion)
        print(f"Producto agregado correctamente.{terminar_color}")
    elif opcion == 1:  # Si es proveedores
        nuevo_proveedor_id = matriz[-1]["id"] + 1 if matriz else 1
        nombre_proveedor = input(f"{color_tabla_par}Ingrese el nombre del proveedor: {terminar_color}")
        venta_minima = int(input("Ingrese la venta mínima: "))
        plazo_entrega = int(input("Ingrese el plazo de entrega (días): "))
        
        cuit_proveedores = [fila["cuit"] for fila in matriz]
        cuit = ""
        cuit_valido = False
        while not cuit_valido:
            cuit = input("Ingrese el CUIT: ")
            patron = re.compile(r'\d{2}-\d{8}-\d')
            if patron.match(cuit):
                if cuit in cuit_proveedores:
                    print("El CUIT ya existe. Ingrese un CUIT único.")
                else:
                    cuit_valido = True
            else:
                print("El formato de CUIT es incorrecto. Debe ser XX-XXXXXXXX-X.")

        nuevo_proveedor = {
            "id": nuevo_proveedor_id,
            "nombre": nombre_proveedor,
            "productos_sum": venta_minima,
            "tiempo_entrega": plazo_entrega,
            "cuit": cuit,
            "activo": True
        }

        matriz.append(nuevo_proveedor)
        mostrar_tabla(matriz, columnas, opcion)
        print(f"Proveedor agregado correctamente.{terminar_color}")
    elif opcion == 2:  # Si es categorias
        nueva_categoria_id = matriz[-1]["id"] + 1 if matriz else 1
        nombres_categorias = [categoria["nombre"] for categoria in matriz]
        nombre_categoria = input(f"{color_tabla_par}Ingrese el nombre de la categoría: {terminar_color}")
        
        nombre_unico = False
        while not nombre_unico:
            if nombre_categoria.capitalize() in nombres_categorias:
                print("La categoría ya existe. Ingrese un nombre único.")
                nombre_categoria = input("Ingrese el nombre de la categoría: ")
            else:
                nombre_unico = True
        
        nueva_categoria = {
            "id": nueva_categoria_id,
            "nombre": nombre_categoria.capitalize()
        }
        matriz.append(nueva_categoria)
        mostrar_tabla(matriz, columnas, opcion)
        print(f"Categoría agregada correctamente.{terminar_color}")

def buscar_proveedor(busqueda):
    proveedores = data.cargar_proveedores()
    busqueda = busqueda.upper()

    i = 0
    while i < len(proveedores):
        fila = proveedores[i]
        nombre_proveedor = fila["nombre"].upper()
        if nombre_proveedor == busqueda:
            return fila["id"]
        i += 1
    return None

def busqueda_proveedor_parcial():
    proveedores = data.cargar_proveedores()
    busqueda = input(f"{color_tabla_par}Escriba la letra o las primeras 3 letras de los proveedores que desea buscar: {terminar_color}")
    patron = re.compile(busqueda, re.IGNORECASE)

    resultados = []
    i = 0
    while i < len(proveedores):
        fila = proveedores[i]
        if patron.search(fila["nombre"]):
            resultados.append(fila)
        i += 1

    if len(resultados) > 0:
        print(f"Estos son los resultados encontrados para su búsqueda: \n{terminar_color}")
        j = 0
        while j < len(resultados):
            fila = resultados[j]
            print(f"{color_tabla_par}-Nombre {fila['nombre']} - Entrega minima: {fila['productos_sum']} unidades - Plazo de entrega: {fila['tiempo_entrega']} dias{terminar_color}")
            j += 1
    else:
        print(f"{color_tabla_par}No se encontraron resultados.{terminar_color}")

def busqueda_productos_parcial():
    productos = data.cargar_productos()
    busqueda = input(f"{color_tabla_par}Escriba la letra o las primeras 3 letras de los productos que desea buscar: {terminar_color}")
    patron = re.compile(busqueda, re.IGNORECASE)

    resultados = []
    i = 0
    while i < len(productos):
        fila = productos[i]
        if patron.search(fila["nombre"]):
            resultados.append(fila)
        i += 1

    if len(resultados) > 0:
        print(f"Estos son los resultados encontrados para su búsqueda: \n{terminar_color}")
        j = 0
        while j < len(resultados):
            fila = resultados[j]
            print(f"{color_tabla_par}-Nombre {fila['nombre']} - Stock: {fila['stock']} unidades - Precio: {fila['precio']} pesos{terminar_color}")
            j += 1
    else:
        print(f"{color_tabla_par}No se encontraron resultados.{terminar_color}")

def modificar_registro(matriz, columnas, opcion):
    if opcion == 0:  # Si es productos
        mostrar_tabla(matriz, columnas, opcion)
        id_modificar = int(input(f"{color_tabla_par}Ingrese el ID del producto a modificar: {terminar_color}"))
        producto = buscar_id(matriz, id_modificar, opcion)
        if producto:
            print(f"{color_tabla_par}Producto encontrado:{terminar_color}")
            proveedores = data.cargar_proveedores()
            distribuidor = buscar_id(proveedores, producto["id_proveedor"])
            nombre_distribuidor = distribuidor['nombre'] if distribuidor else "N/A"
            print(f"{color_tabla_par}El producto es {producto['nombre']}, del distribuidor {nombre_distribuidor}, tiene un stock de {producto['stock']} unidades y un precio de {producto['precio']} pesos{terminar_color}")
            opcion_modificar = int(input(f"{color_tabla_par}Qué desea modificar? 1-Nombre del producto | 2-Nombre del proveedor | 3-Stock | 4-Precio: {terminar_color}"))
            if opcion_modificar == 1:
                nombre_producto = input(f"{color_tabla_par}Ingrese el nuevo nombre del producto: {terminar_color}")
                producto["nombre"] = nombre_producto
            elif opcion_modificar == 2:
                nombre_proveedor = input(f"{color_tabla_par}Ingrese el nuevo nombre del proveedor: {terminar_color}")
                proveedor_id = buscar_proveedor(nombre_proveedor)
                if proveedor_id is not None:
                    producto["id_proveedor"] = proveedor_id
                else:
                    print("Proveedor no encontrado.")
            elif opcion_modificar == 3:
                opcion_stock = input(f"{color_tabla_par}Esta 1-Ingresando stock o 2-Retirando stock?: {terminar_color}")
                if opcion_stock == "1":
                    stock = int(input(f"{color_tabla_par}Ingrese la cantidad a ingresar: {terminar_color}"))
                    producto["stock"] += stock
                    movimiento_stock(0, stock, producto["nombre"])
                    proveedores = data.cargar_proveedores()
                    proveedor_obj = buscar_id(proveedores, producto["id_proveedor"])
                    if proveedor_obj:
                        calcular_tiempo = calcular_tiempo_pedido(proveedor_obj["tiempo_entrega"])
                        print(f"{color_tabla_par}El producto se pidio el día {calcular_tiempo}{terminar_color}")
                elif opcion_stock == "2":
                    stock = int(input(f"{color_tabla_par}Ingrese la cantidad a retirar: {terminar_color}"))
                    producto["stock"] -= stock
                    if producto["stock"] < 0:
                        print(f"{color_tabla_par}No hay suficiente stock. El stock actual es {producto['stock'] + stock}.{terminar_color}")
                        producto["stock"] += stock
                    elif producto["stock"] <= 30:
                        print(f"{color_tabla_par} El stock actual esta por debajo del minimo requerido (30 unidades). El stock actual es {producto['stock']}.{terminar_color}")
                        proveedores = data.cargar_proveedores()
                        proveedor_obj = buscar_id(proveedores, producto["id_proveedor"])
                        if proveedor_obj:
                            recordar_tiempo_envio = calcular_tiempo_entrega(proveedor_obj["tiempo_entrega"])
                            print(f"{color_tabla_par}Recuerde que pidiendo hoy para re abastecer el stock los productos llegaran recien el dia: {recordar_tiempo_envio}{terminar_color}") 
                        movimiento_stock(1, stock, producto["nombre"]) 
                    else:
                        movimiento_stock(1, stock, producto["nombre"])  
            elif opcion_modificar == 4:
                precio = float(input(f"{color_tabla_par}Ingrese el nuevo precio: {terminar_color}"))
                producto["precio"] = precio
            mostrar_tabla([producto], columnas, opcion)
            print(f"{color_tabla_par}Producto modificado correctamente.{terminar_color}")
        else:
            print(f"{color_tabla_par}Producto no encontrado.{terminar_color}")
    elif opcion == 1:  # Si es proveedores
        id_modificar = int(input(f"{color_tabla_par}Ingrese el ID del proveedor a modificar: {terminar_color}"))
        proveedor = buscar_id(matriz, id_modificar, opcion)
        if proveedor:
            print(f"{color_tabla_par}Proveedor encontrado: {proveedor['nombre']}, con venta minima de {proveedor['productos_sum']} y entrega de {proveedor['tiempo_entrega']} dias.{terminar_color}")
            opcion_modificar = input(f"{color_tabla_par}Qué desea modificar? 1-Nombre del proveedor | 2-Venta minima | 3-Tiempo estimado de entrega | 4-CUIT:{terminar_color}")
            if opcion_modificar == "1":
                nombre_proveedor = input(f"{color_tabla_par}Ingrese el nuevo nombre del proveedor: {terminar_color}")
                proveedor["nombre"] = nombre_proveedor
            elif opcion_modificar == "2":
                venta_minima = int(input(f"{color_tabla_par}Ingrese la nueva venta mínima: {terminar_color}"))
                proveedor["productos_sum"] = venta_minima
            elif opcion_modificar == "3":
                plazo_entrega = int(input(f"{color_tabla_par}Ingrese el nuevo plazo de entrega (días): {terminar_color}"))
                proveedor["tiempo_entrega"] = plazo_entrega
            elif opcion_modificar == "4":
                cambio = False
                cuit_proveedores = [fila["cuit"] for fila in matriz if fila["id"] != proveedor["id"]]
                while not cambio:
                    cuit = input(f"{color_tabla_par}Ingrese el CUIT: {terminar_color}")
                    patron = re.compile(r'\d{2}-\d{8}-\d')  
                    if patron.match(cuit):
                        if cuit in cuit_proveedores:
                            print(f"{color_tabla_par}El CUIT ya existe. Ingrese un CUIT único.{terminar_color}")
                        else:
                            proveedor["cuit"] = cuit
                            print(f"{color_tabla_par}Proveedor modificado correctamente.{terminar_color}")
                            cambio = True
                    else:
                        print(f"{color_tabla_par}El formato de CUIT es incorrecto. Debe ser XX-XXXXXXXX-X.{terminar_color}")
                mostrar_tabla([proveedor], columnas, opcion)
        else:
            print(f"{color_tabla_par}Proveedor no encontrado.{terminar_color}")
    return matriz

def movimiento_stock(opcion, stock, producto):
    descripcion_columnas = ["ID", "Tipo(Ingreso, Egreso)", "Producto", "cantidad", "fecha"]
    movimiento_stock = data.cargar_movimientos()
    id_movimiento = len(movimiento_stock) + 1
    if opcion == 0:
        tipo_movimiento = "Ingreso"
        cantidad = stock
    elif opcion == 1:
        tipo_movimiento = "Egreso"
        cantidad = stock
    fecha = datetime.date.today().strftime("%d-%m-%y")
    movimiento_stock.append([id_movimiento, tipo_movimiento, producto, cantidad, fecha])
    data.guardar_movimientos(movimiento_stock)
    
    print(f"{color_tabla_par}Movimiento registrado: {tipo_movimiento} de {cantidad} unidades de {producto} - Fecha: {fecha}{terminar_color}") 

def estadisticas():
    productos = data.cargar_productos()
    categorias = data.cargar_categorias()
    proveedores = data.cargar_proveedores()

    total_productos = len(productos)
    total_categorias = len(categorias)
    total_proveedores = len(proveedores)

    if productos:
        producto_mas_caro = max(productos, key=lambda x: x["precio"])
        producto_mas_barato = min(productos, key=lambda x: x["precio"])
    else:
        producto_mas_caro = {"nombre": "N/A", "precio": 0}
        producto_mas_barato = {"nombre": "N/A", "precio": 0}

    if proveedores:
        proveedor_mas_productos = max(proveedores, key=lambda x: sum(1 for prod in productos if prod["id_proveedor"] == x["id"]))
    else:
        proveedor_mas_productos = {"nombre": "N/A"}

    if categorias:
        categoria_mas_productos = max(categorias, key=lambda x: sum(1 for prod in productos if prod["id_categoria"] == x["id"]))
    else:
        categoria_mas_productos = {"nombre": "N/A"}

    print(f"{negrita}{color_tabla_par}Estadísticas del sistema:{terminar_color}")
    print(f"{color_tabla_par}Total de productos: {total_productos}")
    print(f"Total de categorías: {total_categorias}")
    print(f"Total de proveedores: {total_proveedores}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} - Precio: {producto_mas_caro['precio']}")
    print(f"Producto más barato: {producto_mas_barato['nombre']} - Precio: {producto_mas_barato['precio']}")
    print(f"Proveedor con más productos: {proveedor_mas_productos['nombre']} - Cantidad de productos: {sum(1 for prod in productos if prod['id_proveedor'] == proveedor_mas_productos['id'])}")
    print(f"Categoría con más productos: {categoria_mas_productos['nombre']} - Cantidad de productos: {sum(1 for prod in productos if prod['id_categoria'] == categoria_mas_productos['id'])}{terminar_color}")

def calcular_tiempo_pedido(plazo_dias):
    hoy = datetime.date.today()
    fecha_entrega = hoy - datetime.timedelta(days=plazo_dias)
    return fecha_entrega.strftime("%d-%m-%Y")

def calcular_tiempo_entrega(plazo_dias):
    hoy = datetime.date.today()
    fecha_entrega = hoy + datetime.timedelta(days=plazo_dias)
    return fecha_entrega.strftime("%d-%m-%Y")

def top_productos_vendidos():
    movimientos = data.cargar_movimientos()
    ventas = {}

    i = 0
    while i < len(movimientos):
        mov = movimientos[i]
        if mov[1].lower() == "egreso":
            producto = mov[2]
            cantidad = mov[3]
            ventas[producto] = ventas.get(producto, 0) + cantidad
        i += 1

    if not ventas:
        print(f"{color_tabla_par}No hay registros de ventas aún.{terminar_color}")
        return

    top_ventas = sorted(ventas.items(), key=lambda x: x[1], reverse=True)[:3]

    j = 0
    while j < len(top_ventas):
        producto, cantidad = top_ventas[j]
        print(f"{color_tabla_par}{j + 1}. {producto} - Vendidos: {cantidad}{terminar_color}")
        j += 1
