import funciones as f
import data as data

hacer_matriz = input("¿Desea crear una matriz? (s/n): ").lower()
descripcion_data = ["id", "nombre proveedor", "venta minima", "plazo de entrega"]
if hacer_matriz == "s":
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = f.crear_matriz(filas, columnas)
    f.llenar_matriz(matriz)
    print("Matriz creada y llena:")
    print(descripcion_data)
    for fila in matriz:
        print(fila)