


students = 'jose,david,'


def create_student(student_name):
    global students

    if student_name not in students:
        students += student_name + ','
    else:
        print('El estudiante se encuentra en la lista.')


def list_students():
    global students
    print(students)


def update_student(student_name, update_student_name):
    global students

    if student_name in students:
        students = students.replace(student_name + ',', update_student_name + ',')
    else:
        print(f"El estudiante {student_name} NO se encuentra en la lista.")


def delete_student(student_name):
    global students

    if student_name in students:
        students = students.replace(student_name + ',' , '')
    else:
        print(f"El estudiante {student_name} NO se encuentra en la lista.")
    

def menu():
    print("--APLICACION CRUD: INSCRIPCION ESTUDIANTES--")
    print("="*50)
    print("Escoja su opcion: ")
    print("[C] - Crear estudiante")
    print("[R] - Listar estudiantes")
    print("[U] - Actualizar estudiante")
    print("[D] - Borrar estudiante")


def get_student_name():
    return input('Nombre estudiante: ')


if __name__ == '__main__':
    menu()

    command = input().upper()

    if command == 'C':
        student_name = get_student_name()
        create_student(student_name)
        list_students()
    elif command == 'R':
        list_students()
    elif command == 'U':
        list_students()
        student_name = get_student_name()
        update_student_name = input('Nuevo Nombre: ')
        update_student(student_name, update_student_name)
        list_students()
    elif command == 'D':
        list_students()
        student_name = get_student_name()
        delete_student(student_name)
        list_students()
    else:
        print("COMANDO INVALIDO")
