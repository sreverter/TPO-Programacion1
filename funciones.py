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
