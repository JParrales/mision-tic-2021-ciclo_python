""" List Comprehension """

def uno_a_100():
    numeros = []

    for i in range(1, 101): #[1, 2, 3, 4, 5, ..., 25, 26, ..., 99, 100]
        numeros.append(i)
    
    return numeros

#print(uno_a_100())

numeros = [i for i in range(1, 31)]

#print(numeros)

alfabeto = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]
# print(alfabeto)
# print(alfabeto.index('d'))


def square(lista):
    cuadrado = []

    for num in lista:
        cuadrado.append(num * num)
    
    return cuadrado

#print(square(numeros))

cuadrados = [i*i for i in numeros]
#print(cuadrados)

def div_3(numeros):
    div = []

    for i in numeros:
        if i % 3 == 0:
            div.append(i)
    
    return div

#print(div_3(numeros))

divisibles_por_3 = [i for i in range(1, 31) if i % 3 == 0]

#print(divisibles_por_3)

numeros_2 = [x*x for x in range(1, 11) if x%2 == 0]
#print(numeros_2)

pares_div_5 = [x for x in range(1, 101) if x%2 == 0 and x%5 == 0]
#print(pares_div_5)

palabra = 'murcielago'

vocales_python = [vocal for vocal in palabra if vocal not in 'aeiou']
print(vocales_python)

""" [element for elemento in iterable condicion (opcional)] """