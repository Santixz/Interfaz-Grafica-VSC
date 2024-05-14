#Practicas de python
import operator
#import math
#x = 10
#y = 20
#z = 30
#suma = x + y
#print (suma)
#segsuma = z + y
#print (segsuma)
#tersuma = x + z
#print (tersuma)
#cuartsuma = x + y + x + z 
#print (cuartsuma)
#quintsuma = x + y - z + x
#print (quintsuma)
#multiplicacion = x * y * z
#print (multiplicacion)
#segunmulti = x * z / y
#print (segunmulti)
#sumdiv = x + y / y + z 
#print (sumdiv)
#ola = x + y **z
#print (ola)
#print (math.sqrt(9))
#print (math.sqrt(732))
#print (math.sqrt(87))
#print (math.sqrt(10))

#print (x < z)
#print (x < y)
#print (y < x)

#a = "alexa"
#b = "alexa"
#print (a < b)
#print (a > b)

#Operacion
#impuesto = input ("Digite el valor de impuesto(%):")
#calculo_de_impuesto = int (precio) * int (impuesto) / 100
#print (f"La suma del impuesto es:{calculo_de_impuesto}")

#Notas

#Quimica = input ("Digite su nota final de quimica: ")
#Biologia = input ("Digite su nota final de biologia: ")
#Español = input ("Digite su nota final de español: ")
#Ingles = input ("Digite su nota final de ingles: ")
#sumanotas = int (Quimica) + int (Biologia) + int(Español) + int(Ingles)
#promedio_final = sumanotas / 4
#print (f"Su promedio de nota final es de:{promedio_final}")

#Elementos tecnologicos

#Computador_asus = input ("Digite el precio del Computador: ")
#iphone = input ("Digite el precio del Iphone: ")
#televisor_55_pulgadas = input ("Digite el precio del Televisor: ")
#xbox = input ("Digite el precio del Xbox: ")
#motolola = input ("Digite el precio del Motorola: ")
#precio_total = int (Computador_asus) + int (iphone) + int (televisor_55_pulgadas) + int (xbox) + int (motolola)
#print (f"El precio total de todo es:{precio_total}")
#descuento = precio_total > 2000000
#print (f"El descuento es; {descuento} ")
#precio_descuen = precio_total * 0.85
#print (f"El precio con descuento es de: {precio_descuen}")
#precio_final = precio_descuen * 1.19
#print (f"El precio final es de: {precio_final}")

a = 3.5
b = 2.5
c = 20
frase = ("Hola mundo!")
frase2 = ("Buenas Tardes")
print (frase2)
frase3 = ("Bon Jour!")
boleano = 1 < 10
print (boleano)
suma = a + b
print (suma)
print (2+2)
print (2*2)
print (3**8)
x, y, z = 2 , 4 , 6
print (x, y, z)
a, b, c = ("hola"), 2.5, 3
print (a, b, c)

numero = 5
obj = type (numero)
print (obj)

float = 78.50
obj = type (float)
print (obj)

frase = ("Buenos Dias")
obj = type (frase)
print (obj)

boleano2 = 1 > 100
obj = type (boleano2)
print (obj)

f = 100
print (f + 10)

str = ("Colegio")
str_len = len(str)
print (str_len)

saludo = ("Hello")
print (saludo [1])

#listas

banderas = ["Amarillo", 2, 0.5]
print (banderas)

nombres = ["Santiago", "Juan David", "Alejandro", "Soponcio"]
print (nombres[0])
print (nombres[1]) 
print (nombres[2]) 
print (nombres[3])

nombres.append ("Nacional Jose")
print (nombres)

n = 10 + 2
print (n)

n = operator.add (10, 2)
print (n)

l = operator.add (15, 13)
print (l)

m = operator.add (10, 30)
print (m)

p = operator.sub (60, 57)
print (p)

k = operator.mul (20, 30)
print (k)

ñ = operator.truediv (4, 2)
print (ñ)

h = operator.pow (9, 10)
print (h)