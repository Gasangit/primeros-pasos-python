x=20

#al colocarse == se comparan dos elementos (3==9, es igual a decir ¿3 es igual que 9?)

if x < 30: 
 print("x es menor que 30")
#al utilizara el IF la linea de PRINT tiene que tener un espacio al comienzo

if x == 20:
 print("x es igual a 20")
 
else:
  print("x no es igual a 20")

#ELSE equivale a decir "en caso contrario"     

numero=input("Ingrese un número cualquiera: ")

numero_int=int(numero)
if numero_int > 2:
    print("El número que ingresó es mayor al que estoy pensando")
elif numero_int == 2:
 print("El número que ingresó es igual al que estoy pensando")    
else:
 print("El número que ingresó es menor al que estoy pensando")

#con ELIF agregamos una condición a la ya existente

#Los IF pueden encadenarse

nombre =input("Ingrese su nombre: ")
apellido =input("Ingrese su apellido: ")

if nombre == "Angel Gaston":
    if apellido == "Mansilla":
        print("Tú eres lo más grande que le pasó a este mundo")
    else:
        print("Tú no eres Angel Gaston Mansilla")
elif nombre != "Angel Gaston":
    if apellido == "Mansilla":
        print("Tu no eres Angel Gaston pero eres Mansilla")
    elif apellido != "Mansilla":
        print("Tú no eres Angel Gaston Mansilla")

from decimal import Decimal
if 0.8 > 0.75 and 0.8 < 1:
    print("1/4 de tasa")
else:
    print("No está en el rango")

med=input("Ingrese un número decimal entre 0 y 10: ")
if int(med) >= 1 and int(med) < 2:
    print("Su medida está en el rango de una tasa más o menos")
else:
    print("Su medida NO está dentro del rango de una tasa")

# se pueden utilizar los operadores AND, OR y NOT para realizar operaciones logicas

num_nuevo=input("Ingrese un número cualquiera: ")
if int(num_nuevo) < 3 or int(num_nuevo) >7:
    print("Su número no está comprendido entre el rango de 3 y 7")
else:
    print("Su número está entre 3 y 7")

laverdad=input("Ingrese i si cree ser inteligente, n si no lo cree: ")
if (not(laverdad == "n")):
    print("Este programa cree que le falta humildad o le sobra astucia (no confundir con inteligencia)")
else:
    print("Puede que sea humilde o no haya entendido la pregunta")







