cedList = [100, 50, 20, 10, 5, 2, 1]
curValue = int(input(''))
print(curValue)
for cedul in cedList:
    curCedul = curValue // cedul
    curValue = curValue % cedul
    print(f'{curCedul} nota(s) de R$ {cedul},00')