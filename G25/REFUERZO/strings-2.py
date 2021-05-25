palabra = 'PYTHON'
indices = '012345'
numeros = '0123456789'

# print(palabra[0])
# print(palabra[-6])
# print(palabra[2])
# print(palabra[-1])
# print(palabra[5])

string = '0-1-2-3-4-5-6-7-8-9'
inicio = -1
final = -18
pasos = -2

# notacion = string[inicio:final:pasos]
# print(len(string))
# print(notacion)

nombre = 'ana'

#print(nombre == nombre[::-1])

""" Los teléfonos de una empresa tienen el siguiente formato 
prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y la extensión. """

telefono = "+34-913724710-56"

print(telefono.index('9'))
print(telefono.index('0'))

numero = telefono[telefono.index('9'):telefono.index('0') + 1]
print(numero)

