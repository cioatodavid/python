firsttime = True


def valNota(x):
    if x >= 0 and x <= 10:
        return True
    else:
        return False


def calcMedia():

    contMed = 0
    totMed = 0
    while contMed < 2:
        nota = float(input())
        if valNota(nota):
            contMed += 1
            totMed += nota

        else:
            print('nota invalida')

        if contMed == 2:
            print(f'media = {totMed/contMed:.2f}')
            break


calcMedia()
while True:
    print('novo calculo (1-sim 2-nao)')
    nov = int(input())

    if nov == 1:
        calcMedia()
    elif nov == 2:
        break
    else:
        continue
