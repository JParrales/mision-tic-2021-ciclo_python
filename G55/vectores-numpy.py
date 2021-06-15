import numpy as np
from numpy.core.arrayprint import dtype_is_implied

lista1 = [1, 2, 3, 4, 5]
lista2 = [6,7,8,9,10]
lista3 = lista1 + lista2
# print(lista3)

# # tabla_3 = [i * 3 for i in lista3]
# # print(tabla_3)

arreglo = np.array(lista3)
# print(arreglo * 3)
# print(arreglo -10)

vector1 = np.array(lista1)
vector2 = np.array(lista2)
vector3 = np.array(lista3)

# print(vector1)
# print(type(vector1))


# lista_str = ''.join(str(lista3))
# print(lista_str)
# print(type(lista_str))

# lista = np.array(lista_str)
# print(lista)
# print(type(lista))

# print(vector1)
# print(vector2)
# print(vector3)

# print(vector1 + vector2)
# print(vector3.shape)

# print(vector3[1:3:21])

vector_ceros = np.zeros(4, dtype=int)
print(vector_ceros)

vector_unos = np.ones(5)
print(vector_unos)

vector_cimcos = vector_unos * 5
vector_tres = np.around(vector_ceros, decimals=0) + 3
print(vector_tres)




