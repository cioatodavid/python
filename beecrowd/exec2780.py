D = int(input())


def verify(dist):
    if D >= 0 and D <= 800:
        return 1
    elif D > 800 and D <= 1400:
        return 2
    elif D > 1400 and D <= 2000:
        return 3


print(verify(D))
