m = int(input())
a = int(input())
b = int(input())

if m >= 40 and m <= 110 and a < m and a >= 1 and b < m and b >= 1 and b != a:
    c = m - (a + b)
    print(c)
    