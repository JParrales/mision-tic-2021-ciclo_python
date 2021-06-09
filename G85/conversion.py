cadena = str()
lista = list()
tupla = tuple()
dicc = dict()

# print(cadena)
# print(lista)
# print(tupla, dicc)

""" Cadenas """

cadena = 'aeiou'
lista = list(cadena)
# print(cadena)
# print(lista)

tupla = tuple(cadena)
# print(tupla)

""" Listas """

vocales = ['a', 'e', 'i', 'o', 'u']

cadena = str(vocales)
# print(cadena)

cadena = str()

for vocal in vocales:
    cadena += vocal
# print(cadena)

cadena2 = ''.join(vocales)
# print(cadena2)

tupla = tuple(vocales)
# print(tupla)

""" Tuplas """

vocales = ('a', 'e', 'i', 'o', 'u')

cadena = ''.join(vocales)
# print(cadena)

lista = list(vocales)
# print(lista)


""" Diccionarios """

cadena = 'aeiou'
lista = ['a', 'e', 'i', 'o', 'u']
tupla = ('a', 'e', 'i', 'o', 'u')

vocales_cad = dict(zip(range(len(cadena)), cadena))
#print(vocales_cad)

# cantidad_elementos = len(cadena)
# print(cantidad_elementos)
# rango = list(range(cantidad_elementos))
# print(rango)
# ziip = dict(zip(rango, cadena))
# print(ziip)

vocales_list = dict(zip(range(len(lista)), lista))
vocales_tupl = dict(zip(range(len(tupla)), tupla))

print(vocales_cad)
print(vocales_list)
print(vocales_tupl)