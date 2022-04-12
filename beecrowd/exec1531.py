def fastfib(n):
    nbinary = bin(n)[2:] 
    f = [0, 1]  
 
    for b in nbinary:
        f2i1 = f[1]**2 + f[0]**2  
        f2i = f[0]*(2*f[1]-f[0]) 
 
        if b == '0':
            f[0], f[1] = f2i, f2i1  
        else:
            f[0], f[1] = f2i1, f2i1+f2i
 
    return f[0]

while True:
    try:
        x, y = map(int, input().split())
        xy = fastfib(x) % y
        print(xy)
        
    except EOFError:
        break
    
