# for "variable" in "elemento iterable":
#     pass

# for numeros in range(1, 11):
#     print(numeros, end=' ')
# print()

# x= ["manzanas", "peras", "banas", "melones", "fresas"]

# for i in x:
#     print(i)

# for pares in range(2, 101, 2):
#     print(pares, end=' ')
# print()

# for i in range(65, 91):
#     print(f"{i:c}", end=' ')
# print()

#print(ord('a'))
#print(chr(90))

abcdario = []

for letra in range(ord('a'), ord('z') + 1):
    abcdario.append(chr(letra))
    #print(abcdario)

volcales = []
consonantes = []

# for letra in abcdario:

#     if letra in 'aeiou':
#         volcales.append(letra)
#     else:
#         consonantes.append(letra)

# print(volcales)
# print(consonantes)

nombres  = ['alex', 'edwin', 'heynar', 'Galxy', 'juan', 'jose']
profesiones = ['soporte', 'administrador', 'tecnologo', 'electricista', 'ingeniero', 'ingeniero']

# print(nombres)
# print(profesiones)

trabajos = {} #{profesion: persona}

for i in range(len(nombres)):

    profesion = profesiones[i]
    print(profesion)
    input()
    persona = nombres[i]
    print(persona)
    input()

    if profesion not in trabajos:
        trabajos[profesion] = [persona]
    else:
        trabajos[profesion].append(persona)

    print(trabajos)
    input()