
from typing import ValuesView


abcdario = {i - 64: chr(i) for i in range(65, 91)}
# print(abcdario)

llaves = list(abcdario.keys())
#print(llaves)
valores = list(abcdario.values())
#print(valores)
items = list(abcdario.items())
#print(items)

# numeros = list(range(1,11))
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numeros)

# numeros.append(25)
# print(numeros)
# #numeros.append(-32)
# print(numeros.append(-32))

# nombres = ['andres', 'heynar', 'italo', 'juan', 'yisney']

# revueltos = ''.join(nombres)
# juntos = '-'.join(nombres)

# print(revueltos)
# print(juntos)


cuadrados = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
             6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

llaves = list(cuadrados.keys())
valores = list(cuadrados.values())
items = list(cuadrados.items())

print(llaves)
print(valores)
print(items)

# recorrer diccionario

for i in valores:
    print(i)