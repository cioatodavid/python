while True:
    try:
        n = int(input())
        for i in range(n):
            soma = 0
            x, y = input().split()
            x = int(x)
            y = int(y)
            if x > y:
                x, y = y, x
            for i in range(x+1, y):
                if i % 2 != 0:
                    soma += i
            print(soma)
        break
    except:
        break