
while True:
    try:
        soma = 0
        x, y = map(int, input().split())
        if x > 0 and y > 0:
            if x < y:
                for i in range(x, y + 1):
                    print(i, end=' ')
                    soma += i
                    
            else:
                for i in range(y, x + 1):
                    print(i, end=' ')
                    soma += i
            print(f'Sum={soma}')       
        else:
                
            break
    except EOFError:
        break
    
    