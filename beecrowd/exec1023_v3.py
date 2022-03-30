def floor(n):
    return int(n // 1)


def breakline(boolean):
    if boolean:
        return '\n'
    else:
        return ' '


cont = 0
while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:

            quant, cons = 0, 0
            array = [0] * 300
            for i in range(n):
                tquant, tcons = map(int, input().split())
                array[tcons//tquant] += tquant
                quant += tquant
                cons += tcons
            print(f'Cidade# {cont+1}:')
            cont += 1

            for i in range(300):
                jump = 0
                if array[i] > 0:

                    print(f'{array[i]}-{i}', end=breakline(i == 299))

            print()
            mediaconsumo = round(cons/quant, 2)

            print(f'Consumo medio: {mediaconsumo} m3.')
            print()

    except EOFError:
        break

