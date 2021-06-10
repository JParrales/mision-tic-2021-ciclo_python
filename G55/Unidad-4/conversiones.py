

cadena = str()
lista = list()
tupla = tuple()
diccionario = dict()

# print(cadena)
# print(lista)
# print(tupla)
# print(diccionario)

""" cadenas """

cadena = 'aeiou'
lista = list(cadena)
tupla = tuple(cadena)
# print(lista)
# print(tupla)

# print(cadena.index('i'))
# print(cadena[2])
# print(lista[2])
# print(tupla[2])

""" lista """

lista = ['a', 'e', 'i', 'o', 'u']

cadena = ''

for i in lista:
    cadena += i
# print(cadena)

# cadena_2 = ''.join(lista)
# print(cadena_2)

# tupla = tuple(lista)
# print(tupla)

str_list = str(lista)
# print(type(str_list))

# print(str_list)

""" Tuplas """

vocales = ('a', 'e', 'i', 'o', 'u')

cadena = ''.join(vocales)
lista = list(vocales)
# print(cadena)
# print(lista)

""" Diccionarios """

cadena = 'aeiou'


""" Ejercicio 1. Convertir las cadenas, listas y tuplas, a un diccionario de vocales. """

# Cadena.

indices = [i for i in range(len(cadena))]
elementos = [i for i in cadena]

# print(indices)
# print(elementos)

elementos_indices = list(zip(indices, elementos))
# print(elementos_indices)


# diccionario = dict(elementos_indices)
# print(diccionario)

diccionario_2 = dict(zip(range(len(cadena)), cadena))

# print(diccionario_2)

# lista
lista = ['a', 'e', 'i', 'o', 'u']

dicc_list = dict(zip(range(len(lista)), lista))

# print(dicc_list)

# tupla

tupla = ('a', 'e', 'i', 'o', 'u')

dicc_tupl = dict(zip(range(len(tupla)), tupla))

# print(dicc_tupl)

vocales = {0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u'}

cadena = "".join(vocales.values())
#print(cadena)

lista_valores = list(vocales.values())
lista_llaves = list(vocales.keys())
lista_items = list(vocales.items())

# print(lista_valores)
# print(lista_llaves)
# print(lista_items)

#print(cadena)

#tupla

tupla_valores = tuple(vocales.values())
tupla_llaves = tuple(vocales.keys())
tupla_items = tuple(vocales.items())

# print(tupla_valores)
# print(tupla_llaves)
# print(tupla_items)


conjunto = set('aeiou')
print(conjunto)

dict_conjunto = dict(zip(range(len(conjunto)), conjunto))
print(dict_conjunto)

set_valores = set(vocales.values())
set_llaves = set(vocales.keys())
set_items = set(vocales.items())

print(set_items)
print(set_valores)
print(set_llaves)