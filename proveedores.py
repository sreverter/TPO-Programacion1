#archivo de CRUD proveedores
import funciones as f
import data as data

def proveedores(matriz):
    descripcion_data = ["id", "nombre proveedor", "venta minima", "plazo de entrega", "CUIT"]
    print("Lista de Proveedores:")
    print(descripcion_data)
    for fila in matriz:
        print(fila)

proveedores_data = data.proveedores
proveedores(proveedores_data)
desea_modificar = input("¿Desea modificar la matriz? (s/n): ").lower()
if desea_modificar == "s":
    cual_modifica = int(input("Ingrese el ID del proveedor a modificar: "))
    proveedor_a_modificar = f.buscar_id(proveedores_data, cual_modifica)
    if proveedor_a_modificar:
        print("Proveedor encontrado:", proveedor_a_modificar)
        nuevo_nombre = input("Ingrese el nuevo nombre del proveedor: ")
        nueva_venta_minima = int(input("Ingrese la nueva venta mínima: "))
        nuevo_plazo_entrega = int(input("Ingrese el nuevo plazo de entrega: "))
        proveedor_a_modificar[1] = nuevo_nombre
        proveedor_a_modificar[2] = nueva_venta_minima
        proveedor_a_modificar[3] = nuevo_plazo_entrega 
        print("Proveedor modificado:", proveedor_a_modificar)
        
        
def modificar_proveedor(id_proveedor, proveedores_data)