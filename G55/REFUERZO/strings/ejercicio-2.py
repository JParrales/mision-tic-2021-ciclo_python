""" Los teléfonos de una empresa tienen el siguiente formato 
prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y la extensión. """

numero = '+34-913724710-56'
# string = '0123456789'
# inicio = 0
# final = -1
# pasos = 4
# string[inicio:final:pasos]
# print(string)
# print(string[inicio::pasos])

print(numero[4:-3])
