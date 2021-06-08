

lista = [1, "python", True, 3.0]

datos = {'nombre': 'david', 'apellido': 'santana'}

lista = [
    {'nombre': 'david', 'apellido': 'santana'},
    {'nombre': 'camilo', 'apellido': 'montes'},
    {'nombre': 'sonia', 'apellido': 'villalba'},
    {'nombre': 'nathalie', 'apellido': 'cabrera'}
]

dicc = {
    "naturales": [1, 2, 3, 4, 5],
    "enteros": [-1, -2, 0, 1, 2],
    "decimales": [1.1, 4.5, 6.43]
}


def square():
    square = {}

    for i in range(1,21): #[1, 2, 3, 4, 5, ..., 18, 19, 20]
        # print(i)
        # input()
        if i % 2 != 0:
            square[i] = i**2
            # print(square)
            # input()
    
    return square

def square_dict_comp():

    square = {i: i**2 for i in range(1,21) if i % 2 != 0}
    square2 = {i: i*i for i in range(1,21,2)}

    return square, square2

if __name__ == '__main__':

    # for key, value in dicc.items():
    #     print(key, ":", value)

    diccionario_cuadrados_pares = square()
    print(diccionario_cuadrados_pares)
    dic1, dic2 = square_dict_comp()
    print(dic1)
    print(dic2)