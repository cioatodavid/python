A,B,C = map(float, input().split())

triret = A * C / 2
areacirc = 3.14159 * (C**2)
areatrap = ((A + B) * C) / 2
areaquad = B * B
arearet = A * B

print(f'TRIANGULO: {triret:.3f}')
print(f'CIRCULO: {areacirc:.3f}')
print(f'TRAPEZIO: {areatrap:.3f}')
print(f'QUADRADO: {areaquad:.3f}')
print(f'RETANGULO: {arearet:.3f}')
