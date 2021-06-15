

def read():
    numeros = []
    file = open('./archivos/numeros.txt')

    for line in file:
        numeros.append(int(line))
    print(numeros)


def write():
    lenguajes = ["React", "Ruby", "HTML", "CSS", "JavaScript"]
    file = open("./archivos/lenguajes.txt", "a", encoding="utf-8")
    for lenguaje in lenguajes:
        file.write(lenguaje)
        file.write("\n")



if __name__ == '__main__':
    write()