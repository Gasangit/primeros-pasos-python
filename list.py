demo_list=[1, "Hello", 1.34, True,[1, 2, 3] ]
colors=["red", "green", "blue"]

#numbers_list=list(1, 2, 3, 4)
# print(numbers_list)
#en el último caso la lista se escribió como un STRING. Para poder visualizarla en el interprete hay que escribirla como una TUPLA 
# (revisar este termino, no entiendo la diferencia con lista) agregando un par mas de parentesis.

numbers_list=list((1, 2, 3, 4))
print(numbers_list)

r=list(range(1, 10))
print(r)
#la funcion range completa el rango entre dos números para poder crear listas instantaneas con gran cantidad de numeros

print(dir(colors))
#recordar que la funcion DIR permite ver las opciones de todo lo que se puede hacer(en este caso con una LISTA)

print(colors[1])
#con el número entre corchetes traigo el elemento de la LISTA COLORS que ocupa esa posición

print("green" in colors)
#con IN se puede comprobar si un elemento existe en una LISTA determinada devolviendo TRUE o FALSE

print(colors)
print(demo_list)

colors[1]="yellow"
print(colors)
#en la linea 27 se realizó una operación que permite cambiar uno de los componentes de la LISTA por el que figura luego del signo =

colors.append("violet")
print(colors)
#con la función APPEND agreganos un nuevo dato a la lista. Como en el caso anterior, primero se introduce la modificación y luego si se 
#desea se hace ejecutar en pantalla mediante PRINT

colors.extend(["brown", "pink"])
print(colors)
#para agragar más de un elemento a la vez se debe usar la función EXTED, escribiendo los elemento en una LIST o TUPLE. De lo contrario 
# funciona como APPEND

colors.insert(1, "black")
print(colors)
#con la función INSERT se puede ingresar un nuevo elemento a la LISTA en al posición deseada que esta dada por el número 

colors.insert(len(colors), "white")
print(colors)
#combinando INSERT con LEN (funcion que cuenta los elemtos de la LISTA) puedo insertar un nuevo elemento al final de la lista

colors.pop()
print(colors)
#la funcion POP quita el último elemento de la LISTA. Si continuo ultilizandolo quitara uno a uno los elementos.

colors.remove("blue")
print(colors)
#para quitar un elemento puntual en base a su nombre se usa la funcion REMOVE

colors.pop(0)
print(colors)
#con la funcion POP también puedo quitar un ELEMENTO por su número de INDICE 

colors.clear()
print(colors)
#CLEAR limpia completamente la LISTA

colors.extend(["blue","red","white","green","black","brown"])
print(colors)

colors.sort()
print(colors)
#SORT ordena alfabeticamente los elementos de la LISTA

colors.sort(reverse=True)
print(colors)
#utlizando REVERSE=TRUE junto con SORT ordenamos desde atras hacia adelante alfabeticamente

print(colors.index("black"))
#a traves de INDEX también se puede saber la posición de un elemento dentro de una LISTA (antes se había hecho en un STRING)

print(colors.count("white"))
#mediante la funcion COUNT se puede saber cuantas veces se repite un ELEMENTO de la LISTA







