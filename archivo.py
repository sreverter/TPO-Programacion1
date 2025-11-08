import json
import os

CARPETA_DATA = "data"

def _ensure_data_dir():
    """Crea la carpeta data si no existe"""
    if not os.path.exists(CARPETA_DATA):
        os.makedirs(CARPETA_DATA)

def cargar_datos(archivo):
    ruta = os.path.join(CARPETA_DATA, archivo)
    datos = []
    
    try:
        arch = open(ruta, 'r', encoding='utf-8')
        contenido = ""
        linea = arch.readline()
        
        while linea != "":
            contenido += linea
            linea = arch.readline()
        
        arch.close()
        
        if contenido.strip():
            datos = json.loads(contenido)
            
    except FileNotFoundError:
        datos = []
    except json.JSONDecodeError:
        print("Error: Archivo JSON corrupto:", ruta)
        datos = []
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        datos = []
    
    return datos

def guardar_datos(archivo, datos):
    _ensure_data_dir()
    ruta = os.path.join(CARPETA_DATA, archivo)
    exito = False
    
    try:
        arch = open(ruta, 'w', encoding='utf-8')
        json_str = json.dumps(datos, ensure_ascii=False, indent=4)
        lineas = json_str.split('\n')
        
        for i, linea in enumerate(lineas):
            arch.write(linea)
            if i < len(lineas) - 1:
                arch.write('\n')
        
        arch.close()
        exito = True
        
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        exito = False
    
    return exito

def cargar_movimientos():
    """Para poder usar lista de listas"""
    ruta = os.path.join(CARPETA_DATA, "movimientos.txt")
    movimientos = []
    
    try:
        arch = open(ruta, 'r', encoding='utf-8')
        linea = arch.readline()
        
        while linea != "":
            linea = linea.strip()
            if linea:
                campos = linea.split(';')
                try:
                    id_mov = int(campos[0])
                    tipo = campos[1]
                    producto = campos[2]
                    cantidad = int(campos[3])
                    fecha = campos[4]
                    movimientos.append([id_mov, tipo, producto, cantidad, fecha])
                except (IndexError, ValueError):
                    pass
            linea = arch.readline()
        
        arch.close()
        
    except FileNotFoundError:
        movimientos = []
    except Exception as e:
        print(f"Error al cargar movimientos: {e}")
        movimientos = []
    
    return movimientos

def guardar_movimientos(datos):
    _ensure_data_dir()
    ruta = os.path.join(CARPETA_DATA, "movimientos.txt")
    exito = False
    
    try:
        arch = open(ruta, 'w', encoding='utf-8')
        i = 0
        while i < len(datos):
            movimiento = datos[i]
            linea = ';'.join(str(item) for item in movimiento)
            arch.write(linea)
            if i < len(datos) - 1:
                arch.write('\n')
            i += 1
        
        arch.close()
        exito = True
        
    except Exception as e:
        print(f"Error al guardar movimientos: {e}")
        exito = False
    
    return exito

def cargar_productos():
    return cargar_datos("productos.json")

def guardar_productos(datos):
    return guardar_datos("productos.json", datos)

def cargar_proveedores():
    return cargar_datos("proveedores.json")

def guardar_proveedores(datos):
    return guardar_datos("proveedores.json", datos)

def cargar_categorias():
    return cargar_datos("categorias.json")

def guardar_categorias(datos):
    return guardar_datos("categorias.json", datos)