from starwars_data import DATA



if __name__ == '__main__':

    # print(DATA[0])
    # print(DATA[2])
    # print(DATA[2]['name'])

    """ Lista de personajes """

    personajes = [personaje["name"] for personaje in DATA]
    robots = [robot["name"] for robot in DATA if robot["gender"] == "n/a"]
       
    # print(personajes)
    # print(robots)

    personajes_jovenes = list(filter(lambda personaje: personaje["age"] < 30, DATA))
    #print(personajes_jovenes)
    personajes_jovenes_nombre = list(map(lambda personaje: personaje["name"], personajes_jovenes))

    edad_jovenes = list(map(lambda personaje: personaje["age"], personajes_jovenes))
    #print(edad_jovenes)

    
    #Carlos Andres
    personajes_jovenes=[ro["age"] for ro in DATA if ro["age"]<30]
    #print(personajes_jovenes)

    datos_jovenes = dict(zip(personajes_jovenes_nombre, edad_jovenes))
    #print(datos_jovenes)

    for nombre, edad in datos_jovenes.items():
        print("{} tiene {} años.".format(nombre, edad))

    



    

