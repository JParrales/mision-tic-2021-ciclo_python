


students = 'albert,heidy,'


def create_student(student_name):
    global students

    if student_name not in students:
        students += student_name + ','
    else:
        print(f"El estudiante {student_name} se encuentra en lista")


def list_students():
    print(students)


def update_student(student_name, update_student_name):
    global students
    
    if student_name in students:
        students = students.replace(student_name, update_student_name)
    else:
        print(f"El estudiante {student_name} NO se encuentra en lista")


def delete_student(student_name):
    global students

    if student_name in students:
        students = students.replace(student_name + ',', '')
    else: 
        print(f"El estudiante {student_name} NO se encuentra en lista")


def menu():
    print("-- Aplicación CRUD: INSCRIPCION ESTUDIANTES ---")
    print("="*50)
    print("Seleccione una opción:")
    print("[C] - Crear estudiante.")
    print("[R] - Listar estudiantes.")
    print("[U] - Actualizar estudiante.")
    print("[D] - Borrar estudiate.")
    print("[E] - Salir.")


def get_student_name():
    return input('Nombre estudiante: ')


if __name__ == '__main__':

    mainloop = True

    while mainloop:

        menu()
        option = input().upper()

        if option == 'C':
            student_name = get_student_name()
            create_student(student_name)
            list_students()
        elif option == 'R':
            list_students()
        elif option == 'U':
            list_students()
            student_name = get_student_name()
            update_student_name = input('Nuevo Nombre: ')
            update_student(student_name, update_student_name)
            list_students()
        elif option == 'D':
            list_students()
            student_name = get_student_name()
            delete_student(student_name)
            list_students()
        elif option == 'E':
            mainloop = False
        else:
            print('OPCION INVALIDA')
