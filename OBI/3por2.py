import math
n = int(input())
lista = []

for i in range(n):
    x = int(input())
    lista.append(x)

lista.sort(reverse=True)

tam = math.floor(len(lista)/3)
curInd = 0

for j in range(tam):
    curInd += 3
    lista.pop(curInd-1)
    curInd -= 1

print(sum(lista))
