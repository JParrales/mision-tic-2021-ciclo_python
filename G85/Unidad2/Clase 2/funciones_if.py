# Anotaciones

def saludar(nombre: str) -> None:
    print("Hola", nombre)

# estudiante = saludar("Daniel")
# print(type(estudiante), estudiante)


def sumar(num1: int, num2: int) -> int:
    """ suma num1 con num" """
    return num1 + num2

# print(sumar("jose"," parrales"))


def positivo_negativo(num: int) -> str:

    if num > 0:
        x = f'{num} es mayor que cero y es positivo'
    if num < 0:
        x = f'{num} es menor que cero y es negatico'
    if num == 0:
        x = f'el numeor es 0.'

    # print(x)

    return x, num


# cadena, numero = positivo_negativo(10)

# print(cadena)
# print(numero)

"""
bebe = 0 - 4
niños = 5 - 13
adolescentes = 14 -17
adulto joven = 18 - 35
adultos = 36 - 64
tercera edad = 65 - ....

"""
""" rangos = ["bebe", "niños", "adolescentes", "adulto joven", "adulto", "tercera edad"]
edad_usuario = int(input("Ingrese su edad: "))

def etapa_edad(edad: str, etapas: list) -> str:
    #
    #
    return

 """

rangos = ["bebe", "niños", "adolecentes","adulto joven", "adulto", "tercera edad"]
edad_usuario = int(input("Ingrese su edad en años: "))

# def etapa_edad(edad: int, etapas: list) -> str:
#     edad_estudiante = edad 
#     if 0 <= edad_estudiante <= 4: 
#         etapas = etapas[0] 
#     elif edad_estudiante  <= 5: 
#         etapas = etapas[1] 
#     elif edad_estudiante >= 14:
#         etapas = etapas[2] 
#     elif edad_estudiante >= 18: 
#         etapas = etapas[3] 
#     elif edad_estudiante >= 36: 
#         etapas = etapas[4] 
#     elif edad_estudiante >= 65: 
#         etapas = etapas[5]
#     else:
#         return f"la edad ingresada no esta en el rango de etapas", None
    
#     return edad_estudiante, etapas
    

# edad_estudiante, etapa = etapa_edad(edad_usuario, rangos)
    
# print("El estudiante de {} años esta en la etapa de {}".format(edad_estudiante, etapa))




rangos = ["bebe", "niños", "adolescentes", "adulto joven", "adulto", "tercera edad","difunto"]
edad_usuario = int(input("Ingrese su edad: "))

# def etapa_edad(edad: str, etapas: list,) -> str:
# #
# #
#     return

# while True:
#     try: 
#     edad_usuario = int(input("\nIngrese su edad: "))
#     break
#     except ValueError:
#     print("\ndigita un número no letras por favor")


# while edad_usuario < 0:
#     print("\ndigita un número entero positivo por favor") 

#     edad_usuario = int(input("\nIngrese su edad: "))



#     if edad_usuario <5:
#         x=0

#     elif edad_usuario >4 and edad_usuario <14:
#         x=1

#     elif edad_usuario >13 and edad_usuario <18:
#         x=2

#     elif edad_usuario >17 and edad_usuario <36:
#         x=3

#     elif edad_usuario >35 and edad_usuario <65:
#         x=4

#     elif edad_usuario >64 and edad_usuario <115:
#         x=5
#     else:
#         x=6

# edad=edad_usuario
# etapas=rangos[x] 

# print(f"\nTienes :",edad," años y perteneces al rago de :",etapas) 
