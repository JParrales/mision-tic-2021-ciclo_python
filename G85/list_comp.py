""" List comprehension """

def cuadrado():
    cuadrados = []

    for i in range(1, 21):
        cuadrados.append(i * i)
    
    return cuadrados

#print(cuadrado())

def cuadrado_list_comp():
    cuadrados = [i**2 for i in range(1,21)]
    return cuadrados

#print(cuadrado_list_comp())

def div_by_3(lista):
    div_3 = []

    for i in lista:
        if i % 3 == 0:
            div_3.append(i)
    
    return div_3

def div_by_3_list_copm(lista):
    div_3 = [i for i in lista if i % 3 == 0]

    return div_3

uno_a_cien = [i for i in range(1, 101)]
#print(uno_a_cien)
# print(div_by_3(uno_a_cien))
# print(div_by_3_list_copm(uno_a_cien))

uno_a_cien_div_by_3 = [i for i in range(1, 101) if i % 5 == 0]
print(uno_a_cien_div_by_3)

numeros_usuario = []

for i in range(1,11):
    numeros_usuario.append(int(input(f'Ingrese numero {i}: ')))

pares_usuario = [i for i in numeros_usuario if i%2 == 0]

print(numeros_usuario)
print(pares_usuario)
