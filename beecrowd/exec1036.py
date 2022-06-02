def bhaskara(a, b, c):
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        return "Impossivel calcular"
    else:
        try:
            x1 = (-b + (delta ** 0.5)) / (2 * a)
            x2 = (-b - (delta ** 0.5)) / (2 * a)
            return x1, x2
        except:
            return "Impossivel calcular"


a, b, c = map(float, input().split())
temp = bhaskara(a, b, c)
if temp == 'Impossivel calcular':
    print(temp)
else:
    print("R1 = {:.1f}".format(temp[0]))
    print("R2 = {:.1f}".format(temp[1]))
