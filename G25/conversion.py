from typing_extensions import runtime


cadena = str()
lista = list()
tupla = tuple()
diccionario = dict()

# print(cadena)
# print(lista)
# print(tupla)
# print(diccionario)

""" cadenas """

# cadena = 'aeiou'
# lista = list(cadena)
# print(cadena)
# print(lista)

# tupla = tuple(cadena)
# print(tupla)

# tuplas_varias = (cadena, tupla)
# print(tuplas_varias)

""" lista """

vocales = ['a', 'e', 'i', 'o', 'u']

cadena = ''.join(vocales)

cadena2 = ''

# for vocal in vocales:
    
#     cadena2 += vocal+'-'
# print(cadena)

# tupla = tuple(vocales)
# print(tupla)

""" Tuplas """

# vocales = ('a', 'e', 'i', 'o', 'u')

# cadena = ''.join(vocales)

# print(cadena)

# lista = list(vocales)

# print(lista)

""" diccionarios """

cadena = 'aeiou'
lista = ['a', 'e', 'i', 'o', 'u']
tupla = ('a', 'e', 'i', 'o', 'u')

vocales_cad = dict(zip(range(len(cadena)), cadena))
vocales_list = dict(zip(range(len(lista)), lista))
vocales_tupla = dict(zip(range(len(tupla)), tupla))

# print(vocales_cad)
# print(vocales_list)
# print(vocales_tupla)

vocales = {0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u'}

dict_to_string = "".join(vocales.values())
print(dict_to_string)

tupla_llaves = tuple(vocales.keys())
tupla_valores = tuple(vocales.values())
tupla_items = tuple(vocales.items())
# print(tupla_llaves)
# print(tupla_valores)
# print(tupla_items)

lista_llaves = list(vocales.keys())
lista_valores = list(vocales.values())
lista_items = list(vocales.items())

print(lista_llaves)
print(lista_valores)
print(lista_items)

