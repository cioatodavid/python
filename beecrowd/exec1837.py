a,b = map(int, input().split())

q = a//b
r = a%b

if r < 0:
    if q < 0:
        q = q - 1
if q > 0:
    q = q + 1
        
r = a - (q*b)

print(q,r)