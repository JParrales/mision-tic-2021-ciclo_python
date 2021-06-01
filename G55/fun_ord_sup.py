""" filter """

def multiplo_5(numero):
    if numero % 5 == 0:
        return True

numeros = [i for i in range(1, 51)]
# lista = [1,2,3,4,5,6,7,8,9,10]
# lista = [i for i in range(1, 11)]
# lista = list(range(1,11))
#print(numeros)

multiplos = filter(multiplo_5, numeros)
# print(multiplos)
# print(list(multiplos))

multiplos = list(filter(lambda numero: numero % 3 == 0, numeros))
#print(multiplos)

numeros = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
mayores_a_5 = list(filter(lambda i: i > 5, numeros))
print(mayores_a_5)