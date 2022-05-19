n = int(input())


def splitval(string):
    return list(string)


def dict(curVal):
    switch = {
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6,
        '0': 6
    }

    return switch.get(curVal, 'err: valor inexistente')

for i in range(n):
    soma = 0
    values = str(input())
    for val in splitval(values):
        soma += dict(val)
    print(f'{soma} leds')
