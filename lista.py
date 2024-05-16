lista = ["Colombia", "Uruguay", "Alemania", "Argentina", "Portugual"]

lista.append ("Brasil")

eqipcham = ["Real Madrid", "Barcelona", "Atalanta", "Juventus", "Altletico Nacional"]

accesorios = ["Celular", "Xbox", "Televisor", "Computador", "Audifonos"]

accesorios.append ("Microondas")
accesorios.append ("Nevera")
accesorios.remove ("Microondas")
# .sort Para poner en orden alfabetico
accesorios.sort()
lista.sort()
lista3 = lista + accesorios
lista3.sort ()
lista4 = lista3 + eqipcham
lista4.sort ()

# Tupla es una variable con unos items, se crean similar a las listas y la tupla se pone con (), y no repite items.
tupla = ("Perro", "Gato", "Ratón", "Futbol", "Futbol Americano", "Pez")

# Conjuntos = set es lo mismo pero se utilizan {}

barrios = {"Suba", "Aures", "La Gaitana", "Quirigua"}
numeros = {1, 2, 3, 4, 5, 6}
color = {"Negro", "Blanco", "Azul", "Verde"}

colores = {"Amarillo", "Azul", "Rojo"}
colores.add ("Naranja")
colores.remove ("Amarillo")

mascotas = {"Perros", "Gatos", "Hamster", "Pajaros", "Loros"}
salvajes = {"Leon", "Tigre", "Leopardo", "Hipopotamo", "Serpiente"}
reptiles = {"Tortugas", "Lagartos", "Cocodrilos", "Caimanes"}
conjuntomascotas = mascotas.union (salvajes, reptiles)

# Diccionario es con {} se definen los datos, y se ponen los 2 puntos

Diccionario = {"Marca":"Ford", "Modelo":"Mustang", "Año": 1950 }
Estudiante = {"Nombre":"Santiago", "Apellido":"Hurtado Castellanos", "Email":"s,hurtadocompu2017@gmail.com", "Telefono":"3057612188"}
xj6 = {"Nombre":"Yamaha XJ6", "Cilindraje":599, "Velocidad Maxima": 253, "Modelo": 2007}
#Forma de adiccionar datos
Entrada =  {"18/10/2007": "10:00" }
Entrada["Lugar"] = "Bogotá D.C"
xj6["Peso"] = 210
Estudiante["Direccion"] = "Cra 53B #76 - 39"
# .pop es para borrar datos
xj6.pop ("Peso")

#Condicionales de Python.
x = 30
y = 300
#Estar pendiente del orden y la concordancia de todo.
if x < y: 
    print 

a = 1000
b = 30
c = 23

if a > c:
    print
if c < b:
    print 


h = 50
g = 50

if h > g :
    print
elif h == g :
    print

ab = 10
bc = 10
cd = 15
de = 15

if ab > cd:
    print 
elif ab == bc:
    print
if bc > de:
    print 
elif cd == de:
    print 
if ab > de:
    print 
elif cd > ab:
    print 

# if y elif

a = 100
b = 35
if b > a: 
    print 
elif a == b:
    print 
else: 
    print 

c = 200
d = 50
if d > c: 
    print
elif c == d:
    print 
else: 
    print 

e = 231
f = 34
if f > e: 
    print 
elif f == e:
    print 
else: 
    print 

a = 100
b = 50
if b > a:
    print
else:
    print

c = 150
d = 15
if d > c:
    print
else:
    print

e = 300
f = 30
if f > e:
    print
else:
    print
abcd = 2
bcde = 18
if abcd > bcde:
    print 
else:
    print
#Hacer una calculadora con division y con 0 aparece sintax error
    
a = int(input("¿Que numero quieres dividir?: "))
b = int(input("¿Por cual numero lo quieres dividir?: "))
if b == 0:
    print("Error - No se puede dividir entre cero")
resultado = float (a) / float (b)
print (f"Tu resultado es: {resultado}")

#Hacer un programa donde me diga el numero es par o impar
num = int(input("Digite un numero: "))
if num % 2 :
    print ("Su numero es impar")
else:
    print ("Su numero es par")