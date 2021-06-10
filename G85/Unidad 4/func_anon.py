""" Operadores Encadenados. """

menor = 1 < 2 and 2 < 3
menor_2 = 1 < 2 < 3
mayor = 3 > 2 > 1

# print(menor)
# print(menor_2)
# print(mayor)

numero = -85

# if numero >= 0 and numero <= 100:
#     print(f"El {numero} se encuentra entre 0 y 100")
# else:
#     print(f"El {numero} fuera de rango > forma 1")

# if 0 <= numero <= 100:
#     print(f"El {numero} se encuentra entre 0 y 100 > forma 2")
# else:
#     print(f"El {numero} fuera de rango")


""" lambda """

#lambda argumentos: expresion

def palindromo_func(palabra):
    return palabra == palabra[::-1]

nombre = "ANA"

#print(palindromo_func(nombre))

def cuadrado(num):

    resultado = num*num
    return resultado

def cuadrado_2(num): return num**2

# print(cuadrado(3))
# print(cuadrado_2(3))

num_2 = lambda num: num**2

#print(num_2(5))

impar = lambda x: x%2 != 0

#print(impar(18))

palindromo = lambda palabra: palabra == palabra[::-1]

#print(palindromo('RAFA'))

#REVERTIR

revertir = lambda palabra: palabra[::-1]

#print(revertir('andres'))

suma = lambda a, b: a + b

print(suma(2, 5))