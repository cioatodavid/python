n = int(input())
for i in range(n):
    x,y,z = map(float, input().split())
    mediap = (x*2 + y*3 + z*5)/10
    print(f'{mediap:.1f}')