caso = 0
numcaso = 0
allnumber = []
while True:
    try:
        entrada = int(input())
        if caso == 0:
            allnumber.append(entrada)
            numcaso += 1
            caso += 1
            print(f'Caso {caso}: {numcaso} numero')
            print(0)            
            print()
            
        else:
            numcaso = numcaso + entrada
            caso = caso + 1
            print(f'Caso {caso}: {numcaso} numeros')
            for i in range(entrada):
                allnumber.append(entrada) 
                
            for item in allnumber:
                print(item, end=' ')
            
            print()
            print()
    
    except EOFError:
        break