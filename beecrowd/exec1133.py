x = int(input())
y = int(input())
soma = 0
if x > y:
    x,y = y,x

for i in range(x+1, y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
        
