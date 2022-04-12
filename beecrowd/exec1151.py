n = int(input())
count = 0
fibVal = []

for i in range(n):
    if i == 0:
        fibVal.append(0)
    elif i == 1:
        fibVal.append(1)
    else:
        fibVal.append(fibVal[i-1] + fibVal[i-2])

for i in range(n):
    if i == n-1:
        print(fibVal[i])
    else:
        print(fibVal[i], end=' ')
