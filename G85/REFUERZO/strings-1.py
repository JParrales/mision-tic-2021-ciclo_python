palabra = 'Python'
indices = '012345'

#print(palabra[2])
"""
Escribir un programa que pregunte el nombre completo del usuario en la consola
y después muestre por pantalla el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. 
"""
nombre = input('Ingrese su nombre: ')

def nombre_por_3(nombre_completo):
    minusculas = nombre_completo.lower()
    mayusculas = nombre_completo.upper()
    primera_letra = nombre_completo.title()

    print(minusculas)
    print(mayusculas)
    print(primera_letra)


nombre_por_3(nombre)
   # nombre_completo = nombre
print()
#nombre_por_3('MIguel ferNANDO gonzalez')
    #nombre_completo = 'MIguel ferNANDO gonzalez'


