cedList = [100, 50, 20, 10, 5, 2, 1]
curValue = int(input('Valor desejado: R$ '))
print('-' * 20)
for cedul in cedList:
    curCedul = curValue // cedul
    curValue = curValue % cedul
    if curCedul > 0:
        print(f'{curCedul} cédulas de R$ {cedul}')