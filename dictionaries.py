producto={
    "nombre_producto":"libro",
    "cantidad":3,
    "precio":4.99
}

print(type(producto))

print(producto.keys())
#con la función KEYS se obtinen las CLAVES (clasificación del dato o elemento)

print(producto.items())
#con el comando ITEMS devuelve la descripción del elemento (libro, 3 o 4.99 en este caso)

#también se puede utilizar DEL en los DICCIONARIOS
#del producto

#con CLEAR se pueden limpiar sus elementos internos
producto.clear()
print(producto)

#se pueden incluir DICCIONARIOS dentro de LISTAS
varios=[
    {"Producto":"Libro", "Título":"Ficciones", "Cantidad":5},
{"Producto":"Revista", "Título":"Mecanica Popular", "Cantidad":12}
]
print(varios)
print(varios[1])




















