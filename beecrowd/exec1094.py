animais = {
    'C': 'Coelho',
    'R': 'Rato',
    'S': 'Sapo',
}
tc, ts, tr = 0, 0, 0
n = int(input())
for i in range(n):
    quant, animal = map(str, input().split())
    quant = int(quant)
    if animal == 'C':
        tc += quant
    elif animal == 'R':
        tr += quant
    elif animal == 'S':
        ts += quant
print(f'Total: {tc + tr + ts} cobaias')
print(f'Total de coelhos: {tc}')
print(f'Total de ratos: {tr}')
print(f'Total de sapos: {ts}')
print(f'Percentual de coelhos: {tc / (tc + tr + ts) * 100:.2f} %')
print(f'Percentual de ratos: {tr / (tc + tr + ts) * 100:.2f} %')
print(f'Percentual de sapos: {ts / (tc + tr + ts) * 100:.2f} %')

