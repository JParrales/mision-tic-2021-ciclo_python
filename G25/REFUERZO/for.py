# for variable in objeto_iterable:

# string = 'Python'
# lista = list(range(1, 10))
# tupla = tuple(range(1, 10))
diccionario = {
    (1, 2): 'x, y',
    (3, 4): 'i, j',
    'llave 2': 'T',
    'llave 3': 'H',
    'llave 4': 'O',
    'llave 5': 'N'
}

# print(string)
# print(lista)
# print(tupla)
# print(diccionario)

# print()

for key, values in diccionario.items():
    print(key, ':', values)
    #print(key)
