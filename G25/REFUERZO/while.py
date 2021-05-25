a = 0

while a <= 10:

    print(a)
    if a == 4:
        print('esto es 4')
    if a == 9:
        break
    a += 1

else:
    print('finalizo el ciclo')