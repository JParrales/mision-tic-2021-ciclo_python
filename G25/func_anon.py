""" Operadores encadenados """

menor = 1 < 2 and 2 < 3
menor_2 = 1 < 2 < 3
mayor = 3 > 2 > 1

# print(menor)
# print(menor_2)
# print(mayor)

""" Comprobar si un numero se encuentra entre 0 y 100 """

numero = 27

# if numero >= 0 and numero <= 100:
#     print(f"El número {numero} se encuentra entre 0 y 100")
# else:
#     print(f"El número {numero} no se encuentra entre 0 y 100")


# if 0 <= numero <= 100:
#     print(f"El número {numero} se encuentra entre 0 y 100")
# else:
#     print(f"El número {numero} no se encuentra entre 0 y 100")


""" lambda """

#lambda argumentos: expresion

nombre = 'ana'

def palindromo_func(palabra):
    return palabra == palabra[::-1]

#print(palindromo_func(nombre))

def cuadrado(numero):
    resultado = numero * numero

    return resultado

def cuadrado_v2(numero):
    return numero ** 2

def cuadrado_v3(numero): return numero ** 2

numero  = cuadrado(3)
numero_v2 = cuadrado_v2(3)
numero_v3 = cuadrado_v3(3)

# print(numero)
# print(numero_v2)
# print(numero_v3)

numero_al_cuadrado = lambda num: num**2

# print(numero_al_cuadrado)
# print(numero_al_cuadrado(5))

palindromo = lambda palabra: palabra == palabra[::-1]

#print(palindromo(nombre))

#Numero impar

impar = lambda num: num%2 !=0

#print(impar(2))

#revertir string

revertir = lambda palabra: palabra[::-1]
#print(revertir('Python'))

suma = lambda x, y: x + y

print(suma(2, 5))