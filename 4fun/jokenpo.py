from random import randint

print('-_'*20)
print('Escolha 1-Pedra 2-Papel 3-Tesoura: ')
print('-_'*20)
p_Chosen = int(input())
bot_Chosen = randint(1,3)
print('{} vs {}'.format(p_Chosen, bot_Chosen))
if p_Chosen == bot_Chosen:
    print('Empatou :p')
elif p_Chosen == 1 and bot_Chosen == 2:
      print('Perdeu :o')
elif p_Chosen == 3 and bot_Chosen == 1:
      print('Perdeu :o')
elif p_Chosen == 2 and bot_Chosen == 3:
      print('Perdeu :o')
      
else:
     print('Ganhou :D')   