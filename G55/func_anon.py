""" Operadores encadenados """

menor = 1 < 2 and 2 < 3
menor_2 = 1 < 2 < 3
mayor = 3 > 2 > 1

# print(menor)
# print(menor_2)
# print(mayor)

""" Comprobar si un numero se encuentra entre 0 y 100 """

numero = 200

# if numero >= 0 and numero <= 100:
#     print(f"El {numero} se enecuentra entre 0 y 100")
# else:
#     print(f"El {numero} NO se enecuentra entre 0 y 100")

# if 0 <= numero <= 100:
#     print(f"El {numero} se enecuentra entre 0 y 100")
# else:
#     print(f"El {numero} NO se enecuentra entre 0 y 100") 


""" lambda """

def cuadrado(numero):
    resultado = numero * numero

    return resultado

def cuadrado_v2(numero):
    return numero ** 2

def cuadrado_v3(numero): return numero**2

num1 = cuadrado(3)
num2 = cuadrado_v2(3)
num3 = cuadrado_v3(3)

# print(num1)
# print(num2)
# print(num3)

numero_cuadrado = lambda num: num**2

# print(numero_cuadrado)
# print(numero_cuadrado(5))

def palindromo_func(palabra):
    return palabra == palabra[::-1]

nombre = 'ana'

#print(palindromo_func(nombre))

palindromo = lambda palabra: palabra == palabra[::1]

#print(palindromo(nombre))

#Impar

impar = lambda num: num%2 != 0

#print(impar(5))

#revertir

revertir = lambda palabra: palabra[::-1]

print(revertir('Python'))

suma = lambda x, y: x + y

print(suma(2, 5))

#lambda argumentos: expresion

