

conjunto = set(range(1, 5))
# print(conjunto)

s = {1, 2, 3, 4, 5}
b = {True, "Python", 2, 3.1416, (7, 10)}

# print(s)
# print(b)

repetidos = {1, 2, 2, 5, "hola", "hola", (7, 10), (7, 10)}

# print(repetidos)

# for i in repetidos:
#     print(i)

a = {1, 2, 3, "hola", 21, (7, 12)}
b = {'a', 'b', 100, "hola", 21, (7, 12)}

""" Union | """

union = a | b

# print(union)

""" Interseccion & """

interseccion = a & b
# print(interseccion)


""" Diferencia - """

diferencia_a_b = a - b
diferencia_b_a = b - a
# print(a)
# print(b)
# print(diferencia_a_b)
# print(diferencia_b_a)

""" Diferencia simétrica ^ """

simetrica_a = a ^ b
simetrica_b = b ^ a

# print(a)
# print(b)
# print(simetrica_a)
# print(simetrica_b)
# print(interseccion)


""" Operadores de pertenencia """
a = {1, 2, 3, "hola", 21, (7, 12)}
b = {'a', 'b', 100, "hola", 21, (7, 12)}
# print('hola' in b)
# print((7, 12) in a)


""" operadores relacionales """

conjunto1 = {1, (3, 4), 9.2}
conjunto2 = {1, 9.2}
conjunto3 = {(3, 4), 9.2, 1}


# print(conjunto1 == conjunto3)
# print(conjunto1 != conjunto2)
# print(conjunto1 > conjunto3)
# print(conjunto1 > conjunto2)
# print(conjunto1 >= conjunto3)
# print(conjunto1 > conjunto2)

""" FUnciones """

c1 = {7, 3, 21, 9, 2}
# print(len(c1))
# print(max(c1))
# print(min(c1))
# print(sum(c1))


""" Metodos """

conjunto = {12,"python", 32.21, 7}

for dato in conjunto:
    if dato == 7:
        print(f"Tenmos el dato {dato} en el cojunto.")

