#Numeros 1 al 10

# a = 1
# print(a)
# a += 1
# print(a)

# while a <= 10:
#     print(a)
#     a += 1

# print("Ciclo finaliza, el valor de a es: {a}")
# print(f"Ciclo finaliza, el valor de a es: {a}")

# a = 0
# var_1 = 3
# var_2 = 5

# while a != -1:
#     a = int(input('Ingrese una opcion: '))

#     if a == 1:
#         print(f'{var_1} + {var_2} = {var_1 + var_2}')
#     elif a == 2:
#         print(f'{var_1} - {var_2} = {var_1 - var_2}')
#     elif a == 3:
#         print(f'{var_1} / {var_2} = {var_1 / var_2}')
#     elif a == 4:
#         print(f'{var_1} * {var_2} = {var_1 * var_2}')
#     else:
#         print("Ingrese una opcion correcta")

# numero = 1

# while numero <= 10:
#     print(numero)
#     numero += 1

n = 1
pares = []
impares = []

while n <= 20:

    if n % 2 != 0:
        impares.append(n)
    else:
        pares.append(n)
    
    n += 1

print(pares)
print(impares)