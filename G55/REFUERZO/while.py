# variable = True

# while variable:
#     numero = 1
#     numero += 1
#     print(numero, 'Infinito')
#     numero += 1
#     variable = False

# a = 0

# while a <= 10:
    
#     if a == 8:
#         print('ocho')
#         break
    
#     print(a)
#     a += 1
# else:
#     print("flinalizó el programa")


"""
Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números impares desde 1 hasta ese 
número separados por comas.
"""

numero = int(input('Ingrese un número: '))

contador = 1

while contador <= numero:

    if numero == contador:
        print(contador)
        break
    if numero <= contador + 1:
        print(contador)
        break

    print(contador, end=', ')
    contador += 2
else:
    print('No ingresó un número positivo')