import numpy as np


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(m)

# for i in range(len(matriz)):
#     print('[')
#     for j in range(len(matriz[i])):
#         print('{:s}'.format(matriz[i][j]))


matriz = np.array(m)
# print(matriz)
# print(matriz.shape)
# print(matriz[0][2])

# primera fila
# print(matriz[0:2,:2])

# """ matriz[fila, columna] """
# sub_m1 = matriz[0:2,:2]

# print(sub_m1)

lista = [list('abcd'), list('efgh'), list('ijkl')]
print(lista)

matriz = np.array(lista)
print(matriz)
print(matriz[:,1])
