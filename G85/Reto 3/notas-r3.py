

cuadrados = {i: i*i for i in range(1, 11)}
cuadrados = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
             6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

llaves = list(cuadrados.keys())
print(llaves)
valores = list(cuadrados.values())
print(valores)

items = list(cuadrados.items())
print(items)

a, b, c = 1, 2, 3

for k, v  in items:
    print(k, v)
