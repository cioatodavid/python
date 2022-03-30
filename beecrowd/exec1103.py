while True:
    try:
        total = 0
        h1,m1,h2,m2 = map(int,input().split())
        if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
            break
        else:
            start = h1*60 + m1
            end = h2*60 + m2
            
            if start > end:
                end += 1440
                total = end - start
                print(total)
            else:
                total = end - start
                print(total)
    except:
        break
    
    