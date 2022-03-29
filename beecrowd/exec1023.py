from hashlib import new
import math
allquant = []
allcons = []
indexlist = []


def sortall(cons, quant):
    for i in range(len(cons)):
        for j in range(len(cons)):
            if cons[j] < cons[i]:
                cons[i], cons[j] = cons[j], cons[i]
                quant[i], quant[j] = quant[j], quant[i]
    revcon = cons[::-1]
    revquant = quant[::-1]
    return revcon, revquant


def findduplicates(cons, quant):
    for i in range(len(cons)):
        for j in range(len(cons)):
            if cons[i] == cons[j] and i != j:
                quant[i] += quant[j]
                cons[j] = 'x'
                quant[j] = 'x'
    ran = len(cons)

    for v in range(ran):
        try:
            if cons[v] == 'x':
                cons.pop(v)
                quant.pop(v)
                ran -= 1
                v -= 1
        except IndexError:
            pass
    return cons, quant


def breakline(boolean):
    if boolean:
        return '\n'
    else:
        return ' '


contador = 0
while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            for cid in range(n):
                quant, cons = map(int, input().split())
                allquant.append(quant)
                cons = math.floor(cons / quant)
                allcons.append(cons)

        allcons, allquant = sortall(allcons, allquant)
        newc, newq = findduplicates(allcons, allquant)

        contador += 1
        print(f'Cidade#{contador}')

        for i in range(len(newc)):

            print(f'{newq[i]}-{newc[i]}', end=breakline(i == len(newc)-1))

        newq, new = [], []
        allquant.clear()
        allcons.clear()
    except EOFError:
        break
