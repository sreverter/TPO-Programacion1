import random 

filas = 3
columnas = 4

def crear_matriz(filas, columnas):
    matriz = [[0]*columnas for rellenar in range(filas)]
    return matriz

def llenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

def buscar_id(matriz, id_buscar):
    for fila in matriz:
        if fila[0] == id_buscar:
            return fila
    return None

def agregar_producto(matriz):
    nueva_fila = []
    nueva_fila.append(matriz[-1][0] + 1)  # Asignar un nuevo ID
    nueva_fila.append(input("Ingrese el ID de categoría: "))
    nueva_fila.append(input("Ingrese el nombre del producto: "))
    nueva_fila.append(input("Ingrese el ID del proveedor: "))
    nueva_fila.append(int(input("Ingrese el stock: ")))
    nueva_fila.append(float(input("Ingrese el precio: ")))
    matriz.append(nueva_fila)
    
    return matriz
