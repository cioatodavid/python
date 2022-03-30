contador = 1
while True:
    try:
        ncase = 1
        entrada = int(input())

        for i in range(entrada + 1):
            ncase += i

        if ncase == 1:
            print(f'Caso {contador}: {ncase} numero')
        else:
            print(f'Caso {contador}: {ncase} numeros')

        if entrada == 0:
            print(0)
        else:
            print(0, end=' ')

        for i in range(entrada+1):
            for j in range(i):
                if i == entrada and j == entrada - 1:
                    print(i)
                else:
                    print(i, end=' ')

        print()
        contador += 1
    except:
        break
