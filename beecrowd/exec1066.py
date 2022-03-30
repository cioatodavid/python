par,imp,neg,pos = 0,0,0,0
for i in range(5):
    x = float(input())
    if x%2 == 0 and x != 0:
        par += 1
    elif x%2 != 0 and x != 0:
        imp += 1
    if x < 0:
        neg += 1
    if x > 0:
        pos += 1
    if x == 0:
        par += 1
        
print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')        
