cedList = [100, 50, 20, 10, 5, 2]
curValue = float(input(''))
print(curValue)
resValue = 0
for cedul in cedList:
    curCedul = curValue // cedul
    curValue = curValue % cedul
    resValue = curValue % cedul
    print(f'{int(curCedul)} nota(s) de R$ {cedul}.00')
resValue = round(resValue, 2)
moeList = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
for moe in moeList:
    curMoe = resValue // moe
    resValue = resValue % moe
    strMoe = str(moe).replace(',', '.')
    print(f'{int(curMoe)} moeda(s) de R$ {float(strMoe):.2f}')