from typing import List
import numpy as np

# crear vector de 5 elementos

lista = [25, 12, 15, 66, 12]
vector = np.array(lista)
# print(vector)

# print(vector + 1)
# print(vector * 5)

# print(np.sum(vector))
# print(np.mean(vector))

# print(vector + vector)

""" INDICES """

# print(vector)
# print(vector[3])
# print(vector[1:4])
# print(vector[1:])
# print(vector[:4])
# print(vector[:])

# vector4 zeros

v_ceros = np.zeros(5)
# print(v_ceros)
v_unos = np.ones(5)
# print(v_unos)

v_numeros_dos = np.zeros(3) + 2
# print(v_numeros_dos)
v_nomeros_5 = np.ones(3) * 5
# print(v_nomeros_5)


""" Matrices """

lista_de_listas = [[1, -4], [12, 3], [7, 5]]
matriz = np.array(lista_de_listas)
#print(matriz)

# dimensiones = (3,2)
# matriz_ceros = np.zeros(dimensiones)
# print(matriz_ceros)
# matriz_ones = np.ones(dimensiones)
# print(matriz_ones)

# Ejercicio:
# Crear una matriz de 4x9, inicializada en 0.5

matriz_4x9 = np.ones((4, 9)) * 0.5
# print(matriz_4x9)

lista = [[1, -4],
         [12, 3],
         [7, 5]]

a = np.array(lista)
# print(a)

# # print(a[0, 1])
# # print(a[2,1])

# print(a[1,:])
# print(a[:,0])

# print(a[:2,:]) #submatirz 2x2 primeras 2 filas
# print(a[-2:,:]) #submatirz 2x2 ultimas 2 filas

lista = [[1, -4],
         [12, 3],
         [7, 5]]
print(a)

a = np.array(lista)

a[0,1]=3

a[:,0] = 7

a[1,:] = a[1,:] * 5

a = a + 1
print(a)
