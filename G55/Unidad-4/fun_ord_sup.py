""" filter """


def multiplo_5(numero):
    if numero % 5 == 0:
        return True


numeros = [i for i in range(1, 51)]
# lista = [1,2,3,4,5,6,7,8,9,10]
# lista = [i for i in range(1, 11)]
# lista = list(range(1,11))
# print(numeros)

multiplos = filter(multiplo_5, numeros)
# print(multiplos)
# print(list(multiplos))

multiplos = list(filter(lambda numero: numero % 3 == 0, numeros))
# print(multiplos)

numeros = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
mayores_a_5 = list(filter(lambda i: i > 5, numeros))
# print(mayores_a_5)


""" MAP """


def cuadrado(numero):
    return numero ** 2


numeros = [i for i in range(1, 6)]
# print(numeros)

cuadrados = list(map(cuadrado, numeros))
cuadrados_for = [i*i for i in numeros]
# print(cuadrados)
# print(cuadrados_for)

vocales = ['a', 'e', 'i', 'o']
repeticion = ['1', '3', '6', '2', '4', '8']
otra_lista = [2,1,21,1]
vocales_repeticion = list(
    map(lambda vocales, repeticion, v2: vocales + repeticion *v2, vocales, repeticion, otra_lista))
#print(vocales_repeticion)

def vocales_por_numeros(vocales, repeticion):
    return vocales*repeticion


""" reduce """

from functools import reduce

numeros = list(range(1, 5))
# print(numeros)

def suma(a, b):
    return a + b

#print(reduce(suma, numeros))
proceso = suma(suma(suma(1,2), 3),4)
#print(proceso)

#print(reduce(lambda a, b: a*b, numeros))


lista = ['python', 'java', 'ruby', 'c']

resultado = reduce(lambda a='', e='': a + " " + e, lista)
#print(resultado)

""" zip """

paises = ["CHINA", "JAPON", "USA"]
covid = [1391, 1364, 327, 264]

paises_covid = zip(paises, covid)

print(paises_covid)
print(tuple(paises_covid))