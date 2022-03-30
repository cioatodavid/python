a,b,c = sorted(list(map(float, input().split())),reverse=True)
forma = bool
if a >= b+c:
    print('NAO FORMA TRIANGULO')
    bool = False
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
    forma = True
elif a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')
    forma = True
elif a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')
    forma = True
if forma == True and a == b == c:
    print('TRIANGULO EQUILATERO')
elif forma == True and a == b or b == c or a == c:
    print('TRIANGULO ISOSCELES')

