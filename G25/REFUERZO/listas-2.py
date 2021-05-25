""" 
Escribir un programa que almacene en una lista 
los números del 1 al 10 
y los muestre por pantalla en 
orden inverso separados por comas.
"""

numeros = list(range(1,11))
# print(numeros)
# print(numeros[::-1])

desorden = [7, 3, 6, 15, 8, 9, 1, 2, 10]
#print(desorden)
orden = desorden.copy()
orden.sort(reverse=True)
print(desorden)
print(orden)
desorden.reverse()
print(desorden)
