# for "variable" in "elemento iterable"

# for numeros in range(1, 11):
#     print(numeros)

# for i in range(65, 91):
#     print(f"{i:c}", end=' ')

# print(ord('A'))
# print(chr(90))

# abcdario = []

# for x in range(65, 91):
#     abcdario.append(chr(x))
# #     print(abcdario)

# consonantes = []
# vocales = ['A', 'E', 'I', 'O', 'U']

# for letra in abcdario:

#     if letra in vocales:
#         continue
#     else:
#         consonantes.append(letra)
#         print(consonantes)


# nombres = ['Carlos', 'Daniel', 'Italo', 'Mauricio', 'Jose']
# profesiones = ['Profe', 'Electronico', 'Cheff', 'Adminsitrador', 'Profe']

# trabajos = {} # {profesion:persona}

# for i in range(len(nombres)):

#     profesion = profesiones[i]
#     print(profesion)
#     input()
#     persona = nombres[i]
#     print(persona)
#     input()
#     if profesion not in trabajos:
#         trabajos[profesion] = [persona]
#     else:
#         trabajos[profesion].append(persona)
    
#     print(trabajos)
#     input()

# print(trabajos)

""" 
Escribir un programa que muestre en pantalla los números del 1 al 100, 
sustituyendo los múltiplos de 
3 por la palabra “fizz”, 
los múltiplos de 5 por “buzz” 
y los múltiplos de ambos, es decir, 
los múltiplos de 3 y 5 (o de 15), por la palabra “fizzbuzz”.
"""

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz", end=' ')
        elif i % 5 == 0:
            print("buzz", end= ' ')
        elif i % 3 == 0:
            print("fizz", end=' ')
        else:
            print(i, end=' ')
    
    print()


fizzbuzz()