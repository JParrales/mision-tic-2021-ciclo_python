""" Los teléfonos de una empresa tienen el siguiente formato 
prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y la extensión. """


"""
+1-2345812668-72
+23-2563941285-85
+358-2345812668-76
"""

telefono1 = '+1-2345812668-72'
telefono2 = '+34-913724710-56'
telefono3 = '+358-2345812668-76'

def numero_sin_formato(numero: str) -> str:

    if numero[2] == '-':
        return numero[3:-3]
    if numero[3] == '-':
        return numero[4:-3]
    if numero[4] == '-':
        return numero[5:-3]

formato1 = numero_sin_formato(telefono1)
formato2 = numero_sin_formato(telefono2)
formato3 = numero_sin_formato(telefono3)



print(telefono1, ':', formato1)
print(telefono2, ':', formato2)
print(telefono3, ':', formato3)


numero = '+34-123456789-53'


#FUNCION ANDRES.
def numero_fijo(number: str):
    index_1 = int(number.find('-'))
    #index_1 = number.index('-')
    index_2 = int(number.find('-', index_1+1))
    numero = number[index_1 + 1 : index_2]
    return numero

print(numero_fijo(numero)) 









# string = '0123456789'
# # print(string[9])
# # print(string[-1])

# inicio = 0
# final = len(string)
# pasos = 2

# print(string[inicio:final:pasos])


