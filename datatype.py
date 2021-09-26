# las cadenas de caracteres entre comillas (simples o dobles)se llaman strings
print("Hello World")
print("hello world")
print("hello World")
print("HEllo world")
print(type("Hello World"))
#la funcion type me informa que tipo de entrada es Hello World. En este caso el tipo de entra es sting (str)
#para que el interprete haga aparecer en la pantalla el de tipo de entrada haya que utilizar el comando print (de otra forma no se visualiza)

print("Bye" + " " + "World")

print(30)
# al escribir type en el interprete para saber el tipo de dato que es 30 aparece int (numero entero)
print(30.5)
#al escribir type para saber que tipo de dato es 30.5 nos devuelve float (decimal. Punto flotante)

# los tipos de datos logicos se denominan BOOLEAN (verdadero, falso). Al usar TYPE en FALSE o TRUE aparece como tipo de dato BOOL.
True
False

#Tipo de dato LIST. Agrupa datos que se colocan entre corchetes
[10, 20, 30, 40, 50] 
[10, "Hello", True, 10.1]

#Tuple. Es un tipo de dato que no puede cambiar. Los tipos de dato LIST si puden cambiar
(10, 20, 30, 40)

# Diccionario. Agrupa diferentes tipos de datos con una CLAVE y un VALOR (CLAVE "Nombre" VALOR "Juan Anselmo")
{
    "Nombre":"Juan Anselmo",
    "Apellido":"Gimenez",
    "Apodo":"Chuqui"
}
print(type({
    "Nombre":"Juan Anselmo",
    "Apellido":"Gimenez",
    "Apodo":"Chuqui"
}))









