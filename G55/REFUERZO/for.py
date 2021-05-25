# for variable in objeto_iterable:

string = "Python"
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = tuple(range(10, 20))
diccionario = {
    (1, 2): 'P',
    (2, 3): 'Y',
    'letra 3': 'T',
    'letra 4': 'H',
    'letra 5': 'O',
    'letra 6': 'N'
}

# for llave, valor in diccionario.items():
#     print(llave, valor)
a = 0
for i in lista:
    a += i
    print(a, i)

