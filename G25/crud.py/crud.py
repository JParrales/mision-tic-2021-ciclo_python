#Create - crear
#Read - leer
#Update - actualizar
#Delete - borrar

inventario = ['camara', 'fuente', 'filtros', 'cables', 'conectores']

def create():
    inventario.append(input('Elemento a agregar: '))

def read():
    print(inventario)

def update():
    elemento = input('Elemento a actualizar: ')
    nuevo_elemento = input('Nuevo elemento: ')
    idx = inventario.index(elemento)
    inventario[idx] = nuevo_elemento

def delete():
    inventario.remove(input('Elemento a eliminar: '))
    

def menu():
    print("--CRUD--")
    print("="*25)
    print("Escoja su opcion: ")
    print("[C] - Crear")
    print("[R] - Listar")
    print("[U] - Actualizar")
    print("[D] - Borrar")
    print("[E] - Salir.")


if __name__ == '__main__':


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