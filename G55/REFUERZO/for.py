# for variable in objeto_iterable:

# string = "Python"
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tupla = tuple(range(10, 20))
# diccionario = {
#     (1, 2): 'P',
#     (2, 3): 'Y',
#     'letra 3': 'T',
#     'letra 4': 'H',
#     'letra 5': 'O',
#     'letra 6': 'N'
# }

# # for llave, valor in diccionario.items():
# #     print(llave, valor)
# a = 0
# for i in lista:
#     a += i
#     print(a, i)

#numeros = [72, 73, 74, 75, 76, 77, 78, 79, 90, 91]

# for i in numeros:
#     if i % 2 != 0:
#         print(i, end=' ')
#     else:
#         continue
#print()

# string_numeros = '0-1-2-3-4-5-6-7-8-9'

# for i in string_numeros:
    
#     if i in '0123456789':
#         if int(i) % 2 == 0:
#             print(i)

frase = 'Anita Lava La Tina'
frase_reves = frase[::-1]

#print(frase, frase_reves, sep='\n')
palindromo = ''
frase = frase.lower()
for i in frase:
    
    if i == ' ':
        continue
    palindromo += i

print(palindromo)
print(palindromo[::-1])
es_palindromo = palindromo == palindromo[::-1]
es_palindromo = "Es palindromo" if es_palindromo == True else "No es palindromo"
print(es_palindromo)

