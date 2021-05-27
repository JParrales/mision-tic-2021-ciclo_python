"""escribir una función que nos diga si la frase es un palindromo"""


#print(palindromo.lower() == palindromo[::-1].lower())

#continue

lista = [34, 35, 36, 37, 38, 39, 40, 41, 42, 43]

# for i in lista:
#     if i % 2 != 0:
#         continue
#     print(i, end=' ')
# print()


palindromo = 'escribir codigo '

def es_palindromo(frase):
    frase = frase.lower()
    # print(frase)
    # input()
    frase_sin_espacios = ''

    for i in frase:

        if i == ' ':
            continue
        frase_sin_espacios += i
    
    nuevo_palindromo = frase_sin_espacios[::-1]
    phrase = frase_sin_espacios == nuevo_palindromo


    return phrase

print(es_palindromo(palindromo))




        
