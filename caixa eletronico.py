curValue = int(input('Valor desejado: R$ '))
print('-' * 20)
for cedul in [100, 50, 20, 10, 1]:
    curCedul = curValue // cedul
    curValue = curValue % cedul
    if curCedul > 0:
        print(f'{curCedul} cédulas de R$ {cedul}')