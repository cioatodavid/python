valor = float(input())
if valor <= 2000.00:
    print('Isento')
elif valor <= 3000.00:
    print('R$ {:.2f}'.format((valor - 2000.00) * 0.08))
elif valor <= 4500.00:
    print('R$ {:.2f}'.format((valor - 3000.00) * 0.18 + (1000.00 * 0.08)))
elif valor > 4500.00:
    print('R$ {:.2f}'.format((valor - 4500.00) * 0.28 + (1500.00 * 0.18) + (1000.00 * 0.08)))