#create - crear
#read - leer
#update - actualizar
#delete - borrar

nombres = ['oscar', 'david', 'carlos', 'edinson', 'felipe', 'robin']


def create(nombre):
    nombres.append(nombre)

def read():
    print(nombres)

def update(nombre_anterior, nombre_nuevo):
    idx = nombres.index(nombre_anterior )
    nombres[idx] = nombre_nuevo

def delete(nombre):
    idx = nombres.remove(nombre)


def menu():
    print("--CRUD--")
    print("="*25)
    print("Escoja su opcion: ")
    print("[C] - Crear estudiante")
    print("[R] - Listar estudiantes")
    print("[U] - Actualizar estudiante")
    print("[D] - Borrar estudiante")
    print("[E] - Salir")



if __name__ == '__main__':

    mainlopp = True

    while mainlopp:

        menu()

        opcion = input().upper()

        if opcion == 'C':
            nombre = input('Nombre: ')
            create(nombre)
        elif opcion == 'R':
            read()
        elif opcion == 'U':
            nombre = input('Nombre: ')
            nombre_nuevo = input('Nuevo nombre: ')
            update(nombre, nombre_nuevo)
        elif opcion == 'D':
            nombre = input('Nombre: ')
            delete(nombre)
        elif opcion == 'E':
            mainlopp = False
        else:
            print('OPCIOM INVALIDA')


    
    # read()
    # create('edwin')
    # create('jose')
    # create('estefania')
    # read()
    # update('oscar','john')
    # read()
    # delete('jose')
    # read()

