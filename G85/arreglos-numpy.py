import numpy as np


lista1 = [1, 2, 3, 4, 5]
lista2 = [6,7,8,9,10]
lista3 = lista1 + lista2
# print(lista1 + lista2)
# print(lista3 * 3)
# tabla_3 = [i*3 for i in lista3]
# print(tabla_3)

# arreglo = np.array(lista3)
# print(arreglo * 3)
# print(arreglo - 9)

vector1 = np.array(lista1)
vector2 = np.array(lista2)
vector3 = vector1 + vector2
# print(vector1)
# print(vector2)
# print(vector1 + vector2)

# print( vector1[1:3])
# print(vector2[:4])
# print(vector3[:5:2])

vector_zeros = np.zeros(5)
print(vector_zeros)
vector_ones = np.ones(5)
print(vector_ones)

vector_5 = vector_zeros + 5
v_5 = vector_ones * 5

print(vector_5, v_5)