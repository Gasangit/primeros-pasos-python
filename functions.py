def hello():
    print("Hello World")

hello()

# con DEF definimos una FUNCIÓN que es igual a decirle al INTERPRETE que realice un procedimiento cada vez que llamamos a dicha función poniendo su NOMBRE seguido de ()
 
def hola(nombre):
    print("Hola" + nombre)

hola(" Uno")
hola(" Una")
hola(" La Gorda")

# también pordemos definir un ARGUMENTO entre los () para que sea solicitado por la función (imagino que se podra incluir un INPUT)
# si se solicita un ARGUMENTO y el mismo no es ingresado arrojara error

def hola2(nombre=" Persona"):
    print("HOLA"+nombre)
#en este caso si no se ingresa valos alguno como ARGUMENTO el interprete pondra por defecto la palabra PERSONA

hola2()

#se puede solictar MÁS DE UN ARGUMENTO
def sumarnumeros(numero1, numero2):
    return numero1 + numero2

print(sumarnumeros(4, 5))

suma = lambda numero3, numero4: numero3 + numero4
print(suma(1, 4))
# otra forma de escribir FUNCIONSES mediante la función LAMBDA






