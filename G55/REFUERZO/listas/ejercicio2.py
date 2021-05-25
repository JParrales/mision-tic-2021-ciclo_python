""" 
Escribir un programa que almacene en una lista 
los números del 1 al 10 
y los muestre por pantalla en 
orden inverso separados por comas.
 """
# list()
# tuple()
# dict()

# numeros = list(range(1,11))
# print(numeros)
# print(numeros[::-1])

import random

# desorden = [3, 1, 7, 8, 6, 5, 12, 10, 9]
# print(desorden)
# desorden.sort()
# print(desorden)
# desorden.sort(reverse=True)
# print(desorden)

#print(dir(tuple())) #ver los metodos del tipo de dato

# desorden = [3, 1, 7, 8, 6, 5, 12, 10, 9]
# desorden.reverse()
# print(desorden)

palindromo = 'AnitaLavaLaTina'
# lista = []
# lista[:0] = palindromo
lista = list(palindromo)
print(lista)
al_reves = lista.copy()
al_reves.reverse()
print(al_reves)

string = str(al_reves)
print(string)
