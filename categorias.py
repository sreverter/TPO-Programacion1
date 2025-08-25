import data as data

data_categorias = data.categorias
print("Lista de Categorías:")
descripcion_columnas = ["ID", "NOMBRE"]
print(descripcion_columnas)
for fila in data_categorias:
    print(fila)