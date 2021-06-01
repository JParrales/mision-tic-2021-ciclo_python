def square():

    numeros = {}

    for i in range(1, 21):

        if i % 2 != 0:
            numeros[i] = i**2
    
    return numeros

#print(square())

def numbers(num1, num2):
    numeros = {}

    for i in range(num1, num2 + 1):
        numeros[i] = i**2
    
    return numeros

num_1_to_50 = numbers(1, 50)
#print(num_1_to_50)

def num_div_5(numeros):
    div_5 = {}

    for key in numeros.keys():
        if key % 5 == 0:
            div_5[key] = key**2
    
    return div_5


print(num_div_5(num_1_to_50))

