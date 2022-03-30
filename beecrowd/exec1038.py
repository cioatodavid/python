dict = {
    1: 4,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
}

x,y = map(int, input().split())
total = dict[x] * y
print(f'Total: R$ {total:.2f}')
