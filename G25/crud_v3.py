

#students = ['albert','heidy']

students = [
    {
        'nombre': 'albert',
        'apellido': 'plaza',
        'email': 'albert@mail.me',
        'profesion': 'ingeniero'
    },
    {
        'nombre': 'heidy',
        'apellido': 'rincon',
        'email': 'heidy@mail.me',
        'profesion': 'ingeniero'
    }
]


def create_student(student):
    global students

    if student not in students:
        students.append(student)
    else:
        print(f"El estudiante {student['name'] + '' + student['apellido']}  se encuentra en lista")


def list_students():
    print('idx\tname\tapellido\temail\tprofesion')
    print('-'*50)

    for idx, student in enumerate(students):
        print('{}\t{name}\t{apellido}\t{email}\t{profesion}'.format(
            idx,
            name = student['nombre'],
            apellido = student['apellido'],
            email = student['email'],
            profesion = student['profesion']
        ))


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


def get_student_data():
    student = {
        'nombre': input('Nombre: '),
        'apellido': input('Apellido: '),
        'email': input('email: '),
        'profesion': input('Profesion: ')
    }

    return student


if __name__ == '__main__':

    mainloop = True

    while mainloop:

        menu()
        option = input().upper()

        if option == 'C':
            student = get_student_data()
            create_student(student)
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
