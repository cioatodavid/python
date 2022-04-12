x, y = map(int, input().split())
cont = 1
for i in range(1, y+1):
    if cont != x:
        print(i, end=' ')
        cont += 1
    else:
        print(i)
        cont = 1
