import math

print('Digite um ano para saber se ele é bissexto: ')
year = int(input())
if math.remainder(year,4) == 0:
    if math.remainder(year,100) == 0:
        if math.remainder(year,400) == 0:
              print('É um ano bissexto')
        else:
            print('Não é um bissexto')   
    else:
        print('É um ano bissexto')
    
else:
    print('Não é um bissexto')
