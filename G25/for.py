#for "variable" in "elemento iterable"

# for i in range(1, 20, 2):
#     print(i)


# for i in range(97, 123):
#     print(f"{i:c}", end=' ')
# print()

# print(ord('a'))
# print(chr(122))

import abc


abcdario = []

for x in range(97, 123): #[97, 98, 99, ..., 122]
    abcdario.append(chr(x))
    #print(abcdario)

vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = []

# for letra in abcdario:
    
#     if letra in vocales:
#         continue
#     else:
#         consonantes += letra

# print(consonantes)


# for i in range(1, 11):

#     if i == 2 or i == 4:
#         continue
#     print(i)

nombres = ['Albert', 'Cindy', 'Diego', 'Laura', 'Nayhalie', 'Cristian', 'Jose']
profesiones = ['Ingeniero', 'Empleado', 'Ingeniero', 'Ingeniero', 'Ingeniero', 'Empleado', 'Profe']

trabajos = {}

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

print(trabajos)    

