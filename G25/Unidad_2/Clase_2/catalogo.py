catalogo = {}

# print(catalogo)

catalogo["peliculas"] = ["Comedia", "Terror", "Accion", "Drama", "Misterio"]

# print(catalogo)

# print(catalogo.items())
# print(catalogo.keys())
# print(catalogo.values())

tipos = catalogo["peliculas"]

# print(tipos)

tipos_dic = dict.fromkeys(tipos)
# print(tipos_dic)

catalogo["peliculas"] = tipos_dic

# print(catalogo)

catalogo.update({'series': {}, 'documentales': {}})
#print(catalogo)

catalogo_v2 = {'peliculas': {'Comedia': None,
                             'Terror': None, 
                             'Accion': None,
                             'Drama': None,
                             'Misterio': None
                             },
               'series': {},
               'documentales': {}
               }

catalogo_v2['series']['Comedia'] = ['family guy', 'the office', 'broklin 99']

catalogo_v2['documentales']['animales'] = ['las avispas', 'elefantes en asia', 'wild life']
catalogo_v2['documentales']['ciencia'] = ['merie curie', 'cosmos', 'blue planet']
""" 
print(catalogo_v2)
print(f'--------------')


for formato in catalogo_v2:
    print('Formato', formato)
    for categoria, formato in catalogo_v2[formato].items():
        print(f'Categoría: {categoria} > {formato}')
 """

print(catalogo_v2['series']['Comedia'][2])