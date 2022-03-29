def floor(n):
    return int(n // 1)
contador = 0


def breakline(boolean):
    if boolean:
        return '\n'
    else:
        return ' '


def consumoreal(cons, quant):
    consumo = 0
    quantidade = 0
    for i in range(len(cons)):
        consumo += cons[i]
        quantidade += quant[i]
        total = consumo / quantidade
    return total


while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            newquant = []
            consumoold = []
            newcons = []
            quant = []
            cons = []

            for cid in range(n):
                quant, cons = map(int, input().split())

                newquant.append(quant)
                consumoold.append(cons)
                temp = floor(cons / quant)
                newcons.append(temp)

        contotal = consumoreal(consumoold, newquant)
        sortq = list(zip(*sorted(zip(newcons, newquant))))[1]
        sortquantidade = list(sortq)
        sortc = sorted(newcons)
        for x in range(len(sortc)):
            if x+1 >= len(sortc):
                break
            if sortc[x] == sortc[x+1]:
                sortquantidade[x+1] += sortquantidade[x]
                sortquantidade.remove(sortquantidade[x])
                sortc.remove(sortc[x])

        contador += 1
        print(f'Cidade# {contador}:')
        for i in range(len(sortquantidade)):

            print(f'{sortquantidade[i]}-{sortc[i]}',
                  end=breakline(i == len(sortquantidade)-1))
        print(f'Consumo medio: {round(contotal,2)} m3\n')

        consumo = 0
        sortc.clear()
        sortquantidade.clear()
    except EOFError:
        break
