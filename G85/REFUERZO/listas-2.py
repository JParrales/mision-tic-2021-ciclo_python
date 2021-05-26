""" 
Escribir un programa que almacene en una lista 
los números del 1 al 10 
y los muestre por pantalla en 
orden inverso separados por comas.
"""

numeros = list(range(1, 11))
# print(numeros)
# print(numeros[::-1])

desorden = [6, 7, 4, 15, 10, 12, 2, 3, 5, 8]
# print(desorden)
# print(desorden[::-1])
# print(desorden)
#print(desorden.sort(reverse=True))
# # print(desorden)
#print(desorden.reverse())
# print(desorden)

palindromo = 'AnitaLavaLaTina'

print(palindromo.lower() == palindromo[::-1].lower())