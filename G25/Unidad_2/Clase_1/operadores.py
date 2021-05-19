""" Operadores """

#Comparacion
a = 1
b = 2
c = 3

# print(a == b)
# print(a == 1) 
# print(a < b)
# print(a > b)
# print(a <= 1)
# print(a >= b)

#print(a != 1)

# print(a < b < c)
# print(a < b > 0)

#Booleanos
#AND  ---> (x and y)
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# OR ---> (x or y)
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# NOT
# print(not True)
# print(not False)

inicio_sesion = True
permisos_edicion = False
es_admin = True

#print(inicio_sesion and (permisos_edicion or es_admin))

a = 0
b = 1

# print(a and b)
# print(b and a)

# print(b and c)
# print(c and b)

#Aritmeticos
x = 5
y = 3

# print(y % x)
# print(y // x)
# print(y / x)
# print(x ** y)

# Asignacion

a = 1
# print(id(a))
# a = a + 1
# print(a)
# a = 1
# a += 1
# print(a)
# print(id(a))

# b = 3
# b -= 1 # b = b - 1
# print(b)

# a = 3
# a *= 5
# print(a)

# Operadores de identidad

a = 1
b = a
c = 2

# print(a is b)
# print( a is c)

# d = None
# print( d is None)

# print(a is None)
# print(a is not None)

fruta = 'banana'

#print('ana' in fruta)

""" print(fruta)
fruta_mayus = fruta.upper()
print(fruta_mayus)

print(fruta.find('ana'))

print(fruta_mayus.lower()) """

# cadena = r"Hola\nMundo"  
# print(cadena)

cadena = "un uno, un dos, un tres"
#print(cadena.count("u"))

nombre = "remplaza el string PYTHON"
print(nombre.replace("PYTHON", "java"))
