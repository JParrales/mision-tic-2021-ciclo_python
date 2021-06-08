

def square():
    squares = []

    for i in range(1, 101):
        squares.append(i * i )
    
    return squares

def square_list_compr():
    square = [i ** 2 for i in range(1,101)]
    
    return square


def div_by_3(lista):
    
    div_3 = []

    for i in lista:
        if i % 3 == 0:
            div_3.append(i)
    
    return div_3


def div_by_3_list_copm(lista):

    div_3 = [i for i in lista if i % 3 == 0]

    return div_3

""" [element for elemento in iterable condicion (opcional)] """


if __name__ == '__main__':
    
    #print(square())
    #print(div_by_3(square()))
    lista_cuadrado = square_list_compr()
    print(div_by_3_list_copm(lista_cuadrado))