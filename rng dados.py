from random import randint
from time import sleep

gameData = dict()
results = list()
count = 0

for i in range(4):
    count += 1
    gameData[f'player{count}'] = randint(1,6)
    results.append()
    
print(results)


""" count = 0

for e in results:
    for v in e.items():
        
        if v[0] == 'name':
            playerData.append(v[1])
               
        if v[0] == 'diceValue':
                diceData.append(v[1])
                print(f'o {playerData[count]} tirou {v[1]} no dado')    
                count += 1


print(playerData)
diceData.sort(reverse=True)
print(diceData)
     """