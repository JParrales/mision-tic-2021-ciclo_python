
""" 
-Crear una función que tenga un diccionario donde las llaves sean los numeros del 1 al 10
- los valores de cada llave será un diccionaro de los divisores de esa llave, 
y el valor será el cuadrado de esa llave
"""

ejercicio = {
    1: {1: 1},
    2: {1: 1, 2: 4},
    3: {1: 1, 3: 9},
    4: {1: 1, 2: 4, 4: 16},
    5: {1: 1, 5: 25},
    6: {1: 1, 2: 4, 3: 9, 6: 36}
}

def divisores(num):
    
    divisores = {}

    for i in range(1, num + 1):
        
        divisores[i] = {}

        for x in range(1, i + 1):
            if i % x == 0:
                divisores[i].update({x: x**2})
    return divisores


if __name__ == '__main__':
    rango = int(input("Ingrese el rango: "))
    print(divisores(rango))

    multiplos = {i:{x: x*x for x in range(1, i + 1) if i % x == 0} for i in range(1, 11)}

    multiplos2 = {i:{x: x*x for x in range(1, i + 1) if i % x == 0}  for i in range(1,11)}

    print(multiplos)

