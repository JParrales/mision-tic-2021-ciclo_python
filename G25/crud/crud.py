#Create - crear
#Read - leer
#Update - actualizar
#Delete - borrar



def create():
    inventario.append(input('Elemento a agregar: '))
    write()

def read():
    print(inventario)

def update():
    elemento = input('Elemento a actualizar: ')
    nuevo_elemento = input('Nuevo elemento: ')
    idx = inventario.index(elemento)
    inventario[idx] = nuevo_elemento
    write()

def delete():
    inventario.remove(input('Elemento a eliminar: '))
    write()
    

def menu():
    print("--CRUD--")
    print("="*25)
    print("Escoja su opcion: ")
    print("[C] - Crear")
    print("[R] - Listar")
    print("[U] - Actualizar")
    print("[D] - Borrar")
    print("[E] - Salir.")

def write():
    file = open('inventario.txt', 'w', encoding='utf-8')
    for objeto in inventario:
        file.write(objeto)
        file.write('\n')

def data_inventario():
    datos = []
    file = open('inventario.txt', 'r', encoding='utf-8')
    for objeto in file:
        datos.append(objeto[:-1])
    
    return datos


if __name__ == '__main__':

    inventario = data_inventario()
    mainloop = True

    while mainloop:
        
        menu()


        opcion = input().upper()

        if opcion == 'C':
            create()
        elif opcion == 'R':
            read()
        elif opcion == 'U':
            update()
        elif opcion == 'D':
            delete()
        elif opcion == 'E':
            mainloop = False
        else:
            print('Opción inválida')

#['camara', 'fuente', 'filtros', 'cables', 'conectores', 'dvr', 'monitores']