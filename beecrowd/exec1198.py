while True:
    try:
        x,y = map(int,input().split())
        if x > y:
            x,y = y,x
            
        print(y-x)
            
    except EOFError:
        break