


students = 'jose,david,'

def create_student(student_name):
    global students
    
    if student_name not in students:
        students += student_name + ','

def list_students():
    global students
    print(students)


def print_menu():
    print("--APLICACION CRUD: INSCRIPCION ESTUDIANTES--")
    print("="*50)
    print("Escoja su opcion: ")
    print("[C] - Crear estudiante")
    print("[R] - Listar estudiantes")
    


if __name__ == '__main__':
    print_menu()

    command = input()
    command = command.upper()

    if command == 'C':
        student_name = input('Nombre estudiante: ')
        create_student(student_name)
        list_students()
