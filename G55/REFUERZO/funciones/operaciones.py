""" 
"""


def suma(a, b):
    resultado = a + b

    return resultado

def resta (a, b):
    resultado = a - b

    return resultado

def cuadrado(a):
    return a**2

def num_1_100():

    numeros = []

    for i in range(1, 101):
        i2 = cuadrado(i)
        numeros.append(i2)
    
    return numeros



if __name__ == '__main__':
    
    la_resta = resta(10, 20)
    la_suma = suma(4, 3)

    # print(la_resta)
    # print(la_suma)
    # print(cuadrado(5))

    uno_a_cien = num_1_100()
    print(uno_a_cien)


