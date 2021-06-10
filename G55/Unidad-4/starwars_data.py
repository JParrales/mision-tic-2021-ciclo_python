DATA = [
    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "age": 19,
        "gender": "male",
    },
    {
        "name": "C-3PO",
        "height": "167",
        "mass": "75",
        "hair_color": "n/a",
        "skin_color": "gold",
        "eye_color": "yellow",
        "age": 112,
        "gender": "n/a",
    },
    {
        "name": "R2-D2",
        "height": "96",
        "mass": "32",
        "hair_color": "n/a",
        "skin_color": "white, blue",
        "eye_color": "red",
        "age": 33,
        "gender": "n/a",
    },
    {
        "name": "Darth Vader",
        "height": "202",
        "mass": "136",
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow",
        "age": 41,
        "gender": "male",
    },
    {
        "name": "Han Solo",
        "height": "180",
        "mass": "80",
        "hair_color": "brown",
        "skin_color": "fair",
        "eye_color": "brown",
        "age": 29,
        "gender": "male"
    },
    {
        "name": "Chewbacca",
        "height": "228",
        "mass": "112",
        "hair_color": "brown",
        "skin_color": "unknown",
        "eye_color": "blue",
        "age": 200,
        "gender": "male",
    },
    {
        "name": "Leia Organa",
        "height": "150",
        "mass": "49",
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "age": 19,
        "gender": "female",
    },
    {
        "name": "Obi-Wan Kenobi",
        "height": "182",
        "mass": "77",
        "hair_color": "auburn, white",
        "skin_color": "fair",
        "eye_color": "blue-gray",
        "age": 57,
        "gender": "male",
    }
]


if __name__ == '__main__':

    # print(DATA[0])
    # print(DATA[-1])
    # print(DATA[-1]['name'])

    personajes = [personaje["name"] for personaje in DATA]
    personajes_m = [personaje['name']
                    for personaje in DATA if personaje["gender"] == 'male']

    # print(personajes)
    # print(personajes_m)

    personajes_jovenes = list(
        filter(lambda personaje: personaje["age"] <= 42, DATA))
    personajes_jovenes_nombres = list(
        map(lambda personaje: personaje["name"], personajes_jovenes))
    personajes_jovenes_años = list(
        map(lambda personaje: personaje["age"], personajes_jovenes))
    datos_jovenes = tuple(zip(personajes_jovenes_nombres, personajes_jovenes_años))


    print(datos_jovenes)

    # for nombre, edad in zip(personajes_jovenes_nombres, personajes_jovenes_años):
    #     print("{}: tiene {} años.".format(nombre, edad))
    
