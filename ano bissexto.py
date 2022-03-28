print('Digite um ano para saber se ele é bissexto: ')
year = int(input())
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
              print('É um ano bissexto')
        else:
            print('Não é um bissexto')   
    else:
        print('É um ano bissexto')
    
else:
    print('Não é um bissexto')
