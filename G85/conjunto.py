from typing import Union


conjunto = set(range(1, 6))
# print(conjunto)

a = {1, 2, 4, 3, 5, 7, 6}
b = {True, "Python", 2, 3.1416, (7, 10)}
c = {1, 7, 21, 2}

d = {'a', 'd', 'c', 'f'}

repetidos = {1,2,2,5,"hola", "hola", (7,1), (7,1)}
# print(repetidos)

# for elementos in repetidos:
#     print(elementos)

""" Union | """

a = {1,2,3,"python", 21, (7, 2)}
b = {'a', 'b', 100, "python", 21, (7,2)}

union_a_b = a | b

#print(union_a_b)

""" Inteseccion """

interseccion = a & b

#print(interseccion)


""" Diferencia Simetrica ^ """
simetrica_a = a ^ b
simetrica_b = b ^ a

# print(simetrica_a)
# print(simetrica_b)

""" Diferencia  - """

a = {1,2,3,"python", 21, (7, 2)}
b = {'a', 'b', 100, "python", 21, (7,2)}
diferencia_a = a - b
diferencia_b = b - a

# print(a)
# print(b)
# print(diferencia_a)
# print(diferencia_b)

for i in a:
    if type(i) == int:
        print(i)