""" Filter """


def multiplo_5(numero):
    if numero % 5 == 0:
        return True

numeros = [i for i in range(1, 51)]
#print(numeros)

multiplos = filter(multiplo_5, numeros)
#print(multiplos)
#print(list(multiplos))
#print(tuple(multiplos))
multiplos = list(filter(lambda numero: numero%5 == 0, numeros))
#print(multiplos)

numeros = [1, 4, 5, 6, 9, 13, 19, 21]
impares = [i for i in numeros if i % 2 != 0]
#print(impares)
impares_fil = list(filter(lambda i: i%2 != 0, numeros))
#print(impares_fil)

numeros = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
mayores_a_5 = list(filter(lambda i: i > 5, numeros))
#print(mayores_a_5)


""" MAP """

def cuadrado(numero):
    return numero ** 2


nums = [i for i in range(1, 6)]
# print(nums)
# cuadrados = [i*i for i in nums]
# print(cuadrados)
# cuadrados_map = list(map(lambda i: i*i, nums))
# print(cuadrados_map)

vocales = ['a', 'e', 'i', 'o', 'u']

vocales_posicion = list(map(lambda v, n: v*n, vocales, nums))

#print(vocales_posicion)


""" Reduce """

from functools  import reduce

numeros = list(range(1,5))
#print(numeros)

def suma(a, b):
    return a + b

#print(reduce(suma, numeros))

proceso = suma(suma(suma(1,2), 3), 4)

# print(proceso)

# print(reduce(lambda a, b: a + b, numeros))


""" zip """

paises = ["china", "india", "USA", "colombia"]
poblaciones = [1391, 1364, 327, 264]

poblacion_paises = zip(paises, poblaciones)
print(poblacion_paises)

print(list(poblacion_paises))