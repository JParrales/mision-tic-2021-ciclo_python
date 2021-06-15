import numpy as np
from numpy.core.fromnumeric import ptp

lista_de_listas = [
    [1, -4],
    [12, 3],
    [7, 5]
]

# print(lista_de_listas)

# matriz = np.array(lista_de_listas)
# print(matriz)

# lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(lista)
# matriz = np.array(lista)
# print(matriz)

# matriz_ceros = np.zeros((2,3), dtype=int)
# print(matriz_ceros)
# matriz_unos = np.ones((3,3))
# print(matriz_unos)

# print(matriz[1][1])
# print(matriz[1, 1])
# print(matriz[1, :3])

f1, f2, f3, f4, f5 = list(range(1, 6)), list(
    range(6, 11)), list(range(11, 16)), list(range(16, 21)), list(range(21, 26))

matriz_25 = np.array([f1, f2, f3, f4, f5])

print(matriz_25)

#primera fila
print("primera fila")
print(matriz_25[0], '\n')

#primera columna
print("primera columna")
print(matriz_25[:, 0], '\n')

#matriz3x3
print("submatriz")
print(matriz_25[1:4, 1:4])
