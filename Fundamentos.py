def nuevoTema(tema):
    #pass (palabra para dejar vacio y no marque error.)
    print("\n==== ", tema, " ====\n")


#Esto es un comentario de una línea.
'''Este es un comentario de varias líneas.'''
nuevoTema("O P E R A D O R E S   A R I T M E T I C O S ") #Utilizamos funcion
print("==== O P E R A D O R E S   A R I T M E T I C O S ===")
print("Operador division entera(10 // 3): " , 10 // 3)
print("Operador potencia (5 ** 3): " , 5 ** 3) #Operador ** 

#Actividad : Imprimir la tabla de verdad de los operadores lógicos.
print("==== O P E R A D O R E S   L O G I C O S ====")

#Operdor AND
print("Operador and (True and False): ", True and False)
print("Operador and (False and True): ", False and True)
print("Operador and (True and True): ", True and True)
print("Operador and (False and False): ", False and False)

#Operador OR
print("Operador or (True or False): ", True or False)
print("Operador or (False or True): ", False or True)
print("Operador or (True or True): ", True or True)
print("Operador or (False or False): ", False or False)

#Operador NOT
print("Operador not (True not False): ",  not False)
print("Operador not (False not True): ",  not True)


#Actividad: Agregar los demas operadores de comparacion
print("=== O P E R A D O R E S   D E   C O M P A R A C I O N ===")
print("2==3", 2==3) #Operador igual.
print("2<3", 2<3) #operador menor que.
print("2>3", 2>3) #operador mayor que.
print("2<=3", 2<=3) #operador menor igual que.
print("2>=3", 2>=3) #operador mayor igual que.
print("2!=3", 2!=3) #operador diferente que.


nuevoTema("Variables")
variable1 = 10
variable2 = 6.2456
variable3 = "Juancho"
dosPalabras = "Hola"
dos_palabras = "Hello"

print(variable1, variable2, variable3, dos_palabras, dosPalabras)
a, b, c = 10, 5.16, "Palabra"
print(a, b, c)

#Siguiente actividad
nuevoTema("E N T E R O S")
w = 2
x = 5
y = -1
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("F L O T A N T E S")
x = 1297.50
print(x,type(x))

y = 0.5637939
print(y, type(y))


nuevoTema(" N U M E R O S   C O M P L E J O S")
x = -46j
y = 12 + 45j
z = 2j

print(x, type(x))
print(y, type(y))
print(z, type(z))



nuevoTema(" B O O L E A N O ")
lis = [8]
print(lis, "es", bool(lis))
t = ()
print(t, "es", bool(t))
new = "hello"
print(new, "es", bool(new))
num = 99
print(num, "es", bool(num))
comp = 1 + 0j
print(comp, "es", bool(comp))
val = None #None equivale a NULL
print(val, "es", bool(val))

nuevoTema("L I S T A S ") #No son arreglos
a = [10, 20.5, "Python list"]
print(a)
print(a[1])
a[0] = "Hola"
print(a)

nuevoTema("T U P L A S")
t = (25, "Tupla", 1 + 10j, 3.1416)
print(t)
print(t[2])
print("t[1:4]: ", t[1:4])
#t[1]=34 operación no válida en tuplas.



nuevoTema("Cadenas")
cadena1 = "Cadenas con comillas dobles"
cadena2 = 'Cadena con comillas simples'

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))


cadenaMultilinea = '''Esta es una cadena de varias lineas   con     tabulares       y   saltos  de  linea'''

print(cadenaMultilinea)
print("Segmentacion de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1 = "Hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena5 = cadena4.upper()
print(cadena5)