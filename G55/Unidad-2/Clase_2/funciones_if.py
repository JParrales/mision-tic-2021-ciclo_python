#Anotaciones

def saludar(nombre: str) -> None:
    print("Hola " + nombre)

#estudiante = saludar("Alex")

def sumar(num1: int, num2: int) -> int:
    return num1 + num2

#print(sumar(5, 2))

#print(sumar("Hola ", "Mundo"))

""" Funciones + if """

def positivo_negativo(num: int) -> str:

    if num > 0:
        x = f'{num} es mayor que 0'
    elif num == 0:
        x = f'{num} es cero.'
    else:
        x = f'{num} es menor que 0'

    return x

# numero = positivo_negativo(0)

# print(numero)

"""
-'El ultimo digito de NUMERO es DIGITO'--->CONDICIONES:
            -si el digito es mayor que 5: 'y es mayor que cinco'
            -si el digito es 0: 'y es cero'
            -si el digito es menor que 6: 'y es menor que 6 y no es 0." 

"""

def ultimo_digito(num: int):
    if num >= 0:
        numero = str(num)[-1]
    else:
        numero = '-' + str(num)[-1]
    
    if numero > '5':
        out = f'El ultimo digito de {num} es {numero} y es mayor que cinco'
    elif numero == '0':
        out = f'El ultimo digito de {num} es {numero} y es cero'
    else:
        out = f'El ultimo digito de {num} es {numero} y es menor que 6 y no es 0.'
    
    return out


import random

#numero = random.randint(-1000, 1000)

#print(ultimo_digito(numero))


"""
bebe = 0 - 4
niños = 5 - 13
adolescentes = 14 -17
adulto joven = 18 - 35
adultos = 36 - 64
tercera edad = 65 - ....

"""
rangos = ["bebe", "niños", "adolescentes", "adulto joven", "adulto", "tercera edad"]
edad_usuario = int(input("Ingrese su edad: "))

def etapa_edad(edad: str, etapas: list) -> str:
    
    if edad <= 4:
        idx = 0
    elif edad <= 13:
        idx = 1
    elif edad <= 17:
        idx = 2
    elif edad <= 35:
        idx = 3
    elif edad <= 65:
       idx = 4
    else:
        idx = 5

    print(etapas[idx])
    
    return edad, etapas[idx]

edad_estudiante, etapa=etapa_edad(edad_usuario, rangos)

print(edad_estudiante, etapa)
