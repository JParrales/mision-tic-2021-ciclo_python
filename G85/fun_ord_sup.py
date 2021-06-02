"""  filter """

def multiplo_5(numero):
    if numero % 5 == 0:
        return True

numeros = [i for i in range(1, 51)]
#print(numeros)

multiplos = list(filter(multiplo_5, numeros))
multiplos_2 = list(filter(lambda num: num%2 ==0, numeros))

# print(multiplos)
# print(multiplos_2)

numeros = [1, 4, 5, 6, 9, 13, 19, 21]
impares = [i for i in numeros if i % 2 != 0]
# print(impares)
impares_fil = list(filter(lambda i: i%2 != 0, numeros))

# print(impares_fil)

numeros= (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
mayores_5 = list(filter(lambda i: i>5, numeros))
#print(mayores_5)


"""  MAP """

def cuadrado(numero):
    return numero ** 2


nums = tuple(range(1, 6))
print(nums)

cuadrados = list(map(cuadrado, nums))
print(cuadrados)

cuadrados_map = tuple(map(lambda i: i*i, nums))
print(cuadrados_map)

vocales = ['a', 'e', 'i', 'o', 'u']

vocales_mult = list(map(lambda v, n: v*n, vocales, nums))
print(vocales_mult)