alimentos=["carne", "cebolla", "morron", "palta"]

for alimento in alimentos:
    print(alimento)
# con el procedimiento de la linea 3 hacemos que mediante la entrada ALIMENTO se muestren cada uno de los elementos que componen la lista ALIMENTOS.

print(" ")

for alimento in alimentos:
    if alimento == "cebolla":
        print("El próximo alimento en la lista falta en la heladera")
    print(alimento)    
# se puden realizar comprobaciones al ejecutar los elementos de la lista. En este caso comprobamos el elemento CEBOLLA y le decimos al interprete que imprima un mensaje cuando lo encuentra. Luego pedimos al interprete que imprima la lista y antes del elemento solicitado aparece el mensage del PRINT

print(" ")

for alimento in alimentos:
    if alimento =="cebolla":
        break
    print(alimento)
# el operador BREAK hace que se muestren los elemtos de la lista hasta el especificado (este no se muestra). En esta lista solo se mostraria CARNE

print(" ")

for alimento in alimentos:
    if alimento =="cebolla":
        continue
    print(alimento)    
# el operador CONTINUE al encontrar el elemento solicitado no lo menc   iona y sigue adelante con la lista

print(" ")

for numero in range(1, 8):
    print(numero)
# FOR puede ser aplicado a un RANGO

print(" ")

for letras in "Hola, buen día":
    print(letras)
#FOR también puede mostrar uno a uno los elementos de una frase (letra a letraa)

print(" ")

conteo = 4

while conteo <= 10:
    print(conteo)
    conteo = conteo + 1
# al función WHILE es un IF reitrativo, continua haciando la comprobación de forma infinita y es por eso que en este caso se agrega conteo=conteo+1 para que el elemento CONTEO llegue a 10 y deje de comprobarlo. Es decir que va a realizar la comprobación hasta que no se cumpla el condicionante (que sea menor a 10)










































