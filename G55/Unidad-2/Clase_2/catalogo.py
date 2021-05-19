# catalogo = {}
# # print(catalogo)
# lista_generos = ['accion', 'comedia', 'suspenso', 'drama', 'ficcion']
# # print(lista_generos)
# # print(catalogo)
# catalogo['peliculas'] = lista_generos
# # print(catalogo)
# # print(catalogo['peliculas'])

# # print(catalogo)
# # print(catalogo.keys())
# # print(catalogo.values())
# # print(catalogo.items())

# generos = catalogo['peliculas']  # terror
# # print(generos)
# catalogo['peliculas'] = dict.fromkeys(generos)
# # print(catalogo['peliculas'])
# # print(catalogo)

# catalogo.update({'series': {}, 'documentales': {}})
# print(catalogo)

# catalogo['peliculas'].update({'terror': 'SAW'})
# print(catalogo)

catalogo_v2 = {'peliculas': {'accion': None,
                             'comedia': None,
                             'suspenso': None,
                             'drama': None,
                             'ficcion': None,
                             'terror': 'SAW'},
               'series': {},
               'documentales': {}}



catalogo_v2['series'] = catalogo_v2['peliculas'].copy()
# print(catalogo_v2['peliculas'])
# print(catalogo_v2['series'])
# print(id(catalogo_v2['peliculas']), id(catalogo_v2['series']))
#catalogo_v2['series']['accion'] = 'Duro de matar'
# print(catalogo_v2['peliculas'])
# print(catalogo_v2['series'])
catalogo_v2['series'].pop('terror')
#print(catalogo_v2['series'])
#print(catalogo_v2)

catalogo_v2['documentales']['animales'] = ['las avispas', 'wild life']
#print(catalogo_v2)

catalogo_v2['documentales'].update(catalogo_v2['series'].copy())
print(catalogo_v2)

catalogo_v2['series']['comedia'] = ['rick and morty', 'brooklin 99']
catalogo_v2['series']['comedia'].append('el tarro')

for formato in catalogo_v2:
    print('Formato', formato)
    for genero, formato in catalogo_v2[formato].items():
        print(f'Genero: {genero} > {formato}')

