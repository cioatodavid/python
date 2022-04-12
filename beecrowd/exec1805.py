x, y = map(int, input().split())

totSum = y*(y+1)//2

minSum = x*(x+1)//2

print((totSum - minSum)+x)
