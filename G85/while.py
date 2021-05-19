# a = 1
# print(a)
# a += 1
# print(a)

# n = 1
# pares = []
# impares = []
# while len(pares) < 10:

#     if n % 2 != 0:
#         impares.append(n)
#     else:
#         pares.append(n)

#     n += 1

# print(pares)
# print(impares)


""" 
*
**
***
****
*****
"""


fila = 1
while fila <= 5:
    i = 1
    while i <= fila:
        print('*', end='')
        i += 1
    print()
    fila +=1

i = 1
while i<=5:
    print("*"*i)
    i += 1 