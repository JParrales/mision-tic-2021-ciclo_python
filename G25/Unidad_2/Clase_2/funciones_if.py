#Anotaciones

def saludar(nombre: str) -> None:
    print("Hola " + nombre)

estudiante = "Alfredo"

#saludar(estudiante)

def sumar(num1: int, num2: int) -> int:
    return num1 + num2

#print(sumar(5, 2))

""" funciones + if"""

def positivo_nogativo(num: int) -> str:

    if num < 0:
        out = f'{num} es menor que 0'
    elif num > 0:
        out = f'{num} es mayor que 0'
    else:
        out = f'{num} es cero'
    
    return out

# numero = positivo_nogativo(0)

# print(numero)

"""
-'El ultimo digito de NUMERO es DIGITO' ----> Condiciones:
                                -si digito es mayor que 5: 'y es mayor que cinco'
                                -si el digito es 0: 'y es cero'
                                -si el digito es menor que 6: 'y es menor que 6 y no es 0'

"""

def ultimo_digito(num: int):
    strint = str(num)

    if num > 0:
        strint = strint[-1]
    else: 
        strint = '-' + strint[-1]

    if strint > '5':
        out = f'El ultimo digito de {num} es {strint} y es mayor que cinco'
    elif strint == '0':
        out = f'El ultimo digito de {num} es {strint} y es cero'
    else:
        out = f'El ultimo digito de {num} es {strint} y es menor que 6 y no es 0'

    return out

import random

numero = random.randint(-10000, 10000)

#print(ultimo_digito(numero))


"""
niño: 5 - 13
adolescente: 14 - 17
adulto joven: 18 - 35
adultos: 36 - 64
tercera edad: 65
"""
etapas = ["nino", "adolescente", "adulto joven", "adulto", "tercera edad"]
usuario = input("Ingrese su edad: ")

def etapa_edad(edad: str, etapas: list) -> str:
    edad = int(edad)
    if edad >= 5 and edad <= 13:
        idx = 0
    elif edad >= 14 and edad <= 17:
        idx = 1
    elif edad >= 18 and edad<= 35:
        idx = 2
    elif edad >= 36 and edad <= 64:
        idx = 3
    else:
        idx = -1
    
    print("Su etapa actual es: {}".format(etapas[idx]))
    
    return etapas[idx]

edad_usuario = etapa_edad(usuario, etapas)

print(edad_usuario)
