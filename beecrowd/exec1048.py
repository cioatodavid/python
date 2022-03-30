
percentreajuste = [1.04, 1.07, 1.1, 1.12, 1.15]
val = float(input())

if val >= 0 and val <= 400:
    i = 4
    fval = val * percentreajuste[i]
    print(f'Novo salario: {fval:.2f}')
    print(f'Reajuste ganho: {fval - val:.2f}')
    print(f'Em percentual: {round((percentreajuste[i] - 1)*100)} %')
elif val > 400 and val <=800:
    i = 3
    fval = val * percentreajuste[i]
    print(f'Novo salario: {fval:.2f}')
    print(f'Reajuste ganho: {fval - val:.2f}')
    print(f'Em percentual: {round((percentreajuste[i] - 1)*100)} %')
elif val > 800 and val <=1200:
    i = 2
    fval = val * percentreajuste[i]
    print(f'Novo salario: {fval:.2f}')
    print(f'Reajuste ganho: {fval - val:.2f}')
    print(f'Em percentual: {round((percentreajuste[i] - 1)*100)} %')
elif val > 1200 and val <=2000:
    i = 1
    fval = val * percentreajuste[i]
    print(f'Novo salario: {fval:.2f}')
    print(f'Reajuste ganho: {fval - val:.2f}')
    print(f'Em percentual: {round((percentreajuste[i] - 1)*100)} %')
elif val > 2000:
    i = 0
    fval = val * percentreajuste[i]
    print(f'Novo salario: {fval:.2f}')
    print(f'Reajuste ganho: {fval - val:.2f}')
    print(f'Em percentual: {round((percentreajuste[i] - 1)*100)} %')
    