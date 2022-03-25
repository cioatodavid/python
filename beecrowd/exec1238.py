n = int(input())

for i in range(0, n):
    a, b = input().split()
    t1, t2 = len(a), len(b)
    final = []

    if t1 > t2:
        maior = t1

    else:
        maior = t2

    for j in range(maior):
        if j < t1:
            final.append(a[j])
        if j < t2:
            final.append(b[j])
    template = ''.join(final)
    print(template)
