r = float(input())


def volume(r):
    v = (4/3) * (3.14159 * (r**3))
    return v


print(f'VOLUME = {volume(r):.3f}')
