s, t, f = map(int, input().split())

temp = s + t + f
if temp >= 24:
        temp = (24 - temp) *-1
        
elif temp <= 0:
        temp = 24 + temp
 


print(temp)