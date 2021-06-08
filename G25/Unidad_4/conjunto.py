

conjunto = set(range(1, 6))
# print(conjunto)

s = {1, 2, 3, 4, 5}
b = {True, "Python", 2, 3.1416, (7, 10)}

# print(s)
# print(b)

repetidos = {1, 2, 2, 5, "hola", "hola", (7, 10), (7, 10)}
# print(repetidos)

# for elemento in repetidos:
#     print(elemento)

a = {1, 2, 3, "hola", 21, (7, 12)}
b = {'a', 'b', 100, "hola", 21, (7, 12)}

""" Union | """

union_a_b = a | b
union_b_a = b | a
# print(union_a_b)
# print(union_b_a)

""" Interseccion & """

interseccion = a & b
# print(interseccion)

""" Diferencia - """

diferencia_a_b = a - b
diferencia_b_a = b - a
# print(diferencia_b_a)
# print(interseccion)
# print(b)

""" Diferencia simétrica ^ """
simetrica_a = a ^ b
simetrica_b = b ^ a
# print(simetrica_a)
# print(simetrica_b)
# print(a)
# print(b)

""" otros operadores """
a = {1, 2, 3, "hola", 21, (7, 12)}
b = {'a', 'b', 100, "hola", 21, (7, 12)}

# print('hola' in b)
# print(100 not in a)

""" ------------------------- """

conjunto1 = {1, (3, 4), 9.2}
conjunto2 = {1, 9.2}
conjunto3 = {(3, 4), 9.2, 1}

# print(conjunto1 == conjunto3)
# print(conjunto1 != conjunto2)
# print(conjunto1 > conjunto3)
# print(conjunto1 > conjunto2)
# print(conjunto1 >= conjunto3)

""" FUnciones """

c1 = {7, 3, 21, 9, 2}
c1 = {"Hola", "Adios", "Nombre", "Edad"}
# print(len(c1))
# print(max(c1))
# print(min(c1))
# print(sum(c1))


""" Metodos """

c = {1, 2, 3}
# c.add(4)
# c.remove(3)
# c.discard(2)
# c.pop()
# print(c)
d = c.copy()
d.clear()
# print(d)
d = {2, 100}
# print(c.union(d))
# print(c.intersection(d))
# print(c.difference(d))
# print(d.difference(c))
# print(c.symmetric_difference(d))

# c.update(d)
# print(c)

conjunto = {12, "Hola", 32.21, 7}

for dato in conjunto:
    if dato == 7:
        print(f"Tenemos el dato {dato} en el conjunto")
        
