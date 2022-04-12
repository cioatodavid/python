x1, y1, x2, y2 = map(int, input().split())
from math import sqrt

def retbounds(b, a, q, p):
    res = (2*p*q*a)+
    return res
if x1 > y1:
    x1, y1 = y1, x1
if x2 > y2:
    x2, y2 = y2, x2


if x1 > x2:
    print('no')
elif x1 <= x2 and y1 <= y2:
    print('yes')
elif x1 <= x2 and y1 > y2 and (x1**2 + y1**2) > (x2**2 + y2**2):
    print('no')
elif x1 <= x2 and y1 > y2 and (x1**2 + y1**2) <= (x2**2 + y2**2):
    if retbounds(x1, y1, x2, y2) <= y2:
        print('yes')
    else:
        print('no')
print(retbounds(x1, y1, x2, y2), y2)