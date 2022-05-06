from math import sqrt


def isprime(n):

    if (n <= 1):
        return False

    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False

    return True


while True:
    try:
        listamoedas = []
        nmoedas = int(input())
        for i in range(nmoedas):
            listamoedas.append(int(input()))
        jumpby = int(input())

        listamoedas.reverse()
        slicedmoedas = list(listamoedas[::jumpby])
        summoedas = sum(slicedmoedas)

        if isprime(summoedas):
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
            continue
        else:
            print('Bad boy! I’ll hit you.')
            continue

    except EOFError:
        break
