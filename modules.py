#los MODULOS corresponden a código ya creado de forma eficiente por otros usuarios o integrado en Python que podemos utilizar en
#nuestros programas aportando funcionalidades sin tener que escribri el código desde cero.

#los MÓDULOS son también conocidos como BIBLIOTECAS

#Existen 3 tipos de modulos
#OWN MODULE >> el que podemos escribir nosotros mismos
#THIRDY PARTY MODULE >> es el que podemos descargar desde internet
#PYTHON MODULES >> es el que podemos ejecutar desde la biblioteca de Python

#No solo se pueden agregar funcionalidades a través de los módulos también pueden utilizarse para dividir aplicaciones muy grandes

#un ejemplo de módulo es el datetime que agrega funcionalidades relacionadas con la hora

import datetime 
print(datetime.date.today())

#linea 16 expresa que del MÓDULO datetime quiero ejecutar el PARAMETRO date y su método llamado TODAY (con esto veo la fecha del día)


print(datetime.timedelta(minutes=70))
#esta otra funcionalidad del módulo DATETIME pasa los minutos a horas

from datetime import timedelta
print(timedelta(minutes=100))
#también pordemos utilizar directamente el METODO todo necesario en el momento definiendo que DESDE(FROM) DATETIME IMPOTE(IMPORT) TIMEDELTA

from datetime import timedelta, date
print(date.today())
#como se verifica en la linea 28 se pueden traer varios METODOS a la vez

#para la creación de nuestro propio MÓDULO se genera un nuevo archivo de Python con cualquier nombre y la extensión .py (un archivo
# normal). En este caso creamos el archivo fmath.py

import fmath #importamos el módulo creado
fmath.add(1, 3) 
#En la linea 36 llamamos al MÓDULO y luego al METODO. Entre los parentesis ingresamos los ARGUMENTOS que solicita la FUNCIÓN. En este
#caso summamos 1 + 3

import fmath
fmath.substract(1, 5)
#ejecutamos el otro METODO del MÓDULO fmath que es SUBSTRACT que resta los números ingresados como ARGUMENTOS entre parentesis.


from fmath import add, substract
add(56, 62)
substract(102, 50)
# importando directamente los MÉTODOS desde el MÓDULO
#Python crea arbol llamado PYCACHE que es para funcionamiento interno, no se le presta atención

#Los módulos pueden ser descargados desde pypi.org. En la consola se debe poner el comando que figura debajo del nombre del archivo
#en la página (SIN colocar python delante) EJ: pip colorama install. PIP es el comando de CONSOLA que nos permite INSTALAR los módulos.

#para conocer la version de PYTHON se debe escribir >> python --version
#para conocer la version de PIP se debe escribir >> pip --version

#para actualizar PIP se debe escribir >> python -m pip install --upgrade pip

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + ("HOLA MUNDO"))

#ejemplo de como agregar color a las letras con el MÓDULO colorama todo sacado de la documentación vinculada al MÓDULO (pypi.org)

    





























