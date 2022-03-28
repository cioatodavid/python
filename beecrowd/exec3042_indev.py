from ctypes.wintypes import PINT


m = int(input())
obstacles = []
pos = [0, 1]

for i in range(m+1):
    l = list(map(int, input().split()))
    obstacles.append(l)

