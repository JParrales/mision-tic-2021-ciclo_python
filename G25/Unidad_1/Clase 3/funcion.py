""" def numbre(parametro1, parametro2, ...):
    instruccion 1
    instruccion 2
    ...
    return
 """

def saludar(nombre="Usuario"):
    print(f"Hola Buen Día {nombre}")

#saludar(input("Ingresa tu nombre: "))

def primer_ultimo(lista):
    primero = lista[0]
    ultimo = lista[-1]
    print(primero, ultimo)

    return primero, ultimo

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#x, y = primer_ultimo(numeros)