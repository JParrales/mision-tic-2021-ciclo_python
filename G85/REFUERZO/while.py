# a = 0

# while a <= 10:
#     if a == 8:
#         print('ocho')
#         pass
#     print(a)
#     a += 1
# else:
#     print('Bucle finalizado')

"""
Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números impares desde 1 hasta ese 
número separados por comas.
"""

def conteo():
    numero = int(input("Ingrese un numero: "))
    count = 1

    while count <= numero:

        if numero == count:
            print(count)
            break
        if numero <= count + 1:
            print(count)
            break
        

        print(count, end=', ')
        count += 2

    else:
        print('No ingresó un numero positivo')

conteo()