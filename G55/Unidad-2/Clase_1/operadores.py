""" Operadores """

#Comparacion

a = 1
b = 2
c = 3

# print(a == b)
# print(a == 1)
# print(a < b)
# print( a > b)
# print(a <= 1)
# print(a >= b)

# print(a != b)

# print(a < b < c)
# print(a < b > 0)

#Booleanos --> AND OR not

#and
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

#or
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

#not
# print(not True)
# print(not False)

sesion_iniciada = True
permisos_edicion = False
user_admin = False

#print(sesion_iniciada and permisos_edicion or user_admin)

a = 0
b = 5
c = 7

# print(c and b)
# print(b and c)
# print(c or b)
# print(b or c)

#Aritmeticos
a = 5
b = 3

# print(a % b)
# print(a // b)
# print(a / b)
# print(a ** b)

#Asignacion
# a = 1
# print(a)
# a = a + 1
# print(a)
# a = 1
# a += 1
# print(a)

# b = 3
# b = b - 1
# print(b)
# b = 3
# b -= 1
# print(b)

# c = 3
# c *= 5
# print(c)

#Identidad
a = 0
b = a
c = 2

# print(a is b)
# print(a == b)
# print(a is c)

d = None
list1 = [1]
list2 = [1]
a = 1
b = 1


print(list1 is list2) # la identidad del objeto
print(list1 == list2) # al valor del objeto
print(id(list1))
print(id(list2))
print(a is b)
print(a == b)
print(id(a))
print(id(b))