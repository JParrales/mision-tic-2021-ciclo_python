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

print(vocales_cad)
print(vocales_list)
print(vocales_tupla)