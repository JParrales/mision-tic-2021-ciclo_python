catalogo = {}
# print(type(catalogo))

catalogo["peliculas"] = ['accion ', 'aventura', 'comedia', 'drama']

# print(catalogo)
# print(catalogo.keys())
# print(catalogo.values())
# print(catalogo.items())

generos = catalogo["peliculas"]
# print(generos)
generos_dic = dict.fromkeys(generos)
# print(generos_dic)

# print(catalogo)
# catalogo["peliculas"] = generos_dic
# print(catalogo)

# catalogo.update({'series': {}, 'documentales': {}})
# print(catalogo)

catalogo_v2 = {'peliculas': {'accion ': None,
                             'aventura': None,
                             'comedia': None,
                             'drama': None},
               'series': {},
               'documentales': {}
               }

catalogo_v2['series'] = catalogo_v2['peliculas'].copy()
#print(catalogo_v2)

catalogo_v2['documentales']['animales'] = ['las avispas', 'wild life']

#print(catalogo_v2)

catalogo_v2['documentales'].update(catalogo_v2['peliculas'].copy())


#print(catalogo_v2['documentales'])

#print(catalogo_v2)

catalogo_v2['series']['aventura'] = 'serie1', 'serie2', 'siere3'

""" for formato in catalogo_v2:
    print('Formato', formato)
    for genero, formato in catalogo_v2[formato].items():
        print(f'Genero: {genero} -> {formato}') """

print(catalogo_v2)

