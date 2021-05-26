a = -6

#print(f'a = {a}')

# if a == 0:
#     print(f'{a} es igual a  cero')
# elif a > 0:
#     print(f'{a} es mayor que cero')
# else:
#     print(f'{a} es menor que cero')

b = -4

if a > 0 and b > 0:
    print("Correcto")
elif a < 0 and b < 0:
    print("Incorrecto")
elif a < 0 and b > 0:
    print(f"Cambia el valor de a: {a}")
else:
    print(f"Camabia el valor de b: {b}")

