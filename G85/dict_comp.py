
def square():
    numeros = {}

    for i in range(1, 21):
        if i % 2 == 0:
            numeros[i] = i*i
    
    return numeros

cuadrado = {i:i**2 for i in range(1, 21) if i % 2 == 0}
# print(square())
# print(cuadrado)

""" 
-Crear un diccionario donde las llaves sean los numeros del 1 al 10
- los valores de cada llave será un diccionaro de los divisores de esa llave, 
y el valor será el cuadrado de esa llave
"""

ejercicio = {
    1: {1: 1},
    2: {1: 1, 2: 4},
    3: {1: 1, 3: 9},
    4: {1: 1, 2: 4, 4: 16}
}

divisores = {}

for i in range(1, 11):

    divisores[i] = {}
    
    for x in range(1, i + 1):
        if i % x == 0:
            divisores[i].update({x: x**2})

print(divisores)

multiplos = {i:{x: x**2 for x in range(1, i + 1) if i % x == 0} for i in range(1, 11)}

#multiplos_2 = {i:{x:x**2 for x in range(1, i + 1) if i % x == 0} for i in range(1, 11)}

print(multiplos)
