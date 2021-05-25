palabra1 = 'Python'
palabra2 = 'Hola'
frase = palabra2 + ' ' + palabra1
#print(palabra * 3)
print(frase)

"""
Escribir un programa que pregunte el nombre completo del usuario en la consola
y después muestre por pantalla el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. 
"""
nombre = input("Escribe tu nombre: ")
#print(nombre)
minusculas = nombre.lower()
mayus = nombre.upper()
primera_letra = nombre.title()

# print(minusculas)
# print(mayus)
# print(primera_letra)

