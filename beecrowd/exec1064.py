cont = 0
total = 0
for i in range(6):

    x = float(input())
    if x > 0:
        cont += 1
        total += x
print(f'{cont} valores positivos')
print(f'{total / cont:.1f}')