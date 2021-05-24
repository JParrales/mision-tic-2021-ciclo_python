

students = [
    {
        'nombre': 'mauricio',
        'apellido': 'mancilla',
        'email': 'mauricio@mail.me',
        'profesion': 'administrador'
    },
    {
        'nombre': 'yisney',
        'apellido': 'soto',
        'email': 'yisney@mail.me',
        'profesion': 'docente' 
    }
]


def create_student(student):
    global students

    if student not in students:
        students.append(student)
    else:
        print(f'El estudiante {student["nombre"] + " " + student["apellido"]} se encuentra en lista')


def list_students():
    global students
    print('{uid}\t{nombre}\t{apellido}\t{email}\t{profesion}')
    
    for idx, student in enumerate(students):
        print('{uid}\t{nombre}\t{apellido}\t{email}\t{profesion}'.format(
            uid = idx,
            nombre = student['nombre'],
            apellido = student['apellido'],
            email = student['email'],
            profesion = student['profesion']
        ))


def delete_student(student_name):
    global students

    if student_name in students:
        students.remove(student_name)
    else:
        print(f'El estudiante {student_name} NO se encuentra en lista')


def update_student(student_idx, update_student_data):
    global students

    if len(students) - 1 <= student_idx:
        students[student_idx] = update_student_data
    else:
        print(f'El id NO se encuentra en lista')


def search_student(student_name):
    global students

    if student_name in students:
        print(f"El estudiante {student_name} se encuentra en lista")
    else:
        print(f"El estudiante {student_name} No se encuentra en lista")


def print_menu():
    print("--APLICACION CRUD: INSCRIPCION ESTUDIANTES--")
    print("="*50)
    print("Escoja su opcion: ")
    print("[C] - Crear estudiante")
    print("[R] - Listar estudiantes")
    print("[U] - Actualizar estudiante")
    print("[D] - Borrar estudiante")
    print("[S] - Buscar estudiante")
    print("[E] - Salir.")


def get_student_name():

    student_name = None

    while not student_name:
        student_name = input('Nombre estudiante: ')

    return student_name


def get_student_data():
    student ={
        'nombre': input('Nombre: '),
        'apellido': input('Apellido: '),
        'email': input('email: '),
        'profesion': input('profesion: ')
    }

    return student

if __name__ == '__main__':


    mainlopp = True

    while mainlopp:
        print_menu()

        command = input()
        command = command.upper()

        if command == 'C':
            student = get_student_data()
            create_student(student)
            list_students()
        elif command == 'R':
            list_students()
        elif command == 'U':
            list_students()
            student_idx = int(input('Seleccione usuario: '))
            update_student_data = get_student_data()
            update_student(student_idx, update_student_data)
            list_students()
        elif command == 'D':
            list_students()
            student_name = get_student_name()
            delete_student(student_name)
            list_students()
        elif command == 'S':
            student_name = get_student_name()
            search_student(student_name)
        elif command == 'E':
            mainlopp = False
        else:
            print("OPCION INVALIDA")
