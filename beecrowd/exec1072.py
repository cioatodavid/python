n = int(input())
arein, areout = 0, 0

for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        arein += 1
    else:
        areout += 1
print(f'{arein} in')
print(f'{areout} out')