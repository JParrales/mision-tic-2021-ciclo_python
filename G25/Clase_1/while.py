n = 5
# while n > 0:
#     print(n)
#     n = n - 1

# print('Despegue!')

num = 1

# while num <= 10:
#     print(num)
#     num += 1

# lst = []
# if lst:
#     print("con elementos")
# else:
#     print("vacia")

rango = 1

# a = int(input('Ingrese inicio del rango: '))
# b = int(input('Ingrese final del rango: '))

pares = []
impares = []

# while a <= b:

#     if a % 2 == 0:
#         pares.append(a)
#     else:
#         impares.append(a)
#     a += 1
#     print(pares)
#     print(impares)

"""
*
**
***
****
*****

"""

fila = 1

# while fila <= 5:
#     columna = 1

#     while columna <= fila:
#         print('*', end='')
#         columna += 1
#     print()
#     fila += 1

i = 1

# while i <= 5:
#     print("*"*i)
#     i += 1

numeros = []

num = 1

while num <= 10:
    numeros.append(num)
    #print(numeros)
    num += 1

indice = 0

while indice < len(numeros):
    print(numeros[indice])
    indice += 1

print('---------------------------')
for numero in numeros:
    print(numero)