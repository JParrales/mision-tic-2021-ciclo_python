


students = ['albert','heidy']


def create_student(student_name):
    global students

    if student_name not in students:
        students.append(student_name)
    else:
        print(f"El estudiante {student_name} se encuentra en lista")


def list_students():
    for idx, student in enumerate(students):
        print(f'{idx}: {student}')


def update_student(student_name, update_student_name):
    global students

    if student_name in students:
        idx = students.index(student_name)
        students[idx] = update_student_name
    else:
        print(f"El estudiante {student_name} NO se encuentra en lista")


def delete_student(student_name):
    global students

    if student_name in students:
        students.remove(student_name)
    else: 
        print(f"El estudiante {student_name} NO se encuentra en lista")


def search_student(student_name):
    #students_list = students.split(',')
    global students

    for student in students:

        if student != student_name:
            continue
        else:
            return True


def menu():
    print("-- Aplicación CRUD: INSCRIPCION ESTUDIANTES ---")
    print("="*50)
    print("Seleccione una opción:")
    print("[C] - Crear estudiante.")
    print("[R] - Listar estudiantes.")
    print("[U] - Actualizar estudiante.")
    print("[D] - Borrar estudiate.")
    print("[S] - Buscar estudiante.")
    print("[E] - Salir.")


def get_student_name():
    student_name = None

    while not student_name:
        student_name = input('Nombre estudiante: ')
    
    return student_name


if __name__ == '__main__':

    mainloop = True

    while mainloop:

        menu()
        option = input().upper()

        if option == 'C':
            student_name = get_student_name()
            create_student(student_name)
            list_students()
            input()
        elif option == 'R':
            list_students()
            input()
        elif option == 'U':
            list_students()
            student_name = get_student_name()
            update_student_name = input('Nuevo Nombre: ')
            update_student(student_name, update_student_name)
            list_students()
            input()
        elif option == 'D':
            list_students()
            student_name = get_student_name()
            delete_student(student_name)
            list_students()
            input()
        elif option == 'E':
            mainloop = False
        elif option == 'S':
            student_name = get_student_name()
            student = search_student(student_name)
            if student:
                print(f"El estudiante {student_name} SE encuentra en lista")
            else:
                print(f"El estudiante {student_name} NO se encuentra en lista")
            input()
        else:
            print('OPCION INVALIDA')
            input()
