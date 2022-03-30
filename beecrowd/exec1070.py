x = int(input())

contador = 0
for i in range(x, 200):
    if i % 2 != 0 and contador < 6:
        print(i)
        contador += 1
