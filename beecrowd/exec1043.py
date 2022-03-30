a, b, c = map(float, input().split())


def isatriangle(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        return True
    else:
        return False


if isatriangle(a, b, c):
    print('Perimetro = {:.1f}'.format(a+b+c))
else:
    print('Area = {:.1f}'.format((a+b)*c/2))
