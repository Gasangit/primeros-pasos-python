myStr="Hello World"
locacion="Argentina,Buenos Aires, CABA"


# print(dir(myStr))
# # con lo escrito en la linea 3 nos informa en la consola del interprete todas las opciones de procesamiento que podemos hacer sobre 
# nuestro string (en este caso Hello World)

# print(myStr.upper())
#pasa todo a mayusculas

print(myStr.lower())
#pasa todo a minusculas

print(myStr.swapcase())
#invierte las mausculas en minuscula y viceversa

print(myStr.capitalize())
#deja solo la primer letra de todo el texto en mayuscula

print(myStr.replace("Hello", "Bye"))
#reemplaza palabras del string

print(myStr.replace("Hello", "Bye").upper())
#combinación de dos operaciones REPLACE y UPPER (metodos encadenados)

print(myStr.count("l"))
#cuenta el caracter definido entre parentesis
print(myStr.count("o"))

print(myStr.startswith("hola"))
#informa por verdadero o falso si un STRING comienza con la palabra consultada entre parentesis

print(myStr.endswith("world"))
#informa si un string finaliza con la palabra consultada

print(myStr.split())
#separa el STRING en base al catacter sugerido entre parentesis. Si no se coloca caracter alguno separa el STRING por los espacios. 
# De esta forma se puede generar una lista (LIST)
print(locacion.split(","))

print(myStr.find("o"))
#devuelve la ubicación del caracter consultado entre los parentesis

print(len(myStr))
#cuenta la cantidad de caractreres del STRING consultado

print(myStr.index("o"))
#devuelve el número de indice del caracter entre parentesis ¿? (el primer caracter del STRING se cuenta como 0)

print(myStr.isnumeric())
#verifica si el STRING es numerico

print(myStr.isalpha())
#verifica si el STRING es alfanumerico

print(myStr[4])
#muestra solo el caracter especificado entre corchetes

# para poder comentar varias lineas a la vez (poniendo # en varias lineas) se seleccionan las lineas a pasar a COMENTARIO y se presiona CTRL SHIFT P, escribiendo COMMENT en el cuadro de dialogo y seleccionando la opción ADD LINE COMMENT


print(myStr[-1])
#al no haber caracteres por debajo de 0 trae el ultimo caracter del STRING

print("My name is" + " " + myStr)
print(f"My name is {myStr}")
#las de arriba son dos formas de concatenar los STRINGS. Uno con el + y otra anteponiendo f al concatenado y poniendo el STRING entre LLAVES

print("My name is {0}".format(myStr))
#reemplaza el 0 colocado entre llaves por el STRING mencionado luego de FORMAT





































