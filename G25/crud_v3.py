

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


def update_student(student_idx, update_student_data):
    global students

    if len(students) -1 >= student_idx:
        students[student_idx] = update_student_data
    else:
        print(f"El estudiante NO se encuentra en lista")


def delete_student(student_idx):
    global students

    if len(students) - 1 >= student_idx:
        print('Los datos eliminados son: ')
        print(students.pop(student_idx))
    else:
        print(f"Indice fuera de lista")


def search_student(student_idx):

    if len(students) -1 >= student_idx:
        return students[student_idx]
    else:
        return f"INDICE {student_idx} FUERA DE RANGO"


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
            student_idx = int(input('Seleccione indice: '))
            update_student_data= get_student_data()
            update_student(student_idx, update_student_data)
            list_students()
            input()
        elif option == 'D':
            list_students()
            student_idx = int(input('Seleccione indice: '))
            delete_student(student_idx)
            list_students()
            input()
        elif option == 'E':
            mainloop = False
        elif option == 'S':
            student_idx = int(input('Seleccione indice: '))
            student = search_student(student_idx)
            print(f"Estos son los datos del estidiante:")
            print(student)

        else:
            print('OPCION INVALIDA')
            input()
